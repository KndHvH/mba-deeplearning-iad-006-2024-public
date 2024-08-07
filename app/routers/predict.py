from fastapi import APIRouter, UploadFile, File
from app.model.predictor import DigitPredictor
import io
from PIL import Image

router = APIRouter()
predictor = DigitPredictor()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    prediction = predictor.predict(image)
    return {"prediction": int(prediction)}
    
