# app.py
import streamlit as st
from fpdf import FPDF
from PIL import Image
import io

st.set_page_config(page_title="Momories AI", layout="centered")
st.title("💖 Momories - Mother's Day Memory Maker")

st.markdown("""
Create a magical memory book for your mom, grandma or loved one. 
Upload an old photo, write a message, and download a personalized AI-generated keepsake.
""")

# Step 1: Upload photo
photo = st.file_uploader("📸 Upload a photo (JPG or PNG)", type=["jpg", "jpeg", "png"])

# Step 2: Custom message
name = st.text_input("👩‍👧 Recipient's name", placeholder="e.g. Mom, Grandma")
message = st.text_area("💌 Write a short message", placeholder="Thank you for always being there for me...")

# Step 3: Generate
if st.button("✨ Generate Momories Book"):
    if not photo or not name or not message:
        st.warning("Please upload a photo and write a message before generating.")
    else:
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 18)
        pdf.cell(0, 10, f"To {name}", ln=True, align="C")

        # Add photo
        image = Image.open(photo)
        image_path = "temp_photo.jpg"
        image.save(image_path)
        pdf.image(image_path, x=30, y=30, w=150)

        pdf.set_font("Arial", size=12)
        pdf.ln(100)
        pdf.multi_cell(0, 10, message)

        # Export
        output = io.BytesIO()
        pdf.output(output)
        st.success("Your memory book is ready!")
        st.download_button("📥 Download PDF", data=output.getvalue(), file_name="momories_book.pdf", mime="application/pdf")

