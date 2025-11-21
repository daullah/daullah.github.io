import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# Page config
st.set_page_config(
    page_title="Amirudaullah - Data Analyst & QA Specialist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling (add your full CSS styles from original code here)
css = """
<style>
* {margin: 0; padding: 0;}
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}
/* Add additional CSS from your original styling here */
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Header Section (without purpose statement)
st.markdown("""
<div class="main-header">
    <h1>👨‍💼 Amirudaullah</h1>
    <p>💼 Data Analyst & Quality Assurance Specialist</p>
    <p>📍 Kolkata, India | 📞 (+91) 6268187329</p>
</div>
""", unsafe_allow_html=True)

# Contact Buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![Email](https://img.shields.io/badge/Email-amirudaullah@gmail.com-blue?style=for-the-badge&logo=gmail)](mailto:amirudaullah@gmail.com)")
with col2:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/amirud)")
with col3:
    st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/916268187329)")

# Resume Download Section with check
resume_path = "Amirudaullah_Resume.pdf"
if os.path.exists(resume_path):
    with open(resume_path, "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Amirudaullah_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
else:
    st.info("📄 Resume file not found. Please upload 'Amirudaullah_Resume.pdf' in the app directory.")

st.markdown("---")

# Professional Summary
st.markdown("<h2>📋 Professional Summary</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
<p>Data Analyst & Quality Assurance Specialist with <b>5+ years of experience</b> improving data accuracy and process efficiency through validation, automation, and visualization. Proficient in <b>Excel</b> with growing expertise in <b>SQL, Power BI, and Python</b> for analytical validation, data transformation, and reporting.</p>
<p>Collaborative and detail-oriented professional passionate about delivering actionable insights and continuous improvement in data-driven environments.</p>
</div>
""", unsafe_allow_html=True)

# Key Strengths
st.markdown("<h2>⭐ Key Strengths</h2>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="metric-box"><h3>✅</h3><p><b>Data Integrity</b></p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="metric-box"><h3>⚙️</h3><p><b>Process Optimization</b></p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="metric-box"><h3>💡</h3><p><b>Actionable Insights</b></p></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="metric-box"><h3>🤝</h3><p><b>Collaboration</b></p></div>""", unsafe_allow_html=True)

st.markdown("---")

# Current Role
st.markdown("<h2>🏢 Current Role</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
<h3>Order Management Analyst - British Telecom</h3>
<p><b>Apr 2022 – Present</b></p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="metric-box"><h3>98%</h3><p><b>Accuracy</b></p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="metric-box"><h3>15%↓</h3><p><b>Cycle Time</b></p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="metric-box"><h3>10%↓</h3><p><b>Cost Save</b></p></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="metric-box"><h3>5+ hrs↓</h3><p><b>Weekly Save</b></p></div>""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<ul style="color: #2a2a2a;">
<li>Performed QA and analytical validation on order-management datasets</li>
<li>Built SQL queries and Power BI dashboards to analyze trends and detect anomalies</li>
<li>Conducted root-cause analysis on order failures, contributing to 10% cost reduction</li>
<li>Automated QA checks and reporting pipelines, saving 5+ hours per week</li>
<li>Collaborated with cross-functional global teams to enhance data visibility</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Career Progression Section (Include full content from your original code)
st.markdown("---")
st.markdown("<h2>💼 Career Progression</h2>", unsafe_allow_html=True)
# Insert your career timeline content here 

# Project Portfolio Section (Include full content from your original code)
st.markdown("---")
st.markdown("<h2>📂 Project Portfolio</h2>", unsafe_allow_html=True)
# Insert your projects content here 

# Interactive Demo: Sales Dashboard
st.markdown("## 🎯 Demo: Interactive Sales Dashboard")
np.random.seed(0)
regions = ['North', 'South', 'East', 'West']
months = pd.date_range('2024-01-01', periods=12, freq='M').strftime('%b')
data = pd.DataFrame({
    'Month': np.tile(months, 4),
    'Region': np.repeat(regions, 12),
    'Sales': np.random.randint(100, 1000, size=48)
})

region = st.selectbox("Select Region", options=regions + ["All"])
show_trend = st.checkbox("Show Sales Trend Line", True)
month_range = st.slider("Show months", min_value=1, max_value=12, value=(1,12))

if region != "All":
    df = data[data['Region'] == region]
else:
    df = data

df = df.iloc[month_range[0]-1 : month_range[1]]

fig = px.bar(df, x='Month', y='Sales', title="Monthly Sales", color='Region' if region == "All" else None,
             color_discrete_sequence=px.colors.sequential.Blues)
if show_trend:
    fig.add_scatter(x=df['Month'], y=df['Sales'], mode='lines', name='Trend', line=dict(color='#764ba2', width=3))

st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Show sample data from demo project", False):
    st.write(df.head())

# Feedback Form
st.markdown("---")
st.markdown("### 🤝 Interested in Collaborating or Learning More?")

with st.form("interest_form"):
    user_name = st.text_input("Your Name")
    user_area = st.selectbox("What interests you most?", ["QA & Automation", "Data Analysis", "Dashboards", "Resume Review", "Other"])
    user_msg = st.text_area("Tell me what you'd like to see or discuss (optional)")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success(f"Thank you, {user_name or 'visitor'}! I'll get back to you about {user_area.lower()} soon.")

# Contact Section
st.markdown("""
<div class="contact-section">
    <h2>Let's Connect & Collaborate!</h2>
    <p>Ready to work on exciting data analytics and QA projects? Reach out now!</p>
    <div class="contact-links">
        <a href="mailto:amirudaullah@gmail.com" class="contact-link">📧 Email</a>
        <a href="https://wa.me/916268187329" class="contact-link">💬 WhatsApp</a>
        <a href="https://www.linkedin.com/in/amirud" class="contact-link">💼 LinkedIn</a>
    </div>
    <p style="margin-top: 20px;"><strong>📞 +91 6268187329 | 📍 Kolkata, India</strong></p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>")
st.markdown("<p style='text-align: center; color: white; opacity: 0.7; font-weight: 600;'>© 2024 Amirudaullah | Data Analyst & QA Specialist</p>", unsafe_allow_html=True)
