# Researcher Profile With The Help Of: 
# http://localhost:8501/dataframe_demo & https://docs.streamlit.io/
# Deploy this single file to Streamlit Cloud for public sharing

"""
Wednesday - CHPC Coding SUmmer School (TimeTable on Canvas)
Date: 28th January 2026
Learning From: Binjamin Barsch, Lead Software Engineer (Chat on Slack)
    Time 12H12PM +
Follow-Up Done By: TDS (Astrophysics), NWU
"""

# TDS_Researcher_Profile.py - NO PLOTLY (uses native Streamlit charts)
import streamlit as st
import pandas as TDS
import numpy as np

st.set_page_config(
    page_title="TDS | AtroPhysics, NWU", 
    page_icon="(∀)", 
    layout="wide"
)

st.sidebar.title("Quantor (∀) Navigation")
page = st.sidebar.radio("Select Page:", ["🏠 Home", "🔬 Research", "📊 Data", "✉️ Contact"])

# The Home Field of The Website:
if page == "🏠 Home":
    st.title("TDS | Atro-Physics, NWU")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("NWU", "Potchefstroom")
    with col2: st.metric("Field", "AtroPhysics")
    with col3: st.metric("Location", "North West, ZA")

# The Research Field of The Website:
elif page == "🔬 Research":
    st.header("Q-Value Calculator")
    m_i = st.number_input("Initial mass (u)", 12.0)
    m_f = st.number_input("Final mass (u)", 11.9)
    Q = (m_i - m_f) * 931.494
    st.success(f"Q-value: **{Q:.2f} MeV**")

# The Data Field of The Website:
elif page == "📊 Data":
    data = pd.DataFrame({"Reaction": ["¹²C(α,n)", "¹⁴N(p,γ)"], "Q_MeV": [1.19, 7.29]})
    st.dataframe(data)
    st.bar_chart(data.set_index("Reaction")["Q_MeV"])
    #st.pie_chart(data.set_index("Reaction")["Q_MeV"])

# The Cnntact Field of The Website:
elif page == "✉️ Contact":
    st.info("TDS | Astro-Physics | NWU Potchefstroom")
    st.markdown("# 📧 Get In Touch")
    
    # Email input 
    email = st.text_input(
        "Your Email Address",
        placeholder="student@nwu.ac.za",
        help="I'll Reply Within 24 Hours, Unless I'm On Leave"
    )
    
    message = st.text_area(
        "Your Message",
        placeholder="Tell Me About Your Research Interests...",
        height=150
    )
    
    # Send Button/Prompt:
    if st.button("🚀 Send Message"):
        if email and message:
            st.success(f"✅ Message Sent From {email}!")
            st.balloons()  # Some Interactive Celebration!
        else:
            st.error("⚠️ Mandatory: Fill In Both Fields")


