# 🛣️ Automated Road Damage Detection Using UAV Images & Deep Learning

An AI-powered web application that detects road damages from images (including UAV/drone imagery), classifies severity, estimates repair costs, recommends maintenance actions, and provides multilingual voice feedback and downloadable reports — all in real time.

---

## 📌 Project Overview

Road infrastructure monitoring is critical for smart cities and public safety. Manual inspection is time-consuming, expensive, and error-prone.  
This project leverages **deep learning (YOLOv8)** and **computer vision** to automate road damage detection and decision-making using images captured from ground cameras or UAVs (drones).

The system is deployed as a **web application using Streamlit**, accessible from both desktop and mobile browsers.

---

## 🎯 Key Features

- 📸 **Image & Live Camera Input**
  - Upload road images
  - Use live camera feed (mobile & desktop)

- 🤖 **AI-Based Road Damage Detection**
  - YOLOv8 deep learning model
  - Detects potholes, cracks, and surface damages

- ⚠️ **Severity Classification**
  - Minor
  - Moderate
  - Severe

- 🧠 **Severity-Based Intelligence**
  - Automatic system decision:
    - MONITOR
    - MAINTENANCE REQUIRED
    - CRITICAL – Immediate Action Required

- 🛠️ **Auto Repair Recommendation Engine**
  - Crack sealing
  - Pothole patching
  - Resurfacing / reconstruction

- 💰 **Repair Cost Estimation**
  - Machine learning–based cost prediction using damage area

- 🌍 **Live GPS Location Capture**
  - Stores latitude & longitude with each detection

- 🎙️ **Multilingual Context-Aware Voice Feedback**
  - English
  - Hindi
  - Telugu
  - Tamil
  - Kannada
  - Voice speed & tone adapt to severity

- 📄 **Automated PDF Report Generation**
  - Damage details
  - Severity
  - Cost
  - Repair recommendations
  - Location & visual evidence

- 🎨 **Advanced XR-Style UI**
  - Futuristic design
  - Dynamic themes
  - Heatmaps and HUD overlays

---

## 🧠 System Architecture

Input Image / Live Camera
↓
YOLOv8 Damage Detection
↓
Damage Area Calculation
↓
Severity Classification
↓
Cost Estimation (ML)
↓
Decision & Repair Recommendation
↓
Multilingual Voice + PDF Report


---

## 📏 Distance & Damage Measurement (UAV Context)

- Uses **pixel-to-real-world conversion** based on Ground Sampling Distance (GSD)
- At typical UAV altitudes (20–30 m):
  - Crack width detection: ~2–3 cm
  - Pothole size detection: ~15–20 cm and above
- Damage dimensions are calculated from detected bounding boxes

---

## 🛠️ Tech Stack

### Frontend & UI
- Streamlit
- HTML/CSS (custom animations & XR UI)

### AI & Computer Vision
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- Pillow

### Machine Learning
- Scikit-learn (Linear Regression for cost estimation)

### Backend & Storage
- SQLite (local database for logs)

### Reporting
- ReportLab (PDF generation)

---

## 📂 Project Structure

road-damage-detection/
│
├── app.py
├── requirements.txt
├── packages.txt
├── runs/
│ └── detect/
│ └── rdd_yolov8n/
│ └── weights/
│ └── best.pt
└── README.md


---

## 🚀 Deployment (Streamlit Community Cloud)

1. Push the project to a **public GitHub repository**
2. Ensure `requirements.txt` is present
3. Go to: https://share.streamlit.io
4. Select repository → branch → `app.py`
5. Click **Deploy**

The app will be accessible via a secure public URL and works on **mobile browsers**.

---

## 📦 Installation (Local Setup)

```bash
pip install -r requirements.txt
streamlit run app.py
⚠️ Browser Recommendations
Best experience: Google Chrome / Microsoft Edge

Voice features may be limited on some browsers

HTTPS required for camera & voice (handled automatically on deployment)

📈 Future Enhancements
3D road surface reconstruction using photogrammetry

Depth estimation using stereo or LiDAR

City-scale damage heatmap dashboards

Predictive road degradation analytics

Mobile app (PWA / Android)

🏆 Use Cases
Smart City Infrastructure Monitoring

Municipal Road Inspection

UAV-based Highway Surveys

Research & Academic Projects

AI Hackathons & Demonstrations

👤 Author
Sai Sharan Guptha
AI & Computer Vision Enthusiast

📜 License
This project is for educational and research purposes.
For commercial or governmental deployment, further validation and testing are recommended.

⭐ Acknowledgements
Ultralytics YOLO

Streamlit Community

Open-source Computer Vision Ecosystem


---

### ✅ What this README does well
- Professional & review-ready
- Explains **why**, not just **what**
- Recruiter & evaluator friendly
- Clear deployment instructions
- Research + real-world balance

If you want next, I can:
- Tailor this README for **IEEE paper / thesis**
- Add **badges & screenshots**
- Write a **short abstract version**
- Create **resume bullet points**

Just tell me 👍
