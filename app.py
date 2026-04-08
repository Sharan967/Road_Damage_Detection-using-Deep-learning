import streamlit as st
import streamlit.components.v1 as components
try:
    import cv2
except ImportError:
    import os
    os.system("pip install opencv-python-headless")
    import cv2
from ultralytics import YOLO
from PIL import Image
import time, io, datetime, sqlite3
from sklearn.linear_model import LinearRegression
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# =====================================================
# APP CONFIG
# =====================================================
st.set_page_config(
    page_title="Road Damage Detection System",
    layout="wide",
    page_icon="🛣️",
)
# =====================================================
# SESSION INIT (WELCOME VOICE)
# =====================================================
if "welcome_done" not in st.session_state:
    st.session_state.welcome_done = False

# =====================================================
# DYNAMIC ACCENT COLOR (TIME BASED)
# =====================================================
hour = datetime.datetime.now().hour
if hour < 12:
    accent = "#FF0004"
elif hour < 18:
    accent = "#46C800"
elif hour < 22:
    accent = "#FF9100"
else:
    accent = "#7C4DFF"

# =====================================================
# GLOBAL FUTURISTIC UI (PRO LEVEL)
# =====================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;500;700&display=swap');

html, body, .stApp {{
    background: radial-gradient(circle at top, #050816, #000);
    color: #eaf6ff;
    font-family: 'Inter', sans-serif;
}}

::-webkit-scrollbar {{
    width: 6px;
}}
::-webkit-scrollbar-thumb {{
    background: {accent};
    border-radius: 10px;
}}

.xr-intro {{
    position: fixed;
    inset: 0;
    background: radial-gradient(circle, #000, #020616);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeOut 3s forwards;
}}

@keyframes fadeOut {{
    0% {{opacity:1}}
    85% {{opacity:1}}
    100% {{opacity:0; visibility:hidden}}
}}

.logo {{
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, {accent}, #020616);
    box-shadow: 0 0 60px {accent};
    animation: spin 6s linear infinite;
}}

@keyframes spin {{
    from {{transform: rotate(0deg)}}
    to {{transform: rotate(360deg)}}
}}

.title {{
    font-family: 'Orbitron', sans-serif;
    font-size: 48px;
    font-weight: 900;
    letter-spacing: 2px;
    background: linear-gradient(90deg, {accent}, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.section {{
    background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
    border: 1px solid rgba(255,255,255,0.15);
    border-left: 6px solid {accent};
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 16px;
    box-shadow: 0 0 30px rgba(0,0,0,0.6);
}}

.hud {{
    position: fixed;
    inset: 0;
    pointer-events: none;
}}

.hud:after {{
    content: "";
    position: absolute;
    inset: 20px;
    border: 1px dashed rgba(255,255,255,0.15);
    border-radius: 20px;
}}

.particles {{
    position: fixed;
    inset: 0;
    pointer-events: none;
}}

.p {{
    position: absolute;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: rgba(0,255,255,0.12);
    animation: float 22s linear infinite;
}}

@keyframes float {{
    from {{transform: translateY(120vh)}}
    to {{transform: translateY(-20vh)}}
}}
</style>

<div class="xr-intro">
    <div style="text-align:center">
        <div class="logo"></div>
        <h1 class="title">XR ROAD INTELLIGENCE</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# PARTICLES
# =====================================================
components.html(
    "<div class='particles'>" +
    "".join(f"<div class='p' style='left:{i*12}%;animation-duration:{18+i}s'></div>" for i in range(8)) +
    "</div>",
    height=0
)
# =====================================================
# WELCOME VOICE (JARVIS STYLE)
# =====================================================
if not st.session_state.welcome_done:
    components.html("""
    <script>
    speechSynthesis.speak(new SpeechSynthesisUtterance(
    "Welcome to X R Road Intelligence System. Artificial intelligence powered road damage detection, severity analysis, repair recommendation and cost estimation module initialized."
    ));
    </script>
    """, height=0)
    st.session_state.welcome_done = True

# =====================================================
# LIVE GPS
# =====================================================
loc = components.html("""
<script>
navigator.geolocation.getCurrentPosition(
  pos => Streamlit.setComponentValue({lat:pos.coords.latitude, lon:pos.coords.longitude}),
  () => Streamlit.setComponentValue({lat:null, lon:null})
);
</script>
""", height=0)

lat, lon = None, None
if isinstance(loc, dict):
    lat, lon = loc.get("lat"), loc.get("lon")

# =====================================================
# DATABASE
# =====================================================
conn = sqlite3.connect("damage_logs.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS logs (
 time TEXT, lat REAL, lon REAL,
 damage TEXT, conf REAL, severity TEXT, cost REAL
)
""")
conn.commit()

# =====================================================
# SAFE YOLO MODEL LOADER (STREAMLIT CLOUD READY)
# =====================================================
import os

@st.cache_resource(show_spinner="🔄 Loading AI model...")
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "best.pt")

    if not os.path.exists(model_path):
        st.error("❌ YOLO model file not found in root directory!")
        st.stop()

    return YOLO(model_path)

model = load_model()


# =====================================================
# COST MODEL
# =====================================================
X = np.array([[1000],[5000],[15000],[40000],[80000]])
y = np.array([2000,4000,8000,15000,30000])
cost_model = LinearRegression().fit(X,y)

def predict_cost(area):
    return int(cost_model.predict([[area]])[0])

# =====================================================
# HEATMAP
# =====================================================
def depth_heatmap(img, boxes):
    heat = np.zeros(img.shape[:2], dtype=np.uint8)
    for x1,y1,x2,y2 in boxes:
        cv2.rectangle(heat,(x1,y1),(x2,y2),255,-1)
    heat = cv2.GaussianBlur(heat,(51,51),0)
    heatmap = cv2.applyColorMap(heat, cv2.COLORMAP_JET)
    return cv2.addWeighted(img,0.85,heatmap,0.25,0)


# =====================================================
# ANALYSIS
# =====================================================
def analyze(img, conf):
    res = model.predict(img, conf=conf, save=False)
    boxes, dets = [], []
    for r in res:
        for b in r.boxes:
            x1,y1,x2,y2 = map(int,b.xyxy[0])
            area = (x2-x1)*(y2-y1)
            cost = predict_cost(area)
            sev = "Severe" if cost>20000 else "Moderate" if cost>8000 else "Minor"

            cv2.rectangle(img,(x1,y1),(x2,y2),(80,180,255),1)
            cv2.putText(img,f"{r.names[int(b.cls)]} | {sev}",
                        (x1,max(20,y1-10)),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,255),2)

            dets.append((r.names[int(b.cls)],b.conf.item(),sev,cost))
            boxes.append((x1,y1,x2,y2))

            cur.execute("INSERT INTO logs VALUES (?,?,?,?,?,?,?)",
                (datetime.datetime.now().isoformat(),lat,lon,
                 r.names[int(b.cls)],b.conf.item(),sev,cost))
            conn.commit()

    return depth_heatmap(img, boxes), dets

# =====================================================
# HEADER
# =====================================================
st.markdown("<div class='title'>Road Damage Detection System</div>", unsafe_allow_html=True)

if lat and lon:
    st.success(f"📍 Location Locked: {lat:.6f}, {lon:.6f}")
    st.map({"lat":[lat],"lon":[lon]})

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("⚙ Controls")
conf = st.sidebar.slider("Detection Confidence",0.1,1.0,0.25,0.05)
live = st.sidebar.toggle("Live Camera Mode")
holo = st.sidebar.toggle("Hologram Mode", True)
language = st.sidebar.selectbox(
    "🔊 Voice Language",
    ["English", "Hindi", "Telugu", "Tamil", "Kannada"]
)


# =====================================================
# INPUT
# =====================================================
img = None
if live:
    cam = st.camera_input("📷 Live Camera Feed")
    if cam:
        img = np.array(Image.open(cam))
else:
    f = st.file_uploader("📁 Upload Road Image For Analysis",["jpg","png"])
    if f:
        img = np.array(Image.open(f))

# =====================================================
# PROCESS
# =====================================================
if img is not None:

    st.markdown("<div class='hud'></div>", unsafe_allow_html=True)

    # ---------- ANALYSIS ----------
    out, dets = analyze(img.copy(), conf)

    # ---------- SEVERITY COUNT ----------
    severity_count = {"Minor": 0, "Moderate": 0, "Severe": 0}
    total_cost = 0

    for _, conf_score, sev, cost in dets:
        severity_count[sev] += 1
        total_cost += cost

    # ---------- DECISION ENGINE ----------
    if severity_count["Severe"] > 0:
        decision = "CRITICAL – Immediate Action Required"
        repair = "Full resurfacing or reconstruction recommended"
        voice_rate = 1.25
        voice_pitch = 1.2
    elif severity_count["Moderate"] >= 2:
        decision = "MAINTENANCE REQUIRED"
        repair = "Pothole patching and surface repair recommended"
        voice_rate = 1.05
        voice_pitch = 1.1
    else:
        decision = "MONITOR"
        repair = "Crack sealing and routine inspection recommended"
        voice_rate = 0.9
        voice_pitch = 1.0

    severity_text = ", ".join(
        f"{v} {k}" for k, v in severity_count.items() if v > 0
    )

    # ---------- VISUAL OUTPUT ----------
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='section'>Original Feed</div>", unsafe_allow_html=True)
        st.image(img, use_container_width=True)
    with c2:
        st.markdown("<div class='section'>Analyzed Output</div>", unsafe_allow_html=True)
        st.image(out, use_container_width=True)

    # ---------- CONFIDENCE ----------
    st.markdown("<div class='section'>📊 Detection Confidence</div>", unsafe_allow_html=True)
    for name, conf_score, sev, _ in dets:
        st.progress(min(1.0, conf_score), text=f"{name} | {sev}")

    st.success(f"🧠 System Decision: {decision}")
    st.info(f"🛠 Recommended Repair: {repair}")
    st.success(f"💰 Total Estimated Repair Cost: ₹{total_cost}")

    # ---------- LANGUAGE MAP (CRITICAL FIX) ----------
    lang_map = {
        "English": "en-IN",
        "Hindi": "hi-IN",
        "Telugu": "te-IN",
        "Tamil": "ta-IN",
        "Kannada": "kn-IN"
    }

    voice_text_map = {
        "English":
            f"Analysis complete. Detected {severity_text}. "
            f"System decision is {decision}. "
            f"Recommended repair is {repair}. "
            f"Estimated repair cost is {total_cost} rupees.",

        "Hindi":
            f"विश्लेषण पूर्ण हुआ। {severity_text} क्षति पाई गई। "
            f"प्रणाली का निर्णय है {decision}। "
            f"अनुशंसित मरम्मत है {repair}। "
            f"अनुमानित लागत {total_cost} रुपये है।",

        "Telugu":
            f"విశ్లేషణ పూర్తైంది. {severity_text} నష్టాలు గుర్తించబడ్డాయి. "
            f"వ్యవస్థ నిర్ణయం {decision}. "
            f"సిఫార్సు చేసిన మరమ్మత్తు {repair}. "
            f"అంచనా వ్యయం {total_cost} రూపాయలు.",

        "Tamil":
            f"பகுப்பாய்வு முடிந்தது. {severity_text} சேதங்கள் கண்டறியப்பட்டுள்ளன. "
            f"அமைப்பின் முடிவு {decision}. "
            f"பரிந்துரைக்கப்பட்ட பழுது {repair}. "
            f"மதிப்பிடப்பட்ட செலவு {total_cost} ரூபாய்.",

        "Kannada":
            f"ವಿಶ್ಲೇಷಣೆ ಪೂರ್ಣಗೊಂಡಿದೆ. {severity_text} ಹಾನಿಗಳು ಪತ್ತೆಯಾಗಿದೆ. "
            f"ವ್ಯವಸ್ಥೆಯ ನಿರ್ಧಾರ {decision}. "
            f"ಶಿಫಾರಸು ಮಾಡಿದ ದುರಸ್ತಿ {repair}. "
            f"ಅಂದಾಜು ವೆಚ್ಚ {total_cost} ರೂಪಾಯಿ."
    }

    speech_text = voice_text_map.get(language, voice_text_map["English"])
    speech_lang = lang_map.get(language, "en-IN")

    # ---------- SPEAK (REAL FIX) ----------
    if "last_speech" not in st.session_state:
        st.session_state.last_speech = ""

    if st.session_state.last_speech != speech_text:
        st.session_state.last_speech = speech_text

        components.html(f"""
        <script>
            const utter = new SpeechSynthesisUtterance("{speech_text}");
            utter.lang = "{speech_lang}";
            utter.rate = {voice_rate};
            utter.pitch = {voice_pitch};
            speechSynthesis.cancel();
            speechSynthesis.speak(utter);
        </script>
        """, height=0)

    # ---------- PDF ----------
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [Paragraph("Road Damage Analysis Report", styles["Title"])]

    if lat and lon:
        story.append(Paragraph(f"Location: {lat:.6f}, {lon:.6f}", styles["Normal"]))

    img_buf = io.BytesIO()
    Image.fromarray(out).save(img_buf, format="PNG")
    img_buf.seek(0)
    story.append(RLImage(img_buf, 400, 300))

    for name, conf_score, sev, cost in dets:
        story.append(Paragraph(
            f"{name} – {sev} – Confidence {conf_score:.2f} – ₹{cost}",
            styles["Normal"]
        ))

    story.append(Paragraph(f"Final Decision: {decision}", styles["Normal"]))
    story.append(Paragraph(f"Recommended Repair: {repair}", styles["Normal"]))
    story.append(Paragraph(f"Total Estimated Cost: ₹{total_cost}", styles["Normal"]))

    doc.build(story)

    st.download_button(
        "📄 Download Analyzed Report",
        buf.getvalue(),
        "Road_Damage_Report.pdf",
        mime="application/pdf"
    )

