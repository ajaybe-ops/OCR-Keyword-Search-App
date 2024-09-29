import gradio as gr
import pytesseract
from PIL import Image

def ocr_and_search(image, keyword):
    try:
        extracted_text = pytesseract.image_to_string(image)
        if keyword.lower() in extracted_text.lower():
            search_result = f"'{keyword}' found in the text!"
        else:
            search_result = f"'{keyword}' not found in the text."
        return extracted_text, search_result
    except Exception as e:
        return str(e), "OCR failed"

# Define Gradio app
iface = gr.Interface(
    fn=ocr_and_search,
    inputs=[gr.Image(type="pil"), gr.Textbox(label="Keyword")],
    outputs=[gr.Textbox(label="Extracted Text"), gr.Textbox(label="Search Result")],
)

iface.launch()
