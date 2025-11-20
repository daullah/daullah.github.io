import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Amirudaullah - Data Analyst & QA Specialist",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Amirudaullah")
st.subheader("Data Analyst & Quality Assurance Specialist | Kolkata, India")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('[📧 Email Me](mailto:amirudaullah@gmail.com)')
with col2:
    st.markdown('[💼 LinkedIn](https://www.linkedin.com/in/amirud)')
with col3:
    try:
        with open("Amirudaullah_Resume.pdf", "rb") as file:
            st.download_button(label="📄 Resume", data=file, file_name="Amirudaullah_Resume.pdf", mime="application/pdf")
    except:
        st.markdown('[📄 Resume](mailto:amirudaullah@gmail.com)')

st.markdown("---")
st.header("Professional Summary")
st.markdown("Data Analyst & QA Specialist with **5+ years experience**. Excel, SQL, Power BI, Python expertise.")

st.header("Core Competencies")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Data Validation & QA** - Ensuring accuracy\n**Data Analysis** - Power BI, Excel dashboards")
with col2:
    st.markdown("**SQL & Python** - Data transformation\n**Process Improvement** - Automation & optimization")

st.markdown("---")
st.header("Current Role: Order Management Analyst")
st.subheader("British Telecom | Apr 2022 – Present")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Accuracy", "98%")
with col2:
    st.metric("Speed", "15%↓")
with col3:
    st.metric("Cost Save", "10%↓")
with col4:
    st.metric("Hours/Week", "5+ hrs↓")

st.markdown("---")
st.header("Career Progression")

with st.expander("Order Management Analyst - BT (2022–Present)"):
    st.markdown("- QA validation on large datasets\n- SQL queries & Power BI dashboards\n- Process automation")

with st.expander("Senior Associate - IBM Daksh (2017–2018)"):
    st.markdown("- 90% SLA resolution\n- 30% reduction in discrepancies")

st.markdown("---")
st.header("Projects")

with st.expander("🏥 Healthcare Analytics"):
    st.metric("Accuracy", "99.2%")
    st.metric("Records", "50K+")

with st.expander("📊 Sales Dashboard QA"):
    st.metric("KPIs", "25+")
    st.metric("Coverage", "95%")

st.markdown("---")
st.header("Skills")

skills_data = pd.DataFrame({
    'Skill': ['Excel', 'SQL', 'Power BI', 'Python'],
    'Level': [90, 70, 65, 55]
})
fig = px.bar(skills_data, x='Level', y='Skill', orientation='h', color='Level', color_continuous_scale='Blues')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.header("Certifications")
st.markdown("✅ Project Management • ✅ Agile • ✅ Business Analytics • ✅ Python • ✅ SQL • ✅ Power BI")

st.markdown("---")
st.header("Testimonials")
col1, col2 = st.columns(2)
with col1:
    st.markdown('> "Exceptional attention to detail"\n— Senior Manager, British Telecom')
    st.markdown('> "Power BI dashboards were game-changing"\n— Product Owner, Healthcare')
with col2:
    st.markdown('> "Consistently high-quality work"\n— Team Lead, IBM Daksh')
    st.markdown('> "Identified $45K in discrepancies"\n— Analytics Director, E-Commerce')

st.markdown("---")
st.header("Blog & Insights")

tab1, tab2, tab3 = st.tabs(["Articles", "QA Tips", "Data Tips"])
with tab1:
    st.markdown("📝 5 SQL Queries Every Analyst Should Know")
    st.markdown("📊 Power BI Dashboard Best Practices")
with tab2:
    st.markdown("✅ When to Automate vs Manual Testing")
    st.markdown("🎯 Root Cause Analysis with Data")
with tab3:
    st.markdown("💡 Excel Power Tips for Analysts")
    st.markdown("📈 Data Cleaning 101")

st.markdown("---")
st.header("Contact Me")

with st.form("contact"):
    name = st.text_input("Name *")
    email = st.text_input("Email *")
    message = st.text_area("Message *")
    if st.form_submit_button("Send"):
        if name and email and message:
            st.success("Message received! I'll respond soon.")
        else:
            st.error("Please fill all fields")

st.markdown("---")
st.header("Let's Connect")
st.markdown("**📍 Kolkata, India | 📞 +91 6268187329**")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[📧 Email](mailto:amirudaullah@gmail.com)")
with col2:
    st.markdown("[💬 WhatsApp](https://wa.me/916268187329)")
with col3:
    st.markdown("[💼 LinkedIn](https://linkedin.com/in/amirud)")