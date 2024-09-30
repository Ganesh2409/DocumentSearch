from PIL import Image
import easyocr
import streamlit as st

# Function to extract text using EasyOCR
def extract_text(image_path):
    reader = easyocr.Reader(['en', 'hi'])  # Initialize EasyOCR with English and Hindi
    result = reader.readtext(image_path)
    extracted_text = " ".join([text[1] for text in result])  # Extract the text from the result
    return extracted_text

# Streamlit file uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpeg", "png", "jpg"])

if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Save the image temporarily to pass to EasyOCR
    img.save("temp_img.png")
    
    # Extract text using EasyOCR
    extracted_text = extract_text("temp_img.png")
    st.write("Extracted Text:")
    st.write(extracted_text)

    # Keyword Search
    search_keyword = st.text_input("Enter a keyword to search:")
    if search_keyword:
        if search_keyword in extracted_text:
            st.write(f"Keyword found: {search_keyword}")
        else:
            st.write("Keyword not found")
