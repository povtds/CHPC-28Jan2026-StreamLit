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

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# YOUR EXACT SPECIFICATIONS - Page config at the top (must be first!)
st.set_page_config(
    page_title="TDS | AtroPhysics, NWU", 
    page_icon="∀",  # Your universal quantifier symbol
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("∀ Navigation")
page = st.sidebar.radio("Select Page:", [
    "🏠 Home", 
    "🔬 Research", 
    "📊 Data", 
    "📚 Publications", 
    "✉️ Contact"
])

# === HOME ===
if page == "🏠 Home":
    st.markdown("# TDS | AtroPhysics, NWU")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Institution", "NWU Potchefstroom")
    with col2: st.metric("Field", "AtroPhysics ⚛️")
    with col3: st.metric("Location", "North West, ZA")
    
    st.write("""
    **Graduate researcher** specializing in nuclear physics, cosmic-ray neutron sensing, 
    and astrophysical phenomena. Currently working on soil moisture applications and 
    nuclear reaction energetics at North-West University.
    """)

# === RESEARCH ===
elif page == "🔬 Research":
    st.markdown("# Research Areas")
    
    tab1, tab2, tab3 = st.tabs(["Nuclear Physics", "Cosmic Rays", "Astrophysics"])
    
    with tab1:
        st.latex(r"Q = (m_i - m_f) \times 931.494 \, \text{MeV/u}")
        m_i = st.number_input("Initial mass (u)", 12.0)
        m_f = st.number_input("Final mass (u)", 11.9)
        Q = (m_i - m_f) * 931.494
        st.success(f"**Q-value: {Q:.2f} MeV**")
    
    with tab2:
        st.write("Cosmic-ray neutron sensing for soil moisture measurement")
    
    with tab3:
        st.write("Gamma-ray bursts, neutron star mergers, nucleosynthesis")

# === DATA ===
elif page == "📊 Data":
    nuclear_data = pd.DataFrame({
        "Reaction": ["¹²C(α,n)", "¹⁴N(p,γ)", "⁵⁶Fe(p,γ)", "²³⁸U(α,f)"],
        "Q_MeV": [1.19, 7.29, -0.84, 45.5]
    })
    
    st.dataframe(nuclear_data)
    fig = px.bar(nuclear_data, x="Reaction", y="Q_MeV", title="Q-values")
    st.plotly_chart(fig)

# === PUBLICATIONS ===
elif page == "📚 Publications":
    st.markdown("# Publications")
    pubs = pd.DataFrame({
        "Title": ["Cosmic Neutron Soil Moisture", "Nuclear Q-values", "LaTeX Reports"],
        "Status": ["In Prep", "Submitted", "Complete"],
        "Year": [2026, 2025, 2025]
    })
    st.dataframe(pubs)

# === CONTACT ===
elif page == "✉️ Contact":
    st.markdown("# Contact")
    st.info("**TDS** | NWU Nuclear Physics | Potchefstroom, ZA")

# Footer
st.markdown("---")
st.markdown("*CHPC Coding Summer School | Jan 28, 2026*")
