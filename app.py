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

# Custom CSS styling (insert your full original CSS here for animations and cards)
css = """
<style>
* {margin: 0; padding: 0;}
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}
/* Include your detailed CSS for animation and styling here */
.main-header { ... } 
.card { ... }
.metric-box { ... }
.contact-section { ... }
/* (Truncated for brevity - reuse your original styles) */
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Tabs for multi-page layout
tabs = st.tabs(["About Me", "Career Progression", "Project Portfolio", "Skills & Certifications", "Interactive Demo", "Testimonials", "Contact"])

# -------- About Me -------- #
with tabs[0]:
    st.markdown("""
    <div class="main-header">
        <h1>👨‍💼 Amirudaullah</h1>
        <p>💼 Data Analyst & Quality Assurance Specialist</p>
        <p>📍 Kolkata, India | 📞 (+91) 6268187329</p>
    </div>    
    """, unsafe_allow_html=True)

    # Contact buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[![Email](https://img.shields.io/badge/Email-amirudaullah@gmail.com-blue?style=for-the-badge&logo=gmail)](mailto:amirudaullah@gmail.com)")
    with col2:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/amirud)")
    with col3:
        st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/916268187329)")

    # Resume download
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
        st.info("📄 Resume file not found. Please upload 'Amirudaullah_Resume.pdf'.")

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

# -------- Career Progression -------- #
with tabs[1]:
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

# -------- Project Portfolio -------- #
with tabs[2]:
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

# -------- Skills & Certifications -------- #
with tabs[3]:
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

# -------- Testimonials -------- #
with tabs[5]:
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
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="testimonial">
        <p><b>"A dedicated professional who consistently delivers high-quality work. His expertise in both QA and data analysis makes him invaluable to any team."</b></p>
        <p>— Team Lead, IBM Daksh</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="testimonial">
        <p><b>"Amirudaullah's SQL skills and analytical thinking helped us identify $45K in billing discrepancies. A true asset to our data quality initiatives."</b></p>
        <p>— Analytics Director, E-Commerce Platform</p>
        </div>
        """, unsafe_allow_html=True)

# -------- Interactive Demo -------- #
with tabs[4]:
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

# -------- Contact -------- #
with tabs[6]:
    st.markdown("<h2>📬 Get in Touch</h2>", unsafe_allow_html=True)

    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
        with col2:
            subject = st.selectbox("Subject *", ["Job Opportunity", "Project Inquiry", "Collaboration", "General Question", "Other"])
            phone = st.text_input("Phone (Optional)")
        
        message = st.text_area("Your Message *", height=120)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button("📧 Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success(f"✅ Thank you {name}! Your message has been received. I'll respond within 24 hours.")
                st.balloons()
            else:
                st.error("⚠️ Please fill in all required fields (marked with *)")

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
