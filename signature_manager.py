import os
import json
from template import SignatureTemplate

class SignatureManager:
    def __init__(self):
        self.signatures_dir = "signatures"
        self.ensure_signatures_directory()
        
    def ensure_signatures_directory(self):
        """Ensure the signatures directory exists"""
        if not os.path.exists(self.signatures_dir):
            os.makedirs(self.signatures_dir)
            
    def save_signature(self, data):
        """Save signature data and generate HTML file"""
        email = data['email']
        
        # Save data as JSON
        json_path = os.path.join(self.signatures_dir, f"{email}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        # Generate and save HTML
        html_content = SignatureTemplate.generate_html(data)
        html_path = os.path.join(self.signatures_dir, f"{email}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
    def load_signature(self, email):
        """Load signature data from JSON file"""
        json_path = os.path.join(self.signatures_dir, f"{email}.json")
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
        
    def delete_signature(self, email):
        """Delete signature files"""
        json_path = os.path.join(self.signatures_dir, f"{email}.json")
        html_path = os.path.join(self.signatures_dir, f"{email}.html")
        
        if os.path.exists(json_path):
            os.remove(json_path)
        if os.path.exists(html_path):
            os.remove(html_path)
            
    def list_signatures(self):
        """List all saved signatures"""
        self.ensure_signatures_directory()
        signatures = []
        for filename in os.listdir(self.signatures_dir):
            if filename.endswith('.json'):
                email = filename[:-5]  # Remove .json extension
                data = self.load_signature(email)
                if data:
                    signatures.append(data)
        return signatures

    def preview_signature(self, email):
        """Open signature HTML in default browser"""
        html_path = os.path.join(self.signatures_dir, f"{email}.html")
        if os.path.exists(html_path):
            os.system(f"open {html_path}")
