# onboarding_app.py

import streamlit as st
import pytesseract
import pandas as pd
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

# 🔧 Set the Tesseract path (change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 📄 Utility function: Extract text from uploaded document
def extract_text_from_file(uploaded_file):
    with tempfile.TemporaryDirectory() as path:
        if uploaded_file.type == "application/pdf":
            images = convert_from_path(uploaded_file.name, output_folder=path)
        else:
            image = Image.open(uploaded_file)
            images = [image]

        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
    return text

# 👤 Retail Customer Form
def show_retail_form(prefill_data=None):
    prefill_data = prefill_data or {}
    st.subheader("Retail Customer Onboarding")
    name = st.text_input("Full Name", prefill_data.get("name", ""))
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    address = st.text_area("Residential Address", prefill_data.get("address", ""))
    family_members = st.text_input("Family Members Names (comma-separated)")
    demographics = st.selectbox("Income Group", ["Low", "Middle", "High"])
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "address": address,
        "family": family_members.split(",") if family_members else [],
        "income_group": demographics
    }

# 🏢 Business Customer Form
def show_business_form(prefill_data=None):
    prefill_data = prefill_data or {}
    st.subheader("Business Customer Onboarding")
    biz_name = st.text_input("Business Name", prefill_data.get("biz_name", ""))
    reg_no = st.text_input("Registration Number", prefill_data.get("reg_no", ""))
    biz_type =_
