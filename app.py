# Previous content remains the same, just updating the BASE_URL line
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

# Rest of the file remains exactly the same...
