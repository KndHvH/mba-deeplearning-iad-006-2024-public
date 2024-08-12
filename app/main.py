import streamlit as st
from streamlit_drawable_canvas import st_canvas
from service.api import ApiService

api_service = ApiService()


st.title("Digit Recognizer")

st.write("Desenhe um digito  para obter uma previsão.")

canvas_result = st_canvas(
    stroke_width=10,
    stroke_color="#FFFFFF",
    background_color="#000000",
    height=100,
    width=100,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    predict = None
    image = None
    if st.button("Enviar para Previsão"):
        image = api_service.crop_image(canvas_result)
        predict = api_service.predict(image)

    if image: st.image(image, width=100)
    
    
    if predict is not None:
        st.title(f"Previsão: {predict}")
   