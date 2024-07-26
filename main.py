import streamlit as st
import qrcode
import os
st.title("QR Code Generator")
text_input = st.text_input("Enter text for QR code:")
if text_input:
    img = qrcode.make(text_input)

    # Save the QR code as a temporary file
    temp_file_path = "temp_qr_code.png"
    img.save(temp_file_path)

    # Display the QR code
    st.image(temp_file_path)
    with open(temp_file_path, "rb") as file:
        st.download_button(label="Download", data=file, file_name="qrcodes.png", mime="application/png")
    os.remove(temp_file_path)



# Add your Streamlit content here

# Inject the AdSense code from a separate HTML file
#HtmlFile = open("adsense.html", "r", encoding="utf-8")
#adsense_code = HtmlFile.read()
#st.components.html(adsense_code)



    # Delete the temporary file