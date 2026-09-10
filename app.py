import sklearn
import sys
import joblib
import streamlit as st
import pandas as pd


st.write("Python version:", sys.version)
st.write("Scikit-learn version:", sklearn.__version__)

model_path = "accident_severity_pipeline.pkl"

loaded_model = joblib.load(model_path)

st.write("Model loaded successfully")
st.write(type(loaded_model))
# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Accident Severity Prediction",
    page_icon="🚗",
    layout="wide"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

/* ==========================
   Main App Background
========================== */

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
    color:white;
}

/* ==========================
   Header
========================== */

.main-title{
    text-align:center;
    font-size:46px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:#cbd5e1;
    margin-bottom:30px;
}

/* ==========================
   Sidebar
========================== */

[data-testid="stSidebar"]{
    background:#f8fafc;
}

[data-testid="stSidebar"] label{
    color:#0f172a !important;
    font-weight:600;
}

/* ==========================
   Cards
========================== */

.card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border-radius:20px;
    padding:25px;
    box-shadow:0px 4px 25px rgba(0,0,0,0.25);
    margin-bottom:20px;
}

/* ==========================
   Predict Button
========================== */

.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    font-size:22px;
    font-weight:bold;
    color:white;
    background:linear-gradient(
        135deg,
        #3b82f6,
        #06b6d4
    );
    transition:0.3s;
}

.stButton > button:hover{
    transform:scale(1.02);
}

/* ==========================
   Metrics Visibility Fix
========================== */

[data-testid="stMetricValue"]{
    color:white !important;
    font-size:34px !important;
    font-weight:bold !important;
}

[data-testid="stMetricLabel"]{
    color:#cbd5e1 !important;
    font-size:16px !important;
}

[data-testid="stMetricDelta"]{
    color:white !important;
}

/* ==========================
   Result Cards
========================== */

.success-card{
    background:linear-gradient(
        135deg,
        #166534,
        #22c55e
    );
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:28px;
    font-weight:bold;
    box-shadow:0px 0px 25px rgba(0,255,0,0.25);
    margin-bottom:25px;
}

.danger-card{
    background:linear-gradient(
        135deg,
        #991b1b,
        #ef4444
    );
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:28px;
    font-weight:bold;
    box-shadow:0px 0px 25px rgba(255,0,0,0.25);
    margin-bottom:25px;
}

/* ==========================
   Progress Bar
========================== */

.stProgress > div > div > div > div{
    background:#38bdf8;
}

/* ==========================
   Footer
========================== */

.footer{
    text-align:center;
    color:#cbd5e1;
    margin-top:50px;
    font-size:14px;
}

/* ==========================
   Info Boxes
========================== */

[data-testid="stInfo"]{
    border-radius:15px;
}

[data-testid="stSuccess"]{
    border-radius:15px;
}

[data-testid="stWarning"]{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Load Model
# ==========================================

model = joblib.load("accident_severity_pipeline.pkl")

# ==========================================
# Header
# ==========================================

st.markdown(
    "<div class='main-title'>🚗 Accident Severity Prediction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>AI-powered prediction of accident injury severity using Machine Learning</div>",
    unsafe_allow_html=True
)

st.write("")

# ==========================================
# Sidebar Inputs
# ==========================================

st.sidebar.header("Enter Accident Details")

person_age = st.sidebar.slider(
    "Person Age",
    1,
    100,
    30
)

person_type = st.sidebar.selectbox(
    "Person Type",
    ["Driver","Passenger","Pedestrian"]
)

person_sex = st.sidebar.selectbox(
    "Gender",
    ["M","F"]
)

ejection = st.sidebar.selectbox(
    "Ejection",
    ["Not Ejected","Partially Ejected","Ejected"]
)

safety_equipment = st.sidebar.selectbox(
    "Safety Equipment",
    ["Seat Belt","Helmet","None","Unknown"]
)

emotional_status = st.sidebar.selectbox(
    "Emotional Status",
    ["Conscious","Shock","Unknown"]
)

# ==========================================
# Main Layout
# ==========================================

col1, col2 = st.columns([1,1])

with col1:

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.subheader("📋 Input Summary")

    st.write(f"**Age:** {person_age}")
    st.write(f"**Person Type:** {person_type}")
    st.write(f"**Gender:** {person_sex}")
    st.write(f"**Ejection:** {ejection}")
    st.write(f"**Safety Equipment:** {safety_equipment}")
    st.write(f"**Emotional Status:** {emotional_status}")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.subheader("ℹ Project Information")

    st.write("""
    This application predicts the likelihood of a fatal accident injury
    using Machine Learning models trained on accident data.

    Features include:
    - Demographic details
    - Vehicle position
    - Safety equipment usage
    - Injury characteristics
    - Contributing accident factors
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# Prediction
# ==========================================

if st.button("🔍 Predict Severity"):

 input_df = pd.DataFrame({
     
         'CRASH_DATE':['01/01/2024'],
         'CRASH_TIME':['10:30'],
         'PERSON_TYPE':[person_type],
         'PERSON_AGE':[person_age],
         'EJECTION':[ejection],
         'EMOTIONAL_STATUS':[emotional_status],
         'BODILY_INJURY':['Unknown'],
         'POSITION_IN_VEHICLE':['Driver Seat'],
         'SAFETY_EQUIPMENT':[safety_equipment],
         'PED_LOCATION':['Unknown'],
         'PED_ACTION':['Unknown'],
         'COMPLAINT':['Pain'],
         'PED_ROLE':['None'],
         'CONTRIBUTING_FACTOR_1':['Driver Inattention'],
         'CONTRIBUTING_FACTOR_2':['Unspecified'],
         'PERSON_SEX':[person_sex]
         })
        
 prediction = model.predict(input_df)[0]

 probability = model.predict_proba(input_df)[0][1]

 st.markdown("<h2 style='color:white;'>📊 Prediction Result</h2>",
            unsafe_allow_html=True)

 if prediction==1 :

       st.markdown("""
        <div class='danger-card'>
        ⚠️ HIGH SEVERITY RISK DETECTED
        </div>
        """, unsafe_allow_html=True)
 else:

        st.markdown("""
            <div class='success-card'>
            ✅ LOW SEVERITY RISK DETECTED
            </div>
            """, unsafe_allow_html=True)

 c1,c2,c3 = st.columns(3)

 with c1:
     st.metric(
             "Fatal Injury Probability",
             f"{probability*100:.2f}%"
         )
     
 with c2:
     st.metric(
             "Non Fatal Probability",
             f"{(1-probability)*100:.2f}%"
         )

 with c3:
    st.metric(
        "Risk Level",
        "HIGH" if probability > 0.5 else "LOW"
    )

 st.write("")

 st.markdown("### 🎯 Risk Probability")

 st.progress(float(probability))

 

# ==========================================
# Footer
# ==========================================

st.markdown(
    """
    <div class='footer'>
    Developed using Streamlit • Scikit-Learn • Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)