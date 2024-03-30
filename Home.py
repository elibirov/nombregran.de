import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Elias (Ilya) Brovashov")
    content = """
    Hi, my name is Elias! With extensive experience spanning 15 years  across IT, I emerge as a solutions-oriented professional in the areas of Cloud and AI. 
    My deep-rooted analytical insight aligns seamlessly with a goal-centric approach, ensuring adaptability and resilience during transformative projects. 
    Peers view me as a trusted consultant and solution architect, proficient in bridging gaps between stakeholders and translating visionary concepts into tangible solutions. 
    I pride myself on establishing ambitious benchmarks, steering projects with unwavering integrity, and exhibiting expertise in the Cloud, AI, and Cybersecurity.
"""
    st.info(content)

content2 = """
    Below you can see some examples of my apps that I have built with Python.
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
