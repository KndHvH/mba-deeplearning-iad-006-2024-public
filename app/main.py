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
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    predict = None
    if st.button("Enviar para Previsão"):
        predict = api_service.predict(canvas_result)
    
    
    if predict is not None:
        st.title(f"Previsão: {predict}")
   