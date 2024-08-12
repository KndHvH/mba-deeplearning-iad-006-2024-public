import os
import requests
import io
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

class ApiService:
    def __init__(self) -> None:
        self._url = os.getenv("API_URL")
    
    def predict(self, canvas_result):
        img = Image.fromarray((canvas_result.image_data * 255).astype('uint8'))
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        response = requests.post(self._url + "/predict", files={"file": img_byte_arr})
        return response.json()["prediction"]