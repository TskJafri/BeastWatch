# 🚀 Dangerous Animal Identifier

This project uses **Google Gemini AI** to identify animals from images and provide emergency guidance if the animal is dangerous. 

The project is for wildlife detection. There are many villages where wild animals, such as tigers, leopards and wolves, enter unnoticed, and cause chaos and destruction.

We use the power of computer vision and modern technology to help save these animals and the destructions they cause. This goes both ways, as it can save money loss to the villagers and the lives of these animals.

This will soon be connected to an open source computer vision model which monitors CCTV footage (or even your webcam from your phone or laptop), which then processes the data and sends a warning in real-time. 

Further ideas are being considered, such as SMS warnings to people in the area, and wildlife officials, and much more! Stay tuned!

## 📌 Features
- Takes an image and a word input.
- Warns the user if the animal is dangerous.
- Provides danger level (0-10), speed comparison, and additional details.
- Optimized for emergency situations (concise yet informative output).

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install google-generativeai pillow python-dotenv
```

### 2️⃣ Set Up API Key
Create a `key.env` file in the project directory and add:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3️⃣ Run the Pipeline
Open and run the Jupyter Notebook (`pipeline.ipynb`):
```python
from pipeline import process_input  # Ensure your script is named pipeline.ipynb

text_input = "What animal is this?"
image_path = "path/to/your/image.png"

output = process_input(text_input, image_path)
print(output)
```

## 🚀 Pushing to GitHub
Make sure **key.env** is ignored by adding it to `.gitignore`:
```
key.env
```
Then, push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

## 📜 License
This project is open-source. Feel free to modify and improve it!