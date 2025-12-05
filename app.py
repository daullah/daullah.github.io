import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Amirudaullah - Data Analyst & QA Specialist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- COMPLETE CSS WITH ANIMATIONS AND RESPONSIVENESS ---
css = """
<style>
/* General Reset & Body Styling */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 5px;
    gap: 5px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    background-color: transparent;
    color: rgba(255, 255, 255, 0.7);
}
.stTabs [aria-selected="true"] {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
}

/* Custom Components */
.main-header {
    text-align: center;
    padding: 2rem 1rem;
    margin-bottom: 2rem;
}
.main-header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}
.main-header p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.card {
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1.5rem 2rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.45);
}

.metric-box {
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    margin-bottom: 1rem;
    transition: transform 0.3s ease, background-color 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.2);
}
.metric-box:hover {
    transform: translateY(-5px);
    background-color: rgba(255, 255, 255, 0.25);
}
.metric-box h3 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.org-timeline {
    position: relative;
    padding-left: 2rem;
}
.org-item {
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1.5rem 2rem;
    margin-bottom: 1.5rem;
    border-left: 5px solid #fbbf24;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.testimonial {
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    font-style: italic;
    border-left: 5px solid #34d399;
}
.testimonial p:last-child {
    text-align: right;
    font-weight: bold;
    margin-top: 1rem;
    font-style: normal;
}

.badge {
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 0.5rem 1rem;
    margin-bottom: 0.5rem;
    display: inline-block;
    font-size: 0.9rem;
    border: 1px solid rgba(255, 255, 255, 0.3);
}

.contact-section {
    text-align: center;
    padding: 2rem;
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    margin-top: 2rem;
}
.contact-link {
    display: inline-block;
    margin: 0.5rem;
    padding: 0.75rem 1.5rem;
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    text-decoration: none;
    color: white;
    font-weight: 600;
    transition: background-color 0.3s ease, transform 0.3s ease;
}
.contact-link:hover {
    background-color: rgba(255, 255, 255, 0.3);
    transform: scale(1.05);
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2rem;
    }
    .stColumns > div {
        padding: 0.25rem;
    }
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Tabs for multi-page layout
tabs = st.tabs(["About Me", "Career Progression", "Project Portfolio", "Skills & Certifications", "Interactive Demo", "Articles & Insights", "Testimonials", "Contact"])
