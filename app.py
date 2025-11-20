import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Amirudaullah - Data Analyst & QA Specialist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css = """
<style>
* {
    margin: 0;
    padding: 0;
}

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

[data-testid="stMainBlockContainer"] {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
}

.main-header {
    animation: slideDown 0.8s ease-out;
    text-align: center;
    padding: 30px 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 20px;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.main-header h1 {
    font-size: 3em;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.main-header p {
    font-size: 1.3em;
    opacity: 0.95;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}

.card {
    background: white;
    border-radius: 15px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    animation: fadeIn 0.6s ease-out;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 5px solid #667eea;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.3);
}

.metric-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    animation: fadeIn 0.8s ease-out;
    transition: transform 0.3s ease;
}

.metric-box:hover {
    transform: scale(1.05);
}

.metric-box h3 {
    font-size: 2em;
    margin: 10px 0;
}

.metric-box p {
    font-size: 0.9em;
    opacity: 0.9;
}

.org-timeline {
    border-left: 4px solid #667eea;
    padding-left: 20px;
    margin: 20px 0;
}

.org-item {
    margin: 20px 0;
    padding: 15px;
    background: #f8f9ff;
    border-radius: 10px;
    border-left: 4px solid #764ba2;
    animation: fadeIn 0.6s ease-out;
}

.org-item:hover {
    background: #f0f2ff;
    transform: translateX(5px);
    transition: all 0.3s ease;
}

.badge {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-size: 0.9em;
    animation: pulse 2s infinite;
}

.contact-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    margin-top: 40px;
    animation: fadeIn 1s ease-out;
}

.contact-links {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}

.contact-link {
    background: white;
    color: #667eea;
    padding: 15px 30px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
    transition: transform 0.3s ease;
}

.contact-link:hover {
    transform: scale(1.1);
}

.testimonial {
    background: linear-gradient(135deg, #f5f7ff 0%, #f0f2ff 100%);
    border-left: 5px solid #667eea;
    padding: 20px;
    border-radius: 10px;
    margin: 15px 0;
    animation: fadeIn 0.8s ease-out;
}

.testimonial:hover {
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
}

h2, h3 {
    color: #667eea;
    margin-top: 30px;
    animation: slideDown 0.6s ease-out;
}

@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2em;
    }
    
    .main-header p {
        font-size: 1em;
    }
    
    .metric-box {
        margin: 10px 0;
    }
    
    .contact-links {
        flex-direction: column;
    }
    
    .card {
        padding: 15px;
    }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>👨‍💼 Amirudaullah</h1>
    <p>Data Analyst & Quality Assurance Specialist</p>
    <p>📍 Kolkata, India | 📞 (+91) 6268187329</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![Email](https://img.shields.io/badge/Email-amirudaullah@gmail.com-blue?style=for-the-badge)](mailto:amirudaullah@gmail.com)")
with col2:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/amirud)")
with col3:
    st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/916268187329)")

try:
    with open("Amirudaullah_Resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Amirudaullah_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
except:
    st.info("📄 Resume available on request")

st.markdown("---")

st.markdown("<h2>📋 Professional Summary</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
Data Analyst & Quality Assurance Specialist with <b>5+ years of experience</b> improving data accuracy and process efficiency through validation, automation, and visualization. Proficient in <b>Excel</b> with growing expertise in <b>SQL, Power BI, and Python</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("<h2>⭐ Key Strengths</h2>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="metric-box"><h3>✅</h3><p>Data Integrity</p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="metric-box"><h3>⚙️</h3><p>Process Optimization</p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="metric-box"><h3>💡</h3><p>Insights</p></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="metric-box"><h3>🤝</h3><p>Collaboration</p></div>""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>🏢 Current Role</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
<h3>Order Management Analyst - British Telecom</h3>
<p><strong>Apr 2022 – Present</strong></p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="metric-box"><h3>98%</h3><p>Accuracy</p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="metric-box"><h3>15%↓</h3><p>Cycle Time</p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="metric-box"><h3>10%↓</h3><p>Cost</p></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="metric-box"><h3>5+ hrs↓</h3><p>Weekly</p></div>""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<ul>
<li>Performed QA and analytical validation on order-management datasets</li>
<li>Built SQL queries and Power BI dashboards to analyze trends</li>
<li>Conducted root-cause analysis on order failures</li>
<li>Automated QA checks and reporting pipelines</li>
<li>Collaborated with cross-functional global teams</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>💼 Career Progression</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="org-timeline">
<div class="org-item">
<h3>Senior Associate - IBM Daksh</h3>
<p><strong>Mar 2017 – Jan 2018</strong></p>
<ul>
<li>Executed QA validation and trend analysis on escalation data</li>
<li>Achieved <strong>90% resolution within SLA</strong></li>
<li>Built Excel dashboards reducing discrepancies by <strong>30%</strong></li>
<li>Provided data-driven insights for service quality improvements</li>
</ul>
</div>

<div class="org-item">
<h3>Associate Engineer - Wipro</h3>
<p><strong>Mar 2016 – Oct 2016</strong></p>
<ul>
<li>Validated telecom datasets and optimized testing workflows</li>
<li>Achieved <strong>95% first-contact resolution</strong></li>
<li>Enhanced data integrity through system audits</li>
<li>Collaborated with cross-functional teams</li>
</ul>
</div>

<div class="org-item">
<h3>Associate - Aegis Limited</h3>
<p><strong>May 2015 – Feb 2016</strong></p>
<ul>
<li>Conducted data validation and billing accuracy checks</li>
<li>Improved financial data quality by <strong>20%</strong></li>
<li>Ensured smooth customer resolutions with <strong>95% accuracy</strong></li>
<li>Created data quality reports</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>📂 Project Portfolio</h2>", unsafe_allow_html=True)

with st.expander("🏥 Healthcare Analytics - Patient Data Validation"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Overview:** Led data validation for healthcare analytics platform
        
        **Achievements:** 50K+ records validated, 99.2% accuracy, 15% improvement
        
        **Technologies:** Excel, SQL, Python, Power BI
        """)
    with col2:
        st.markdown("""<div class="metric-box"><h3>99.2%</h3><p>Accuracy</p></div>""", unsafe_allow_html=True)

with st.expander("📊 Sales Performance Dashboard - QA & Validation"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Overview:** Designed Power BI dashboards for sales analytics
        
        **Achievements:** 25+ KPIs validated, 95% test coverage, 500+ users
        
        **Technologies:** Power BI, SQL, DAX, Excel
        """)
    with col2:
        st.markdown("""<div class="metric-box"><h3>95%</h3><p>Coverage</p></div>""", unsafe_allow_html=True)

with st.expander("🛒 E-Commerce Data Analysis - Transaction Validation"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Overview:** Cleaned and analyzed e-commerce transaction data
        
        **Achievements:** 100K+ records, $45K discrepancies identified, 25% improvement
        
        **Technologies:** Python, SQL, Tableau
        """)
    with col2:
        st.markdown("""<div class="metric-box"><h3>96%</h3><p>Quality</p></div>""", unsafe_allow_html=True)

with st.expander("📈 Exploratory Data Analysis - Business Growth"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Overview:** Statistical analysis for business insights
        
        **Achievements:** 500K+ data points, 95% confidence, C-level reporting
        
        **Technologies:** Python, SQL, Excel
        """)
    with col2:
        st.markdown("""<div class="metric-box"><h3>95%</h3><p>Confidence</p></div>""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>📊 Technical Skills</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Overview", "By Category", "Timeline"])

with tab1:
    skills_data = pd.DataFrame({
        'Skill': ['Excel', 'Data QA', 'ETL', 'SQL', 'Automation', 'Power BI', 'Tableau', 'Python'],
        'Proficiency': [90, 95, 80, 70, 75, 65, 60, 55]
    })
    fig = px.bar(skills_data.sort_values('Proficiency', ascending=True), x='Proficiency', y='Skill', 
                 orientation='h', color='Proficiency', color_continuous_scale='Viridis',
                 title='Technical Skills (%)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    category_data = pd.DataFrame({
        'Category': ['QA', 'Data Analysis', 'Automation', 'Visualization', 'Programming'],
        'Count': [4, 5, 3, 3, 2],
        'Proficiency': [88, 78, 75, 62, 55]
    })
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name='Skills', x=category_data['Category'], y=category_data['Count'], marker_color='lightblue'))
    fig2.add_trace(go.Bar(name='Proficiency', x=category_data['Category'], y=category_data['Proficiency'], marker_color='darkblue'))
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    timeline_data = pd.DataFrame({
        'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        'Excel': [40, 50, 60, 65, 70, 75, 80, 85, 88, 90],
        'SQL': [0, 10, 20, 30, 40, 50, 55, 60, 65, 70],
        'Power BI': [0, 0, 0, 10, 20, 30, 40, 50, 60, 65],
        'Python': [0, 0, 0, 0, 10, 20, 30, 40, 50, 55]
    })
    fig3 = go.Figure()
    for skill in ['Excel', 'SQL', 'Power BI', 'Python']:
        fig3.add_trace(go.Scatter(x=timeline_data['Year'], y=timeline_data[skill], mode='lines+markers', name=skill))
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

st.markdown("<h2>🎓 Certifications</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='badge'>✅ Project Management</div>", unsafe_allow_html=True)
    st.markdown("<div class='badge'>✅ Agile</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='badge'>✅ Business Analytics</div>", unsafe_allow_html=True)
    st.markdown("<div class='badge'>✅ Python</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='badge'>✅ SQL</div>", unsafe_allow_html=True)
    st.markdown("<div class='badge'>✅ Power BI</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>💬 Testimonials</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="testimonial">
    <p><strong>"Exceptional attention to detail. QA scripts saved countless hours."</strong></p>
    <p>— British Telecom</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="testimonial">
    <p><strong>"Power BI dashboards helped critical business decisions."</strong></p>
    <p>— Healthcare Analytics</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="testimonial">
    <p><strong>"Dedicated professional, invaluable to any team."</strong></p>
    <p>— IBM Daksh</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="testimonial">
    <p><strong>"Identified $45K in billing discrepancies."</strong></p>
    <p>— E-Commerce Platform</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>📬 Get in Touch</h2>", unsafe_allow_html=True)

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name *")
        email = st.text_input("Email *")
    with col2:
        subject = st.selectbox("Subject *", ["Job", "Project", "Collaboration", "Question", "Other"])
        phone = st.text_input("Phone")
    
    message = st.text_area("Message *", height=100)
    submitted = st.form_submit_button("📧 Send", use_container_width=True)
    
    if submitted:
        if name and email and message:
            st.success(f"Thank you {name}! I'll respond within 24 hours.")
            st.balloons()
        else:
            st.error("Fill all required fields!")

st.markdown("---")

st.markdown("""
<div class="contact-section">
    <h2>Let's Connect!</h2>
    <div class="contact-links">
        <a href="mailto:amirudaullah@gmail.com" class="contact-link">📧 Email</a>
        <a href="https://wa.me/916268187329" class="contact-link">💬 WhatsApp</a>
        <a href="https://www.linkedin.com/in/amirud" class="contact-link">💼 LinkedIn</a>
    </div>
    <p style="margin-top: 20px;"><strong>📞 +91 6268187329 | 📍 Kolkata, India</strong></p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>")
st.markdown("<p style='text-align: center; color: white; opacity: 0.7;'>© 2024 Amirudaullah | Data Analyst & QA Specialist</p>", unsafe_allow_html=True)
