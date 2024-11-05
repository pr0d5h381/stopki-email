import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import json
import unicodedata
from signature_manager import SignatureManager

class SignatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Stopki Email")
        self.root.geometry("1000x800")
        
        self.signature_manager = SignatureManager()
        self.load_config()
        
        # Create notebook for multiple views
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Create frames for different views
        self.list_frame = ttk.Frame(self.notebook)
        self.form_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.list_frame, text='Lista Stopek')
        self.notebook.add(self.form_frame, text='Nowa Stopka')
        
        self.setup_list_view()
        self.setup_form_view()

    def load_config(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                "departments": [],
                "addresses": [],
                "positions": [],
                "company_data": {},
                "email_domain": "podnosniki.pl"
            }

    def generate_email(self, name):
        """Generate email from name"""
        if not name:
            return ""
        # Remove accents and convert to lowercase
        name = ''.join(c for c in unicodedata.normalize('NFKD', name)
                      if not unicodedata.combining(c))
        name = name.lower()
        # Replace spaces with dots and remove special characters
        name = '.'.join(name.split())
        # Remove any remaining special characters
        name = ''.join(c for c in name if c.isalnum() or c == '.')
        return f"{name}@{self.config['email_domain']}"
        
    def setup_list_view(self):
        # Top frame for button
        top_frame = ttk.Frame(self.list_frame)
        top_frame.pack(fill='x', padx=10, pady=5)
        
        add_button = ttk.Button(top_frame, text="Dodaj Nową Stopkę", command=self.show_form_view)
        add_button.pack(side='left')
        
        # Create treeview with scrollbar
        tree_frame = ttk.Frame(self.list_frame)
        tree_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Create treeview
        self.tree = ttk.Treeview(tree_frame, columns=('Email', 'Name', 'Position'), 
                                show='headings', 
                                yscrollcommand=scrollbar.set)
        
        self.tree.heading('Email', text='Email')
        self.tree.heading('Name', text='Imię i Nazwisko')
        self.tree.heading('Position', text='Stanowisko')
        
        # Configure scrollbar
        scrollbar.config(command=self.tree.yview)
        
        self.tree.pack(fill='both', expand=True)
        
        # Bottom frame for buttons
        button_frame = ttk.Frame(self.list_frame)
        button_frame.pack(fill='x', padx=10, pady=5)
        
        # Create buttons with fixed width
        preview_button = ttk.Button(button_frame, text="Podgląd", command=self.preview_selected, width=20)
        preview_button.pack(side='left', padx=5)
        
        edit_button = ttk.Button(button_frame, text="Edytuj", command=self.edit_selected, width=20)
        edit_button.pack(side='left', padx=5)
        
        delete_button = ttk.Button(button_frame, text="Usuń", command=self.delete_selected, width=20)
        delete_button.pack(side='left', padx=5)
        
        self.refresh_list()
        
    def setup_form_view(self):
        # Main container with scrollbar
        main_container = ttk.Frame(self.form_frame)
        main_container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create canvas and scrollbar
        canvas = tk.Canvas(main_container)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        
        # Create main frame for content
        content_frame = ttk.Frame(canvas)
        
        # Configure canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Create window in canvas
        canvas_frame = canvas.create_window((0, 0), window=content_frame, anchor="nw")
        
        # Configure canvas scrolling
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        content_frame.bind('<Configure>', configure_scroll_region)
        
        # Configure canvas resize
        def configure_canvas_size(event):
            canvas.itemconfig(canvas_frame, width=event.width)
        canvas.bind('<Configure>', configure_canvas_size)
        
        # Employee Data Section
        employee_frame = ttk.LabelFrame(content_frame, text="Dane Pracownika", padding=10)
        employee_frame.pack(fill='x', padx=5, pady=5)
        
        # Name field with auto-email generation
        ttk.Label(employee_frame, text="Imię i nazwisko:").grid(row=0, column=0, sticky=tk.W, pady=5)
        name_entry = ttk.Entry(employee_frame, width=50)
        name_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.entries = {'name': name_entry}
        
        # Email field (auto-generated but editable)
        ttk.Label(employee_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        email_entry = ttk.Entry(employee_frame, width=50)
        email_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.entries['email'] = email_entry
        
        # Auto-generate email when name changes
        def on_name_change(*args):
            email = self.generate_email(name_entry.get())
            email_entry.delete(0, tk.END)
            email_entry.insert(0, email)
        name_entry.bind('<KeyRelease>', on_name_change)
        
        # Phone field
        ttk.Label(employee_frame, text="Numer telefonu:").grid(row=2, column=0, sticky=tk.W, pady=5)
        phone_entry = ttk.Entry(employee_frame, width=50)
        phone_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.entries['phone'] = phone_entry
        
        # Position dropdown
        ttk.Label(employee_frame, text="Stanowisko:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.position_var = tk.StringVar()
        position_combo = ttk.Combobox(employee_frame, textvariable=self.position_var, values=self.config['positions'])
        position_combo.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        self.entries['position'] = position_combo
        
        # Department dropdown
        ttk.Label(employee_frame, text="Oddział:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.department_var = tk.StringVar()
        department_combo = ttk.Combobox(employee_frame, textvariable=self.department_var, values=self.config['departments'])
        department_combo.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        self.entries['department'] = department_combo
        
        # Address dropdown
        ttk.Label(employee_frame, text="Adres:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.address_var = tk.StringVar()
        address_combo = ttk.Combobox(employee_frame, textvariable=self.address_var, values=self.config['addresses'])
        address_combo.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
        address_combo.set(self.config['company_data']['default_address'])
        self.entries['address'] = address_combo
        
        # Company Data Section
        company_frame = ttk.LabelFrame(content_frame, text="Dane Firmy", padding=10)
        company_frame.pack(fill='x', padx=5, pady=5)
        
        # Profile image URL
        ttk.Label(company_frame, text="Link do zdjęcia profilowego:").grid(row=0, column=0, sticky=tk.W, pady=5)
        profile_image_entry = ttk.Entry(company_frame, width=50)
        profile_image_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.entries['profile_image'] = profile_image_entry
        
        # Social media and website fields with default values
        social_fields = [
            ("Strona internetowa:", "website"),
            ("Facebook:", "facebook"),
            ("LinkedIn:", "linkedin"),
            ("Instagram:", "instagram"),
            ("YouTube:", "youtube")
        ]
        
        for i, (label, key) in enumerate(social_fields, start=1):
            ttk.Label(company_frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(company_frame, width=50)
            entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=5)
            entry.insert(0, self.config['company_data'][key])
            self.entries[key] = entry
            
        # Disclaimer Section
        disclaimer_frame = ttk.LabelFrame(content_frame, text="Informacja", padding=10)
        disclaimer_frame.pack(fill='x', padx=5, pady=5)
        
        # Disclaimer text area
        self.disclaimer_text = scrolledtext.ScrolledText(disclaimer_frame, wrap=tk.WORD, height=6)
        self.disclaimer_text.pack(fill='x', padx=5, pady=5)
        self.disclaimer_text.insert('1.0', self.config['company_data']['disclaimer'])
        self.entries['disclaimer'] = self.disclaimer_text
        
        # Buttons frame
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(fill='x', padx=5, pady=15)
        
        save_button = ttk.Button(button_frame, text="Zapisz", command=self.save_signature, width=20)
        save_button.pack(side='left', padx=5)
        
        cancel_button = ttk.Button(button_frame, text="Anuluj", command=lambda: self.notebook.select(0), width=20)
        cancel_button.pack(side='left', padx=5)
        
    def show_form_view(self):
        self.notebook.select(1)  # Switch to form view
        self.clear_form()
        
    def clear_form(self):
        for key, entry in self.entries.items():
            if isinstance(entry, ttk.Combobox):
                if key == 'address':
                    entry.set(self.config['company_data']['default_address'])
                else:
                    entry.set('')
            elif isinstance(entry, scrolledtext.ScrolledText):
                entry.delete('1.0', tk.END)
                entry.insert('1.0', self.config['company_data']['disclaimer'])
            else:
                entry.delete(0, tk.END)
                if key in self.config['company_data']:
                    entry.insert(0, self.config['company_data'][key])
            
    def save_signature(self):
        data = {}
        for key, entry in self.entries.items():
            if isinstance(entry, ttk.Combobox):
                data[key] = entry.get()
            elif isinstance(entry, scrolledtext.ScrolledText):
                data[key] = entry.get('1.0', tk.END).strip()
            else:
                data[key] = entry.get()
                
        if not data['email']:
            messagebox.showerror("Błąd", "Email jest wymagany!")
            return
            
        self.signature_manager.save_signature(data)
        messagebox.showinfo("Sukces", "Stopka została zapisana!")
        self.refresh_list()
        self.notebook.select(0)  # Switch back to list view
        
    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        signatures = self.signature_manager.list_signatures()
        for sig in signatures:
            self.tree.insert('', 'end', values=(sig['email'], sig['name'], sig['position']))
            
    def preview_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Ostrzeżenie", "Wybierz stopkę do podglądu!")
            return
            
        email = self.tree.item(selected[0])['values'][0]
        self.signature_manager.preview_signature(email)
        
    def edit_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Ostrzeżenie", "Wybierz stopkę do edycji!")
            return
            
        email = self.tree.item(selected[0])['values'][0]
        data = self.signature_manager.load_signature(email)
        
        if data:
            self.notebook.select(1)  # Switch to form view
            self.clear_form()
            for key, value in data.items():
                if key in self.entries:
                    if isinstance(self.entries[key], ttk.Combobox):
                        self.entries[key].set(value)
                    elif isinstance(self.entries[key], scrolledtext.ScrolledText):
                        self.entries[key].delete('1.0', tk.END)
                        self.entries[key].insert('1.0', value)
                    else:
                        self.entries[key].delete(0, tk.END)
                        self.entries[key].insert(0, value)
                    
    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Ostrzeżenie", "Wybierz stopkę do usunięcia!")
            return
            
        email = self.tree.item(selected[0])['values'][0]
        
        # Double confirmation
        if messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz usunąć tę stopkę?"):
            if messagebox.askyesno("Potwierdzenie", "Ta operacja jest nieodwracalna. Kontynuować?"):
                self.signature_manager.delete_signature(email)
                self.refresh_list()
                messagebox.showinfo("Sukces", "Stopka została usunięta!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()
