import tkinter as tk
from tkinter import ttk, messagebox

class GeneratorStopki:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Stopki Email")
        self.root.geometry("800x900")
        
        # Create main scrollable frame
        main_canvas = tk.Canvas(root)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk.Frame(main_canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )

        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        main_canvas.pack(side="left", fill="both", expand=True)
        
        # Style
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 12, 'bold'))
        
        # Tytuł
        title_label = ttk.Label(scrollable_frame, text="Generator Stopki Email", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Lista pól
        fields = [
            ("Imię i nazwisko:", "name"),
            ("Stanowisko:", "position"),
            ("Oddział:", "department"),
            ("Email:", "email"),
            ("Numer telefonu:", "phone"),
            ("Adres:", "address"),
            ("Strona internetowa:", "website"),
            ("Facebook:", "facebook"),
            ("LinkedIn:", "linkedin"),
            ("Instagram:", "instagram"),
            ("YouTube:", "youtube"),
            ("Link do zdjęcia profilowego:", "profile_image")
        ]
        
        # Tworzenie pól wprowadzania
        self.entries = {}
        for i, (label, key) in enumerate(fields):
            ttk.Label(scrollable_frame, text=label).grid(row=i+1, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(scrollable_frame, width=50)
            entry.grid(row=i+1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
            self.entries[key] = entry
        
        # Przycisk generowania
        generate_button = ttk.Button(scrollable_frame, text="Generuj stopkę", command=self.generate_signature)
        generate_button.grid(row=len(fields)+2, column=0, columnspan=2, pady=20)
            
    def generate_signature(self):
        # Pobieranie wartości z pól
        data = {key: entry.get() for key, entry in self.entries.items()}
        
        # Generowanie HTML
        html_content = self.generate_html(data)
        
        # Zapisywanie do pliku
        with open('wygenerowana_stopka.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        tk.messagebox.showinfo("Sukces", "Stopka została wygenerowana! Zapisano do pliku 'wygenerowana_stopka.html'")
        
    def generate_html(self, data):
        # Podstawowy szablon HTML stopki
        html_template = f'''
<div>
    <style>
        .sh-src a {{
            text-decoration: none !important;
        }}
    </style>
</div>
<br>
<table cellpadding="0" cellspacing="0" border="0" class="sh-src" style="">
    <tr>
        <td style="padding: 0px 1px 0px 0px;">
            <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: separate;">
                <tr>
                    <td align="center" valign="top" style="padding: 0px 25px 0px 0px; vertical-align: top;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 1px 0px 0px;">
                                    <p style="margin: 1px;">
                                        <img src="{data['profile_image']}" 
                                             alt="" 
                                             style="display: block; border: 0px; width: auto; height: 100px; max-width: 100px; object-fit: contain;">
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td valign="top" style="padding: 0px 30px 0px 1px; vertical-align: top;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 1px 0px 0px; font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap;">
                                    <p style="font-family: Arial, sans-serif; font-size: 19px; line-height: 25px; font-weight: 700; color: rgb(0,0,0); white-space: nowrap; margin: 1px;">{data['name']}</p>
                                    <p style="font-family: Arial, sans-serif; font-size: 13px; line-height: 17px; white-space: nowrap; color: rgb(121,121,121); margin: 1px;">{data['position']}</p>
                                    <p style="font-family: Arial, sans-serif; font-size: 13px; line-height: 17px; white-space: nowrap; color: rgb(121,121,121); margin: 1px;">{data['department']}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td style="padding: 1px 0px 0px; border-right: 1px solid rgb(248,173,37);"></td>
                    <td valign="top" style="padding: 0px 1px 0px 30px; vertical-align: top;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 1px 0px 0px;">
                                    <table cellpadding="0" cellspacing="0" border="0" style="">
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-mail"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z" /><path d="M3 7l9 6l9 -6" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <a href="mailto:{data['email']}" style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">
                                                        <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['email']}</span>
                                                    </a>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-phone"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <a href="tel:{data['phone']}" style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">
                                                        <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['phone']}</span>
                                                    </a>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-map-pin"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 11a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" /><path d="M17.657 16.657l-4.243 4.243a2 2 0 0 1 -2.827 0l-4.244 -4.243a8 8 0 1 1 11.314 0z" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['address']}</span>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-phone"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 15l6 -6" /><path d="M11 6l.463 -.536a5 5 0 0 1 7.071 7.072l-.534 .464" /><path d="M13 18l-.397 .534a5.068 5.068 0 0 1 -7.127 0a4.972 4.972 0 0 1 0 -7.071l.524 -.463" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <a href="{data['website']}" style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">
                                                        <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['website']}</span>
                                                    </a>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" style="padding: 15px 0px 15px 0px;">
                                                <table cellpadding="0" cellspacing="0" border="0" style="">
                                                    <tr>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['facebook']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-facebook"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3" /></svg>
                                                            </a>
                                                        </td>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['linkedin']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-linkedin"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M8 11v5" /><path d="M8 8v.01" /><path d="M12 16v-5" /><path d="M16 16v-3a2 2 0 1 0 -4 0" /><path d="M3 7a4 4 0 0 1 4 -4h10a4 4 0 0 1 4 4v10a4 4 0 0 1 -4 4h-10a4 4 0 0 1 -4 -4z" /></svg>
                                                            </a>
                                                        </td>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['instagram']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-instagram"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 8a4 4 0 0 1 4 -4h8a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-8a4 4 0 0 1 -4 -4z" /><path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" /><path d="M16.5 7.5v.01" /></svg>
                                                            </a>
                                                        </td>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['youtube']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-youtube"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M2 8a4 4 0 0 1 4 -4h12a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-12a4 4 0 0 1 -4 -4v-8z" /><path d="M10 9l5 3l-5 3z" /></svg>
                                                            </a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td style="padding: 30px 1px 0px 0px;">
            <table cellpadding="0" cellspacing="0" border="0" style="">
                <tr>
                    <td style="padding: 0px 0px 0px 0px;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 0px 0px 0px;">
                                    <p style="margin: 0px;">
                                        <a href="https://www.podnosniki.pl/">
                                            <img src="https://podnosniki.pl/wp-content/uploads/2024/11/Logo-stopka.png" 
                                                 alt="" 
                                                 width="200"
                                                 height="200" 
                                                 style="display: block; border: 0px; width: 200px; height: 200px;">
                                        </a>
                                    </p>
                                </td>
                                <td style="padding: 0px 0px 0px 0px;">
                                    <p style="margin: 0px;">
                                        <a href="https://www.podnosniki.pl/">
                                            <img src="https://podnosniki.pl/wp-content/uploads/2024/11/Banner-stopka.png" 
                                                 alt="" 
                                                 width="400"
                                                 height="200" 
                                                 style="display: block; border: 0px; width: 400px; height: 200px;">
                                        </a>
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td style="padding: 0px 1px 0px 0px;">
            <table cellpadding="0" cellspacing="0" border="0" style="max-width: 600px;">
                <tr>
                    <td style="padding: 30px 1px 0px 0px; font-family: Arial, sans-serif; font-size: 10px; line-height: 13px; color: rgb(136,136,136);">
                        <p style="font-family: Arial, sans-serif; font-size: 10px; line-height: 13px; color: rgb(136,136,136); margin: 1px;">Treść tej wiadomości jest poufna i przeznaczona wyłącznie dla odbiorcy wskazanego w wiadomości. Surowo zabrania się udostępniania jakiejkolwiek części tej wiadomości osobom trzecim bez pisemnej zgody nadawcy. Jeśli otrzymałeś tę wiadomość przez pomyłkę, prosimy o odpowiedź na tę wiadomość, a następnie jej usunięcie, abyśmy mogli zapewnić, że taka pomyłka nie powtórzy się w przyszłości. 

                            KARCZEWSKI sp. z o.o., ul. Toruńska 20, 86-005 Ciele, NIP: 5543003933, KRS: 0000978104, Regon: 522450199</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
        return html_template

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneratorStopki(root)
    root.mainloop()
