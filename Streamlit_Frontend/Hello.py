import streamlit as st
import streamlit.components.v1 as components

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/premium-photo/fresh-healthy-vegetable-fruits-seen-from-isolated-green-background-with-copy-space_709963-1630.jpg");
    background-size: cover;
}



[data-testid="stSidebar"] {
    background-image : url("https://i.pinimg.com/originals/87/1f/aa/871faa5d438cc3183bee28b1d74907d1.jpg");
    background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.write("# Nutrion! - Empowering Healthier Eating habits")

components.iframe("https://lottie.host/embed/fa657645-4bcc-4a23-9ec1-805ecc8dd7d3/KfPFonPKA7.json", width=700, height=400)
