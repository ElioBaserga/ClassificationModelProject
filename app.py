import gradio as gr
from transformers import pipeline

vit_classifier = pipeline("image-classification", model="ElioBaserga/fruits-and-vegetables-vit")
clip_detector = pipeline(model="openai/clip-vit-large-patch14", task="zero-shot-image-classification")

labels_fruit_and_vegetable = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

def classify_pet(image):
    vit_results = vit_classifier(image)
    vit_output = {result['label']: result['score'] for result in vit_results}
    
    clip_results = clip_detector(image, candidate_labels=labels_fruit_and_vegetable)
    clip_output = {result['label']: result['score'] for result in clip_results}
    
    return {"ViT Classification": vit_output, "CLIP Zero-Shot Classification": clip_output}

example_images = [
    ["examples/Image_1.jpg"],
    ["examples/Image_3.jpg"],
    ["examples/Image_6.jpg"],
    ["examples/Image_9.jpg"],
    ["examples/Image_5.jpg"]
]

iface = gr.Interface(
    fn=classify_pet,
    inputs=gr.Image(type="filepath"),
    outputs=gr.JSON(),
    title="Fruit and Vegetable Classification Comparison",
    description="Upload an image of a fruit or vegetable, and compare results from a trained ViT model and a zero-shot CLIP model.",
    examples=example_images
)

iface.launch()