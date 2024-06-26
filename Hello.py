import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Nombre Grande",
    page_icon="👋",
)

st.write("# Welcome to the demo site of Elias Brovashov! 👋")

st.sidebar.success("Select a demo above.")

col1, col2 = st.columns(2)

with col1:
    st.image("static/images/photo.png", width=500)

with col2:
    st.markdown("**About me**")
    content = """
    Hi, my name is Elias! With extensive experience spanning 15 years  across IT, I emerge as a solutions-oriented professional in the areas of Cloud and AI. 
    My deep-rooted analytical insight aligns seamlessly with a goal-centric approach, ensuring adaptability and resilience during transformative projects. 
    Peers view me as a trusted consultant and solution architect, proficient in bridging gaps between stakeholders and translating visionary concepts into tangible solutions. 
    I pride myself on establishing ambitious benchmarks, steering projects with unwavering integrity, and exhibiting expertise in the Cloud, AI, and Cybersecurity.
"""
    st.info(content)



