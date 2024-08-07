import pickle
import numpy as np

class DigitPredictor:
    def __init__(self):
        self.model = self._import_model()

    def predict(self, image):
        image_array = self._preprocess_image(image)
        return self.model.predict([image_array])[0]
    
    def _import_model(self):
        with open('app/model/gradientboost.pkl', 'rb') as file:
            return pickle.load(file)
        
    def _preprocess_image(self, image):
        img = image.convert('L')
        img = img.resize((8, 8))  
        img_array = np.array(img)
        return img_array.flatten()
        