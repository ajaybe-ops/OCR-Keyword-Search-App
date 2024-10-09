import os
import gradio as gr
import pytesseract
from PIL import Image

# Install Tesseract if not present
os.system("apt-get update && apt-get install -y tesseract-ocr")

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Function to perform OCR and keyword search
def ocr_and_search(image, keyword):
    try:
        # Extract text using OCR (Hindi + English)
        extracted_text = pytesseract.image_to_string(image, lang='hin+eng')

        # Perform keyword search
        if keyword.lower() in extracted_text.lower():
            return extracted_text, f"'{keyword}' found in the text!"
        else:
            return extracted_text, f"'{keyword}' not found in the text."
    except Exception as e:
        return str(e), "OCR failed"

# Gradio Interface
iface = gr.Interface(
    fn=ocr_and_search,
    inputs=[gr.Image(type="pil", label="Upload Image"), gr.Textbox(label="Keyword")],
    outputs=[gr.Textbox(label="Extracted Text"), gr.Textbox(label="Keyword Search Result")]
)

# Launch the app
iface.launch()
