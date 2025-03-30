import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import ssl
import requests

# Disable SSL verification to fix certificate issues
ssl._create_default_https_context = ssl._create_unverified_context

# Load a pretrained ResNet-50 model
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.eval()  # Set to evaluation mode

# Define preprocessing transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Had to resize the image as ResNet
    transforms.ToTensor(),  # Convert image to tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Image Input
image_path = "animal_r.jpg"   # Input the image file here
image = Image.open(image_path)
image = transform(image).unsqueeze(0)  # Add batch dimension

# Make a prediction
with torch.no_grad():
    outputs = model(image)

# Get the predicted class
_, predicted_class = outputs.max(1)

# Download ImageNet class labels with SSL disabled
url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(url, verify=False).text.split("\n")  # Bypass SSL verification

# Print the predicted animal name
animal_name = labels[predicted_class.item()]
print(f"Predicted Animal: {animal_name}")