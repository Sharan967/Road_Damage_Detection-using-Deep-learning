🛣️ AI-Based Road Damage Detection System (XR Road Intelligence)

An advanced **AI-powered web application** for **automated road damage detection, severity analysis, repair recommendation, cost estimation, and multilingual voice feedback** using **deep learning and computer vision**.

The system supports **image upload and live camera input**, generates **visual heatmaps**, provides **decision intelligence**, and produces **downloadable PDF reports**.  
It is fully deployable on **Streamlit Community Cloud** and accessible from **desktop and mobile devices**.

---

## 🚀 Features

### 🔍 Core AI Capabilities
- Road damage detection using **YOLOv8**
- Damage classification: **Minor, Moderate, Severe**
- Visual **bounding boxes + heatmap overlay**
- Confidence-based detection visualization

### 🧠 Intelligence Layer
- Severity-based decision making:
  - **CRITICAL – Immediate Action Required**
  - **MAINTENANCE REQUIRED**
  - **MONITOR**
- **Auto repair recommendation engine**
- **Repair cost estimation** using Machine Learning (Linear Regression)

### 🎙️ Multilingual Context-Aware Voice
- Real-time voice feedback based on severity and cost
- Supported languages:
  - English
  - Hindi
  - Telugu
  - Tamil
  - Kannada
- Voice speed and tone adapt to damage severity

### 📍 Additional Capabilities
- Live **GPS location capture**
- **SQLite database** for logging detections
- **PDF report generation** (image + details)
- Mobile-friendly web interface
- Futuristic XR-style UI with animations

---

## 🧠 Technology Stack

| Component | Technology |
|---------|-----------|
| Frontend | Streamlit |
| Deep Learning | YOLOv8 (Ultralytics) |
| Image Processing | OpenCV, PIL |
| ML (Cost Estimation) | Scikit-learn |
| Database | SQLite |
| Reporting | ReportLab |
| Voice Output | Browser SpeechSynthesis API |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

road-damage-detection/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── packages.txt # System-level dependencies
├── runs/
│ └── detect/
│ └── rdd_yolov8n/
│ └── weights/
│ └── best.pt # Trained YOLO model
└── README.md


---

## 🛠️ Installation (Local Setup)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/road-damage-detection.git
cd road-damage-detection
2️⃣ Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the App
streamlit run app.py
🌐 Deployment (Streamlit Community Cloud)
Push the project to a public GitHub repository

Ensure requirements.txt and model weights are included

Go to 👉 https://share.streamlit.io

Click New App

Select:

Repository

Branch (main)

Main file: app.py

Click Deploy

🎉 Your app will be live with a public URL and accessible on mobile.

📱 Mobile Usage
Open the deployed URL in Chrome / Edge

Allow camera and microphone permissions

Optionally Add to Home Screen for app-like experience

📊 How It Works (High Level)
User uploads a road image or uses live camera

YOLOv8 detects road damages

Damage area is calculated

ML model estimates repair cost

Severity and decision logic applied

Multilingual voice feedback generated

PDF report created for download

🧪 Example Use Cases
Smart city road monitoring

Municipal road inspection

UAV / drone-based road surveys

Infrastructure maintenance planning

Academic research & hackathons

⚠️ Notes & Limitations
Crack depth estimation is not supported with RGB images

Very thin cracks (<1 cm) require low-altitude, high-resolution input

Voice support depends on browser language availability (best on Chrome / Edge)

🚀 Future Enhancements
UAV (drone) image integration

Road Health Index (0–100)

Historical trend analysis

City-scale damage heatmaps

Emergency alert system for severe damage

Mobile app version

👤 Author
Sai Sharan Guptha

AI | Computer Vision | Smart Infrastructure

📄 License
This project is intended for academic, research, and demonstration purposes.


---

If you want, I can also:
- ✨ Customize README for **research paper / IEEE**
- ✨ Add **screenshots & demo GIFs**
- ✨ Write a **deployment section for UAV use**
- ✨ Optimize it for **hackathon submission**

Just tell me 👍
