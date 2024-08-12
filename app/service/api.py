import os
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import numpy as np

load_dotenv()

class ApiService:
    def __init__(self) -> None:
        self._url = os.getenv("API_URL") if os.getenv("API_URL") else "http://localhost:8000"
    
    def predict(self, img):
        
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        response = requests.post(self._url + "/predict", files={"file": img_byte_arr})
        return response.json()["prediction"]
    
    def crop_image(self, canva_result):
        img = Image.fromarray((canva_result.image_data[:, :, 0]).astype('uint8'), 'L')
        img_array = np.array(img)

        mask = img_array > 0

        coords = np.argwhere(mask)

        if coords.any():
            x0, y0 = coords.min(axis=0) - 10
            x1, y1 = coords.max(axis=0) + 10
            img_cropped = img.crop((y0, x0, y1, x1))
        else:
            img_cropped = img
        
        return img_cropped.resize((8,8), Image.BICUBIC)