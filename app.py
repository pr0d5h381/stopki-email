import streamlit as st
import json
import os
import unicodedata
from template import SignatureTemplate
import webbrowser
from pathlib import Path
import base64
import hashlib

# Polish characters mapping
POLISH_CHARS = {
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 
    'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
    'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
    'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
}

# Production URL for Streamlit Cloud
BASE_URL = "https://stopki-email-eweehzc3dd6nudamxntkop.streamlit.app"

# Load configuration
def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Save configuration
def save_config(config_data):
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)

# Generate email from name
def generate_email(name, domain):
    if not name:
        return ""
    
    # Replace Polish characters
    for polish, latin in POLISH_CHARS.items():
        name = name.replace(polish, latin)
    
    # Convert to lowercase
    name = name.lower()
    
    # Replace spaces with dots and remove special characters
    name = '.'.join(name.split())
    
    # Remove any remaining special characters
    name = ''.join(c for c in name if c.isalnum() or c == '.')
    
    return f"{name}@{domain}"

# Generate public preview link
def generate_preview_link(email):
    # Create a hash of the email to use as a preview token
    preview_token = hashlib.sha256(email.encode()).hexdigest()[:16]
    return f"{BASE_URL}?preview={preview_token}"

# Save signature
def save_signature(data):
    # Ensure signatures directory exists
    os.makedirs("signatures", exist_ok=True)
    
    # Generate preview token
    preview_token = hashlib.sha256(data['email'].encode()).hexdigest()[:16]
    data['preview_token'] = preview_token
    
    # Save JSON data
    json_path = os.path.join("signatures", f"{data['email']}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Generate and save HTML
    html_content = SignatureTemplate.generate_html(data)
    html_path = os.path.join("signatures", f"{data['email']}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    return html_path

# List all signatures
def list_signatures():
    signatures = []
    if os.path.exists("signatures"):
        for file in os.listdir("signatures"):
            if file.endswith(".json"):
                with open(os.path.join("signatures", file), 'r', encoding='utf-8') as f:
                    signatures.append(json.load(f))
    return signatures

# Delete signature
def delete_signature(email):
    json_path = os.path.join("signatures", f"{email}.json")
    html_path = os.path.join("signatures", f"{email}.html")
    
    if os.path.exists(json_path):
        os.remove(json_path)
    if os.path.exists(html_path):
        os.remove(html_path)

# Load signature data
def load_signature(email):
    json_path = os.path.join("signatures", f"{email}.json")
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

# Find signature by preview token
def find_signature_by_token(preview_token):
    signatures = list_signatures()
    for sig in signatures:
        if sig.get('preview_token') == preview_token:
            return sig
    return None

# Config editor section
def config_editor():
    st.title("Edytor Konfiguracji")
    
    config = load_config()
    modified = False
    
    # Email domain
    email_domain = st.text_input("Domena Email", value=config['email_domain'])
    if email_domain != config['email_domain']:
        config['email_domain'] = email_domain
        modified = True
    
    # Departments
    st.subheader("Oddziały")
    departments = config['departments']
    for i, dept in enumerate(departments):
        col1, col2 = st.columns([4, 1])
        with col1:
            new_dept = st.text_input(f"Oddział {i+1}", value=dept, key=f"dept_{i}")
            if new_dept != dept:
                departments[i] = new_dept
                modified = True
        with col2:
            if st.button("🗑️", key=f"del_dept_{i}"):
                departments.pop(i)
                modified = True
                st.rerun()
    
    if st.button("➕ Dodaj Oddział"):
        departments.append("Nowy Oddział")
        modified = True
        st.rerun()
    
    # Positions
    st.subheader("Stanowiska")
    positions = config['positions']
    for i, pos in enumerate(positions):
        col1, col2 = st.columns([4, 1])
        with col1:
            new_pos = st.text_input(f"Stanowisko {i+1}", value=pos, key=f"pos_{i}")
            if new_pos != pos:
                positions[i] = new_pos
                modified = True
        with col2:
            if st.button("🗑️", key=f"del_pos_{i}"):
                positions.pop(i)
                modified = True
                st.rerun()
    
    if st.button("➕ Dodaj Stanowisko"):
        positions.append("Nowe Stanowisko")
        modified = True
        st.rerun()
    
    # Addresses
    st.subheader("Adresy")
    addresses = config['addresses']
    for i, addr in enumerate(addresses):
        col1, col2 = st.columns([4, 1])
        with col1:
            new_addr = st.text_input(f"Adres {i+1}", value=addr, key=f"addr_{i}")
            if new_addr != addr:
                addresses[i] = new_addr
                modified = True
        with col2:
            if st.button("🗑️", key=f"del_addr_{i}"):
                addresses.pop(i)
                modified = True
                st.rerun()
    
    if st.button("➕ Dodaj Adres"):
        addresses.append("Nowy Adres")
        modified = True
        st.rerun()
    
    # Company data
    st.subheader("Dane Firmowe")
    company_data = config['company_data']
    
    # Default department
    default_department = st.selectbox(
        "Domyślny Oddział",
        options=departments,
        index=departments.index(company_data['default_department']) if company_data['default_department'] in departments else 0
    )
    if default_department != company_data['default_department']:
        company_data['default_department'] = default_department
        modified = True
    
    # Default address
    default_address = st.selectbox(
        "Domyślny Adres",
        options=addresses,
        index=addresses.index(company_data['default_address']) if company_data['default_address'] in addresses else 0
    )
    if default_address != company_data['default_address']:
        company_data['default_address'] = default_address
        modified = True
    
    # Social media and website
    for key in ['website', 'facebook', 'linkedin', 'instagram', 'youtube']:
        new_value = st.text_input(f"Link {key.title()}", value=company_data[key])
        if new_value != company_data[key]:
            company_data[key] = new_value
            modified = True
    
    # Disclaimer
    new_disclaimer = st.text_area("Treść Informacji", value=company_data['disclaimer'], height=200)
    if new_disclaimer != company_data['disclaimer']:
        company_data['disclaimer'] = new_disclaimer
        modified = True
    
    # Save changes
    if modified:
        save_config(config)
        st.success("Konfiguracja została zapisana!")
        st.rerun()

# Main Streamlit app
def main():
    st.set_page_config(page_title="Generator Stopki Email", layout="wide")
    
    # Check if this is a preview request
    if "preview" in st.query_params:
        preview_token = st.query_params["preview"]
        signature = find_signature_by_token(preview_token)
        if signature:
            st.components.v1.html(SignatureTemplate.generate_html(signature), height=600)
            return
        else:
            st.error("Nieprawidłowy link podglądu")
            return
    
    config = load_config()
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = "Lista Stopek"
    
    # Sidebar for navigation
    st.sidebar.title("Menu")
    page = st.sidebar.radio(
        "Wybierz opcję:",
        ["Lista Stopek", "Nowa Stopka", "Konfiguracja"],
        index=0 if st.session_state.page == "Lista Stopek" else 
              1 if st.session_state.page == "Nowa Stopka" else 2
    )
    
    if page == "Konfiguracja":
        config_editor()
    elif page == "Lista Stopek":
        st.title("Lista Stopek Email")
        
        # Add New Signature button
        if st.button("➕ Dodaj Nową Stopkę", type="primary"):
            st.session_state.page = "Nowa Stopka"
            st.rerun()
            
        # Display signatures in a table
        signatures = list_signatures()
        if signatures:
            for sig in signatures:
                col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
                with col1:
                    st.write(f"**{sig['name']}** ({sig['email']})")
                with col2:
                    preview_link = generate_preview_link(sig['email'])
                    st.markdown(f'<a href="{preview_link}" target="_blank">👁️ Podgląd</a>', unsafe_allow_html=True)
                with col3:
                    if st.button("🔗 Link", key=f"link_{sig['email']}"):
                        preview_link = generate_preview_link(sig['email'])
                        st.code(preview_link)
                with col4:
                    if st.button("✏️ Edytuj", key=f"edit_{sig['email']}"):
                        st.session_state.edit_email = sig['email']
                        st.session_state.page = "Nowa Stopka"
                        st.rerun()
                with col5:
                    if st.button("🗑️ Usuń", key=f"delete_{sig['email']}"):
                        if st.session_state.get(f'delete_confirm_{sig["email"]}', False):
                            delete_signature(sig['email'])
                            st.success("Stopka została usunięta!")
                            st.rerun()
                        else:
                            st.session_state[f'delete_confirm_{sig["email"]}'] = True
                            st.warning("Kliknij ponownie, aby potwierdzić usunięcie.")
                st.divider()
        else:
            st.info("Brak zapisanych stopek. Kliknij 'Dodaj Nową Stopkę' aby utworzyć pierwszą stopkę.")
            
    else:  # Nowa Stopka
        st.title("Generator Stopki Email")
        
        # Initialize form data from edit if needed
        initial_data = {}
        if hasattr(st.session_state, 'edit_email'):
            initial_data = load_signature(st.session_state.edit_email)
            if initial_data is None:
                initial_data = {}
        
        # Create two columns for the form
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Dane Pracownika")
            name = st.text_input("Imię i nazwisko", value=initial_data.get('name', ''))
            
            # Auto-generate email based on name
            if name:
                email = generate_email(name, config['email_domain'])
            else:
                email = initial_data.get('email', '')
            email = st.text_input("Email", value=email)
            
            phone = st.text_input("Numer telefonu", value=initial_data.get('phone', ''))
            position = st.selectbox("Stanowisko", config['positions'], 
                                  index=config['positions'].index(initial_data['position']) if initial_data.get('position') in config['positions'] else 0)
            
            department = st.selectbox("Oddział", config['departments'],
                                    index=config['departments'].index(config['company_data']['default_department']))
            
            address = st.selectbox("Adres", config['addresses'],
                                 index=config['addresses'].index(config['company_data']['default_address']))
            
        with col2:
            st.subheader("Dane Dodatkowe")
            profile_image = st.text_input("Link do zdjęcia profilowego", value=initial_data.get('profile_image', ''))
            website = st.text_input("Strona internetowa", value=config['company_data']['website'])
            facebook = st.text_input("Facebook", value=config['company_data']['facebook'])
            linkedin = st.text_input("LinkedIn", value=config['company_data']['linkedin'])
            instagram = st.text_input("Instagram", value=config['company_data']['instagram'])
            youtube = st.text_input("YouTube", value=config['company_data']['youtube'])
        
        st.subheader("Informacja")
        disclaimer = st.text_area("Treść informacji", value=config['company_data']['disclaimer'], height=100)
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("💾 Zapisz", type="primary"):
                if not email:
                    st.error("Email jest wymagany!")
                else:
                    data = {
                        'name': name,
                        'email': email,
                        'phone': phone,
                        'position': position,
                        'department': department,
                        'address': address,
                        'profile_image': profile_image,
                        'website': website,
                        'facebook': facebook,
                        'linkedin': linkedin,
                        'instagram': instagram,
                        'youtube': youtube,
                        'disclaimer': disclaimer
                    }
                    html_path = save_signature(data)
                    st.success("Stopka została zapisana!")
                    
                    # Generate and show preview link
                    preview_link = generate_preview_link(email)
                    st.markdown(f'<a href="{preview_link}" target="_blank">🔗 Otwórz podgląd w nowej karcie</a>', unsafe_allow_html=True)
                    st.code(preview_link)
                    
                    # Clear edit state if it exists
                    if hasattr(st.session_state, 'edit_email'):
                        del st.session_state.edit_email
                    
                    # Return to list view
                    st.session_state.page = "Lista Stopek"
                    st.rerun()
        
        with col2:
            if st.button("❌ Anuluj"):
                if hasattr(st.session_state, 'edit_email'):
                    del st.session_state.edit_email
                st.session_state.page = "Lista Stopek"
                st.rerun()

if __name__ == "__main__":
    main()
