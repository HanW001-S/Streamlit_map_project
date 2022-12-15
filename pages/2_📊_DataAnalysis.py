import streamlit as st
from streamlit.logger import get_logger
from PIL import Image
image_1 = Image.open('data/image_1.jpg')
image_2 = Image.open('data/image_2.jpg')
image_3 = Image.open('data/image_3.jpg')
image_4 = Image.open('data/image_4.jpg')
image_5 = Image.open('data/image_5.jpg')

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="DataAnalysis")

    st.write("# 숫자로 보는 청년친화강소기업")
    
    st.image(image_1)
    st.image(image_2)
    st.image(image_3)
    st.image(image_4)
    st.image(image_5, caption='©청년워크넷')
    
if __name__ == "__main__":
    run()