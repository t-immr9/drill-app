import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="数学ドリル",
    page_icon="✕",
    layout="centered",
)

# タブで2つのアプリを切り替え
tab1, tab2 = st.tabs(["✕ かけ算ドリル", "　因数ドリル"])

with tab1:
    components.html(
        open("multiplication_drill.html", encoding="utf-8").read(),
        height=820,
        scrolling=False,
    )

with tab2:
    components.html(
        open("factorization_drill.html", encoding="utf-8").read(),
        height=820,
        scrolling=False,
    )
