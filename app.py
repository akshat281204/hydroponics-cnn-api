import gradio as gr
import tensorflow as tf
from PIL import Image
import numpy as np

# loading the model
try:
    model=tf.keras.models.load_model("models/spinach_disease_classifier.h5")
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading the model: {e}")
    model=None

CLASS_NAMES=['Leaf Spot','Healthy','Mite Damage']

def predict_image(input_image: Image.Image):
    if model is None:
        print("Error loading the model, Check the logs")
    
     # preprocessing the image
    img = input_image.convert("RGB").resize((224, 224))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # making the predictions
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = CLASS_NAMES[predicted_class_index]
    
    # returning a dictionary of labels
    confidence_scores = {CLASS_NAMES[i]: float(prediction[0][i]) for i in range(len(CLASS_NAMES))}
    return confidence_scores

# creating gradio interface
iface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil", label="Upload Spinach Leaf Image"),
    outputs=gr.Label(num_top_classes=3, label="Prediction"),
    title="Spinach Disease Classifier",
    description="Upload an image of a spinach leaf to classify its health status."
)

# launch the api
if __name__ == "__main__":
    iface.launch()