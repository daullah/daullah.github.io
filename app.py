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
    st.markdown("""
    <div style="text-align: center; margin: 1.5rem 0;">
        <a href="https://your-cloud-storage-link-to-Amirudaullah_Resume.pdf" target="_blank" 
           style="display: inline-block; padding: 0.75rem 1.5rem; background-color: #4CAF50; 
                  color: white; text-decoration: none; border-radius: 8px; font-size: 1.1rem; font-weight: 600;">
            📄 Download Resume
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2>📋 Professional Summary</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <p>Data Analyst & Quality Assurance Specialist with <b>5+ years of experience</b> improving data accuracy and process efficiency through validation, automation, and visualization. Highly proficient in <b>Excel</b> and <b>Data QA</b>, with foundational knowledge and actively developing skills in <b>SQL, Power BI, and Python</b> for data analysis and reporting.</p>
    <p>A collaborative and detail-oriented professional passionate about delivering actionable insights and continuous improvement in data-driven environments.</p>
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
    <ul style="color: #f0f0f0;">
    <li>Executed QA validation and trend analysis on escalation data</li>
    <li>Achieved <b>90% resolution within SLA</b></li>
    <li>Streamlined processes and built Excel dashboards, reducing discrepancies by <b>30%</b></li>
    <li>Provided data-driven insights for service quality improvements</li>
    </ul>
    </div>
    <div class="org-item">
    <h3>Associate Engineer - Wipro</h3>
    <p><b>Mar 2016 – Oct 2016</b></p>
    <ul style="color: #f0f0f0;">
    <li>Validated telecom datasets and optimized testing workflows</li>
    <li>Achieved <b>95% first-contact resolution</b></li>
    <li>Enhanced data integrity through system audits and structured defect reporting</li>
    <li>Collaborated with cross-functional teams for process improvements</li>
    </ul>
    </div>
    <div class="org-item">
    <h3>Associate - Aegis Limited</h3>
    <p><b>May 2015 – Feb 2016</b></p>
    <ul style="color: #f0f0f0;">
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
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <div style="color: #f0f0f0;">
            <b>Overview:</b> Led comprehensive data validation for a healthcare analytics platform, ensuring high fidelity of patient records.
            
            <b>Key Achievements:</b>
            • Validated patient records across 50,000+ entries
            • Achieved 99.2% data accuracy rate
            • Improved diagnostic reporting accuracy by 15%
            • Used basic Python scripts for automated checks
            
            <b>Technologies:</b> Excel (Advanced), SQL (Basic Queries), Python (Scripting), Power BI (Developing)
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="metric-box"><h3>99.2%</h3><p><b>Accuracy</b></p></div>""", unsafe_allow_html=True)
            st.markdown("""<div class="metric-box"><h3>50K+</h3><p><b>Records</b></p></div>""", unsafe_allow_html=True)

    with st.expander("📊 Sales Performance Dashboard - QA & Validation"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <div style="color: #f0f0f0;">
            <b>Overview:</b> Assisted in designing and validating Power BI dashboards for sales analytics.
            
            <b>Key Achievements:</b>
            • Created QA test cases for 25+ KPIs
            • Achieved 95% test coverage for metrics
            • Contributed to a dashboard for 500+ users
            • Helped reduce monthly reporting time by 30%
            
            <b>Technologies:</b> Power BI (Developing), SQL (Basic Queries), DAX (Learning), Excel (Advanced)
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="metric-box"><h3>95%</h3><p><b>Coverage</b></p></div>""", unsafe_allow_html=True)
            st.markdown("""<div class="metric-box"><h3>500+</h3><p><b>Users</b></p></div>""", unsafe_allow_html=True)

    with st.expander("🛒 E-Commerce Data Analysis - Transaction Validation"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <div style="color: #f0f0f0;">
            <b>Overview:</b> Cleaned and validated e-commerce transaction data to ensure billing accuracy.
            
            <b>Key Achievements:</b>
            • Cleaned and standardized 100K+ transaction records
            • Identified and helped recover $45K in billing discrepancies
            • Improved overall data quality score by 25%
            • Built simple scripts for data monitoring
            
            <b>Technologies:</b> Excel (Advanced), SQL (Foundational), Python (Pandas - Learning)
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="metric-box"><h3>$45K</h3><p><b>Recovered</b></p></div>""", unsafe_allow_html=True)
            st.markdown("""<div class="metric-box"><h3>100K+</h3><p><b>Records</b></p></div>""", unsafe_allow_html=True)

    with st.expander("📈 Exploratory Data Analysis - Business Growth"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <div style="color: #f0f0f0;">
            <b>Overview:</b> Performed statistical analysis to validate business growth hypotheses.
            
            <b>Key Achievements:</b>
            • Analyzed over 500K data points from multiple sources
            • Validated 6 out of 8 growth hypotheses
            • Achieved a 95% confidence level in key findings
            • Presented findings in a clear, C-level report
            
            <b>Technologies:</b> Excel (Advanced), SQL (Learning), Statistical Analysis (Foundational)
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="metric-box"><h3>95%</h3><p><b>Confidence</b></p></div>""", unsafe_allow_html=True)
            st.markdown("""<div class="metric-box"><h3>500K+</h3><p><b>Data Points</b></p></div>""", unsafe_allow_html=True)

# -------- Skills & Certifications -------- #
with tabs[3]:
    st.markdown("<h2>📊 Technical Skills</h2>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Overview", "By Category", "Timeline"])

    with tab1:
        with st.spinner("Generating skill chart..."):
            skills_data = pd.DataFrame({
                'Skill': ['Excel', 'Data QA', 'ETL', 'SQL', 'Automation', 'Power BI', 'Tableau', 'Python'],
                'Proficiency': [90, 95, 80, 50, 75, 50, 45, 40] # Lowered SQL, Power BI, Python
            })
            fig = px.bar(skills_data.sort_values('Proficiency', ascending=True), x='Proficiency', y='Skill', 
                        orientation='h', color='Proficiency', color_continuous_scale='Viridis',
                        title='Technical Skills Proficiency (%)', text='Proficiency')
            fig.update_traces(texttemplate='%{text}%', textposition='outside')
            fig.update_layout(height=400, showlegend=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        with st.spinner("Generating category chart..."):
            category_data = pd.DataFrame({
                'Category': ['QA', 'Data Analysis', 'Automation', 'Visualization', 'Programming'],
                'Count': [4, 5, 3, 3, 2],
                'Proficiency': [88, 68, 75, 47, 40] # Adjusted to reflect lower skills
            })
            fig2 = go.Figure()
            fig2.add_trace(go.Bar(name='Skills Count', x=category_data['Category'], y=category_data['Count'], marker_color='rgba(173, 216, 230, 0.8)'))
            fig2.add_trace(go.Bar(name='Avg. Proficiency', x=category_data['Category'], y=category_data['Proficiency'], marker_color='rgba(65, 105, 225, 0.8)'))
            fig2.update_layout(title='Skills Distribution by Category', barmode='group', height=400, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white', legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
            st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        with st.spinner("Generating timeline chart..."):
            timeline_data = pd.DataFrame({
                'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
                'Excel': [40, 50, 60, 65, 70, 75, 80, 85, 88, 90],
                'SQL': [0, 0, 5, 10, 15, 20, 25, 30, 40, 50], # Slower growth
                'Power BI': [0, 0, 0, 5, 10, 15, 20, 30, 40, 50], # Slower growth
                'Python': [0, 0, 0, 0, 5, 10, 15, 20, 30, 40] # Slower growth
            })
            fig3 = go.Figure()
            for skill in ['Excel', 'SQL', 'Power BI', 'Python']:
                fig3.add_trace(go.Scatter(x=timeline_data['Year'], y=timeline_data[skill], mode='lines+markers', name=skill, line=dict(width=3), marker=dict(size=8)))
            fig3.update_layout(title='Skill Development Timeline', xaxis_title='Year', yaxis_title='Proficiency (%)', height=400, hovermode='x unified', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white', legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
            st.plotly_chart(fig3, use_container_width=True)

    st.markdown("<h2>🎓 Professional Certifications</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='badge'>✅ Project Management Foundation</div>", unsafe_allow_html=True)
        st.markdown("<div class='badge'>✅ Agile Methodologies</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='badge'>✅ Business Analytics Pro</div>", unsafe_allow_html=True)
        st.markdown("<div class='badge'>📚 Python for Analytics (In Progress)</div>", unsafe_allow_html=True) # Adjusted
    with col3:
        st.markdown("<div class='badge'>📚 SQL for Data Analysis (In Progress)</div>", unsafe_allow_html=True) # Adjusted
        st.markdown("<div class='badge'>📚 Power BI Visualization (In Progress)</div>", unsafe_allow_html=True) # Adjusted

# -------- Interactive Demo -------- #
with tabs[4]:
    st.markdown("## 🎯 Demo: Interactive Sales Dashboard")
    np.random.seed(42)
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

    with st.spinner("Generating sales chart..."):
        fig = px.bar(df, x='Month', y='Sales', title="Monthly Sales", color='Region' if region == "All" else None,
                    color_discrete_sequence=px.colors.sequential.Blues)
        if show_trend:
            fig.add_scatter(x=df['Month'], y=df['Sales'], mode='lines', name='Trend', line=dict(color='#fbbf24', width=3))
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig, use_container_width=True)

    if st.checkbox("Show sample data from demo project", False):
        st.write(df.head())

# -------- Articles & Insights (FIXED) -------- #
with tabs[5]:
    st.markdown("<h2>📝 Articles & Insights</h2>", unsafe_allow_html=True)
    st.markdown("A collection of my thoughts on data analytics, quality assurance, and industry trends.")

    with st.expander("Data Quality Best Practices in Healthcare Analytics"):
        st.markdown("""
        <div class="card">
        <p><b>Published on:</b> June 15, 2024 | <b>Platform:</b> Medium</p>
        <p>In this article, I discuss the critical importance of data quality in healthcare analytics. I cover topics such as data validation techniques, the impact of poor data on patient outcomes, and best practices for maintaining high data integrity standards...</p>
        <a href="https://your-blog-link.com/article1" target="_blank" style="color: #fbbf24; font-weight: bold;">Read More →</a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("How to Automate QA Checks with Python and Pandas"):
        st.markdown("""
        <div class="card">
        <p><b>Published on:</b> April 22, 2024 | <b>Platform:</b> Personal Blog</p>
        <p>This post provides a practical, step-by-step guide to automating repetitive Quality Assurance checks using Python's Pandas library. It includes code snippets for validating data types, checking for null values, and identifying outliers, saving analysts countless hours...</p>
        <a href="https://your-blog-link.com/article2" target="_blank" style="color: #fbbf24; font-weight: bold;">Read More →</a>
        </div>
        """, unsafe_allow_html=True)
        
# -------- Testimonials (FIXED) -------- #
with tabs[6]:
    st.markdown("<h2>💬 Testimonials</h2>", unsafe_allow_ht
