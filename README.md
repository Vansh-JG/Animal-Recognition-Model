# 🐾 WildScan - Animal Recognition Model

This project uses **deep learning** to recognize animals in images using a **pre-trained ResNet-50 model**. It takes an image as input and predicts the animal's name using **PyTorch** and **Torchvision**.

## 🚀 Features

* ✅ **Pre-trained ResNet-50 model** for accurate predictions
* 🖼 **Image preprocessing** (resizing, normalizing, converting to tensor)
* 🌍 **Supports ImageNet's extensive label set** for classification
* 📷 **Works with any image** of an animal

## 📥 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/Animal-Recognition-Model.git
cd Animal-Recognition-Model
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)

```
python -m venv env  # Create a virtual environment
source env/bin/activate  # Activate it (Mac/Linux)
# On Windows, use: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install torch torchvision pillow requests
```

## 🎯 Usage

### 🔹 Step 1: Place an Image in the Project Folder
Make sure you have an image of an animal, such as `animal_cheetah.jpg`.

### 🔹 Step 2: Run the Script

```
python animal_recognition.py
```

### 🔹 Step 3: View the Prediction
Example output:

```
Predicted Animal: Cheetah
```

## 📁 Project Structure

```
Animal-Recognition-Model/
│── animal_recognition.py  # Main script for prediction
│── animal_cheetah.jpg  # Example image (replace with your own)
│── README.md  # Documentation
```
