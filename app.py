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
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.8; transform: scale(1.02); }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes shimmer {
    0% { background-position: -1000px 0; }
    100% { background-position: 1000px 0; }
}

@keyframes glow {
    0%, 100% { box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3); }
    50% { box-shadow: 0 8px 30px rgba(118, 75, 162, 0.5); }
}

@keyframes textGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.main-header {
    animation: slideDown 1s ease-out;
    text-align: center;
    padding: 50px 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 30px;
    margin-bottom: 50px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
    animation: shimmer 3s infinite;
}

.main-header h1 {
    font-size: 3.5em;
    margin-bottom: 10px;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    animation: float 3s ease-in-out infinite;
    position: relative;
    z-index: 1;
    font-weight: 900;
}

.main-header p {
    font-size: 1.2em;
    opacity: 0.98;
    position: relative;
    z-index: 1;
    margin: 8px 0;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 30px;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    animation: fadeInUp 0.8s ease-out both;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    border-left: 6px solid #667eea;
    color: #1a1a1a;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(102, 126, 234, 0.4);
    animation: glow 2s infinite;
}

.card p, .card ul, .card li {
    color: #2a2a2a;
}

.metric-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    animation: fadeInUp 0.8s ease-out both;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.metric-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    animation: shimmer 3s infinite;
}

.metric-box:hover {
    transform: scale(1.08) rotate(2deg);
    box-shadow: 0 15px 35px rgba(102, 126, 234, 0.5);
}

.metric-box h3 {
    font-size: 2.5em;
    margin: 10px 0;
    position: relative;
    z-index: 1;
    font-weight: 900;
}

.metric-box p {
    font-size: 0.95em;
    opacity: 0.95;
    position: relative;
    z-index: 1;
}

.org-timeline {
    border-left: 5px solid #667eea;
    padding-left: 25px;
    margin: 30px 0;
    position: relative;
}

.org-timeline::before {
    content: '';
    position: absolute;
    left: -8px;
    top: 0;
    width: 11px;
    height: 11px;
    background: #667eea;
    border-radius: 50%;
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
}

.org-item {
    margin: 25px 0;
    padding: 20px;
    background: white;
    border-radius: 15px;
    border-left: 5px solid #764ba2;
    animation: slideInLeft 0.8s ease-out both;
    transition: all 0.4s ease;
    color: #1a1a1a;
}

.org-item:hover {
    background: linear-gradient(135deg, #f8f9ff 0%, #f0f2ff 100%);
    transform: translateX(10px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.25);
}

.org-item h3, .org-item p {
    color: #1a1a1a;
}

.org-item ul li {
    color: #2a2a2a;
}

.badge {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 10px 20px;
    border-radius: 25px;
    margin: 8px;
    font-size: 0.95em;
    animation: pulse 2s infinite;
    font-weight: 600;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    transition: all 0.3s ease;
}

.badge:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
}

.contact-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 50px;
    border-radius: 25px;
    text-align: center;
    margin-top: 50px;
    animation: fadeInUp 1s ease-out;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    position: relative;
    overflow: hidden;
}

.contact-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.1) 0%, transparent 100%);
}

.contact-section h2 {
    position: relative;
    z-index: 1;
    font-size: 2.5em;
    margin-bottom: 20px;
}

.contact-section p {
    position: relative;
    z-index: 1;
    font-size: 1.1em;
}

.contact-links {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 30px;
    position: relative;
    z-index: 1;
}

.contact-link {
    background: white;
    color: #667eea;
    padding: 15px 35px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    display: inline-block;
}

.contact-link:hover {
    transform: scale(1.12) translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    background: #f0f2ff;
}

.testimonial {
    background: white;
    border-left: 6px solid #667eea;
    padding: 25px;
    border-radius: 15px;
    margin: 20px 0;
    animation: fadeInUp 0.8s ease-out both;
    transition: all 0.4s ease;
    color: #1a1a1a;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.testimonial:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.25);
    border-left-color: #764ba2;
}

.testimonial p {
    color: #2a2a2a;
}

h2, h3 {
    color: #667eea;
    margin-top: 40px;
    animation: slideDown 0.8s ease-out;
}

h2 {
    font-size: 2.2em;
    font-weight: 800;
    position: relative;
    padding-bottom: 15px;
}

h2::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 2px;
    animation: slideInLeft 0.8s ease-out;
}

.page-separator {
    margin: 50px 0;
}

@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2.2em;
    }
    
    .main-header p {
        font-size: 1em;
    }
    
    h2 {
        font-size: 1.8em;
    }
    
    .metric-box {
        margin: 15px 0;
    }
    
    .contact-links {
        flex-direction: column;
    }
    
    .card {
        padding: 20px;
    }
    
    .contact-section {
        padding: 30px;
    }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>👨‍💼 Amirudaullah</h1>
    <p>💼 Data Analyst & Quality Assurance Specialist</p>
    <p>📍 Kolkata, India | 📞 (+91) 6268187329</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![Email](https://img.shields.io/badge/Email-amirudaullah@gmail.com-blue?style=for-the-badge&logo=gmail)](mailto:amirudaullah@gmail.com)")
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
<p>Data Analyst & Quality Assurance Specialist with <b>5+ years of experience</b> improving data accuracy and process efficiency through validation, automation, and visualization. Proficient in <b>Excel</b> with growing expertise in <b>SQL, Power BI, and Python</b> for analytical validation, data transformation, and reporting.</p>
<p>Collaborative and detail-oriented professional passionate about delivering actionable insights and continuous improvement in data-driven environments.</p>
</div>
""", unsafe_allow_html=True)

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

st.markdown("---")

st.markdown("<h2>💼 Career Progression</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="org-timeline">
<div class="org-item">
<h3>Senior Associate - IBM Daksh</h3>
<p><b>Mar 2017 – Jan 2018</b></p>
<ul style="color: #2a2a2a;">
<li>Executed QA validation and trend analysis on escalation data</li>
<li>Achieved <b>90% resolution within SLA</b></li>
<li>Streamlined processes and built Excel dashboards, reducing discrepancies by <b>30%</b></li>
<li>Provided data-driven insights for service quality improvements</li>
</ul>
</div>

<div class="org-item">
<h3>Associate Engineer - Wipro</h3>
<p><b>Mar 2016 – Oct 2016</b></p>
<ul style="color: #2a2a2a;">
<li>Validated telecom datasets and optimized testing workflows</li>
<li>Achieved <b>95% first-contact resolution</b></li>
<li>Enhanced data integrity through system audits and structured defect reporting</li>
<li>Collaborated with cross-functional teams for process improvements</li>
</ul>
</div>

<div class="org-item">
<h3>Associate - Aegis Limited</h3>
<p><b>May 2015 – Feb 2016</b></p>
<ul style="color: #2a2a2a;">
<li>Conducted data validation and billing accuracy checks</li>
<li>Improved financial data quality by <b>20%</b></li>
<li>Ensured smooth customer resolutions with <b>95% accuracy</b></li>
<li>Created data quality reports and identified improvement areas</li>
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
        <div style="color: #1a1a1a;">
        <b>Overview:</b> Led comprehensive data validation for healthcare analytics platform
        
        <b>Key Achievements:</b>
        • Validated patient records across 50,000+ entries
        • Achieved 99.2% data accuracy rate
        • Improved diagnostic reporting accuracy by 15%
        • Implemented automated QA checks
        
        <b>Technologies:</b> Excel, SQL, Python, Power BI
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-box"><h3>99.2%</h3><p><b>Accuracy</b></p></div>""", unsafe_allow_html=True)

with st.expander("📊 Sales Performance Dashboard - QA & Validation"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style="color: #1a1a1a;">
        <b>Overview:</b> Designed and validated Power BI dashboards for sales analytics
        
        <b>Key Achievements:</b>
        • Created QA scripts for 25+ KPIs
        • Achieved 95% test coverage
        • Delivered bug-free dashboard to 500+ users
        • Reduced reporting time by 30%
        
        <b>Technologies:</b> Power BI, SQL, DAX, Excel
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-box"><h3>95%</h3><p><b>Coverage</b></p></div>""", unsafe_allow_html=True)

with st.expander("🛒 E-Commerce Data Analysis - Transaction Validation"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style="color: #1a1a1a;">
        <b>Overview:</b> Cleaned and analyzed e-commerce transaction data
        
        <b>Key Achievements:</b>
        • Cleaned and standardized 100K+ records
        • Identified $45K in billing discrepancies
        • Improved data quality by 25%
        • Automated quality monitoring
        
        <b>Technologies:</b> Python, SQL, Tableau
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-box"><h3>96%</h3><p><b>Quality</b></p></div>""", unsafe_allow_html=True)

with st.expander("📈 Exploratory Data Analysis - Business Growth"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style="color: #1a1a1a;">
        <b>Overview:</b> Statistical analysis for business insights
        
        <b>Key Achievements:</b>
        • Analyzed 500K+ data points
        • Validated 6 out of 8 growth hypotheses
        • Achieved 95% confidence level
        • Delivered C-level reporting
        
        <b>Technologies:</b> Python, SQL, Excel, Statistical Analysis
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-box"><h3>95%</h3><p><b>Confidence</b></p></div>""", unsafe_allow_html=True)

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
                 title='Technical Skills Proficiency (%)', text='Proficiency')
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(height=400, showlegend=False)
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
    fig2.update_layout(title='Skills Distribution by Category', barmode='group', height=400)
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
        fig3.add_trace(go.Scatter(x=timeline_data['Year'], y=timeline_data[skill], mode='lines+markers', name=skill, line=dict(width=3), marker=dict(size=8)))
    fig3.update_layout(title='Skill Development Timeline', xaxis_title='Year', yaxis_title='Proficiency (%)', height=400, hovermode='x unified')
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

st.markdown("<h2>🎓 Professional Certifications</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='badge'>✅ Project Management Foundation</div>", unsafe_allow_html=True)
    st.markdown("<div class='badge'>✅ Agile Methodologies</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='badge'>✅ Business Analytics Pro</div>", unsafe_allow_html=True)
    st.markdown("<div class='badge'>✅ Python for Analytics</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='badge'>✅ SQL for Data Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='badge'>✅ Power BI Visualization</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2>💬 Testimonials</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="testimonial">
    <p><b>"Exceptional attention to detail in data validation. Automated QA scripts saved our team countless hours and significantly improved our data accuracy."</b></p>
    <p>— Senior Manager, British Telecom</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="testimonial">
    <p><b>"His Power BI dashboards provided clear insights that helped us make critical business decisions. Highly recommend for any data analytics project."</b></p>
    <p>— Product Owner, Healthcare Analytics</p>
    </div>
    """, unsafe_allow_html=Tr
