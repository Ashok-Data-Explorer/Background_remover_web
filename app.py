import streamlit as st
from rembg import remove
from PIL import Image
import io

# Streamlit interface for image background removal
st.title("Background Remover")
st.write("Upload an image and the background will be removed.")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption='Uploaded Image', use_column_width=True)

    # Process the image
    with st.spinner('Processing...'):
        output_image = remove(input_image)

    # Convert output to a downloadable format
    output_buffer = io.BytesIO()
    output_image.save(output_buffer, format='PNG')
    output_buffer.seek(0)

    st.success("Background removed successfully!")
    st.image(output_image, caption='Processed Image', use_column_width=True)

    # Download link
    st.download_button(
        label="Download Processed Image",
        data=output_buffer,
        file_name="output.png",
        mime="image/png"
    )
