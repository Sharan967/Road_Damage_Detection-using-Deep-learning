
# 🛣️ Road Damage Detection Intelligence System

### AI-Powered Road Damage Detection, Severity Analysis & Cost Estimation

> **An end-to-end intelligent road inspection system** that leverages **Deep Learning, Computer Vision, GPS, Voice AI, and Data Analytics** to detect road damages, assess severity, estimate repair costs, and generate automated reports — all through a futuristic interactive web interface.

---

## 🚀 Project Overview

The **XR Road Intelligence System** is a real-time, AI-driven application designed to assist governments, municipalities, and infrastructure agencies in **automated road condition monitoring**.

Using **YOLOv8 deep learning models**, the system detects road damages such as potholes and surface defects from images or live camera feeds. It then:

* Classifies damage severity
* Estimates repair cost using ML regression
* Logs GPS-based damage records
* Provides multilingual voice alerts
* Generates professional PDF inspection reports

All wrapped in a **high-end futuristic Streamlit UI**.

---

## ✨ Key Features

### 🔍 Intelligent Damage Detection

* YOLOv8-based object detection
* High-accuracy bounding box localization
* Confidence-based filtering

### 📊 Severity Classification

* **Minor / Moderate / Severe**
* Based on detected damage area
* Rule-based decision engine

### 💰 Automated Cost Estimation

* Machine Learning regression model
* Area-to-cost prediction
* Real-time total repair budget calculation

### 🌍 Live GPS Integration

* Captures latitude & longitude
* Damage logging with location data
* Visual map plotting

### 🔊 Multilingual Voice Assistance

* Languages supported:

  * English
  * Hindi
  * Telugu
  * Tamil
  * Kannada
* Dynamic speech rate & pitch based on severity
* Real-time AI voice alerts (JARVIS-style)

### 📄 Professional PDF Report Generation

* Annotated analyzed image
* Damage summary
* Severity & cost details
* Location metadata
* Downloadable inspection report

### 🧠 Advanced Visualization

* Heatmap-based damage intensity overlay
* HUD-style futuristic UI
* Time-based accent color themes
* Particle & hologram effects

---

## 🛠️ Tech Stack

| Category             | Technologies                     |
| -------------------- | -------------------------------- |
| **Frontend**         | Streamlit, HTML, CSS, JavaScript |
| **Computer Vision**  | OpenCV, YOLOv8 (Ultralytics)     |
| **Machine Learning** | Scikit-learn (Linear Regression) |
| **Deep Learning**    | PyTorch (YOLO backend)           |
| **Database**         | SQLite                           |
| **Reporting**        | ReportLab (PDF generation)       |
| **Voice AI**         | Web Speech API                   |
| **Image Processing** | PIL, NumPy                       |

---

## 🧩 System Architecture

```
Input Image / Live Camera
        ↓
YOLOv8 Damage Detection
        ↓
Damage Area Calculation
        ↓
Severity Classification
        ↓
Cost Estimation (ML Model)
        ↓
Decision Engine
        ↓
Voice Alerts + UI Visualization
        ↓
Database Logging + PDF Report
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/xr-road-intelligence.git
cd xr-road-intelligence
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Place Trained YOLO Model

```text
runs/detect/rdd_yolov8n/weights/best.pt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Input Modes

* 📁 **Image Upload** (JPG / PNG)
* 📷 **Live Camera Feed** (Webcam / Mobile)

---

## 🧠 Decision Logic

| Condition                 | System Decision | Recommendation     |
| ------------------------- | --------------- | ------------------ |
| Severe damage detected    | 🚨 CRITICAL     | Full resurfacing   |
| Multiple moderate damages | ⚠️ MAINTENANCE  | Patching & repair  |
| Minor damage              | 👀 MONITOR      | Routine inspection |

---

## 📂 Database Schema

```sql
logs (
  time TEXT,
  lat REAL,
  lon REAL,
  damage TEXT,
  conf REAL,
  severity TEXT,
  cost REAL
)
```

---

🌍 Real-World Applications

  🏙️ Smart City Infrastructure

  🚧 Highway & Road Maintenance

  🚁 UAV / Drone Road Inspection

  🏛️ Municipal Damage Reporting

  🧑‍🔧 Automated Repair Cost Estimation

🔮 Future Enhancements

 📡 Drone video stream integration

 🛰️ GIS map-based damage clustering

 📈 Dashboard analytics & trends
 
🤖 Automatic repair scheduling

 ☁️ Cloud deployment (AWS / Streamlit Cloud)
---

## 👨‍💻 Developer

**Sai Sharan Guptha**
AI & Computer Vision Enthusiast
📍 India

> *“Building intelligent systems that bridge AI with real-world infrastructure problems.”*

---

## 📜 License

This project is licensed for **academic and research purposes**.
For commercial deployment, please seek appropriate permissions.

---
## Output
<img width="3157" height="1727" alt="Screenshot 2026-02-06 144331" src="https://github.com/user-attachments/assets/612e61aa-bf83-422c-99ea-b2a9291d3eb7" />
<img width="3129" height="1053" alt="image" src="https://github.com/user-attachments/assets/7f61fc67-f4f3-4f10-9ff3-3aa2b11bc3bb" />

