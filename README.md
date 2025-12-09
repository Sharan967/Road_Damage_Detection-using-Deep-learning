🛣️ Road Damage Detection (YOLOv8 + Streamlit UI)

A modern deep-learning application that automatically detects potholes, cracks, and road surface damages using YOLOv8, deployed with a sleek dark-mode Streamlit interface.
Built for real-world use cases in smart city development, civil engineering, and road safety monitoring.

🚀 Features
✅ YOLOv8-Based Damage Detection

Detects potholes, cracks, and various road surface defects

Supports JPG, JPEG, PNG images

Fast inference (<100ms depending on hardware)

🎨 Dark-Mode Animated Streamlit UI

Clean, modern, responsive layout

Smooth animations

Easy drag-and-drop interface

📊 Detailed Damage Summary

Displays:

Detected classes

Confidence scores

Severity level

📥 Download Annotated Image

Download the final processed image with bounding boxes.

🧠 Tech Stack
Component	Technology
Model	YOLOv8
Framework	Streamlit
Backend	Python
Image Processing	OpenCV, PIL
Deployment	Local / Cloud
📂 Project Structure

RoadDamageDetection/
│── runs/                    # YOLO output folder
│── dataset/                 # Training dataset (RDD2022)
│── src/
│   ├── app.py               # Streamlit UI
│   ├── train.py             # Training script
│   ├── predict.py           # Prediction test script
│── yolov8n.pt               # Base model (before training)
│── README.md                # Documentation
│── requirements.txt         # Dependencies

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/RoadDamageDetection.git
cd RoadDamageDetection

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows

3️⃣ Install Requirements
pip install -r requirements.txt

🏋️ Train Your Model (Optional)

Place your dataset in:

dataset/RDD2022/


Run training:

python src/train.py


Weights will be stored in:

runs/detect/your_model/weights/best.pt

🖥️ Run Streamlit App
streamlit run src/app.py


Open browser →
http://localhost:8501

📸 UI Preview

<img width="3174" height="1731" alt="image" src="https://github.com/user-attachments/assets/08efa497-c69a-413f-a5b9-10751d34818a" />
<img width="3123" height="1655" alt="image" src="https://github.com/user-attachments/assets/a7985969-1021-4d97-baa1-6039b287aaca" />



📌 Use Cases

Smart road inspection systems

Municipality automated reporting

Civil engineering projects

Autonomous vehicle safety

AI research in infrastructure monitoring

🔥 Future Enhancements

📹 Video-based detection

📍 Real-time location tagging

🚗 Integration with dashcam systems

🌐 Cloud API for large-scale deployment

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📧 Contact

Sai Sharan
📍 India
📩 saisharanvuthuri5256@gmail.com

🔗 www.linkedin.com/in/sai-sharan-guptha-1102512a5

⭐ Support

If you like this project, please give it a star ⭐ on GitHub — it helps a lot!
