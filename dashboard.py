import streamlit as st
import start_here
import beginners_guide
import trading_simulator
import support_center

st.set_page_config(layout="wide")

# WRAP PAGES
pages = [
    st.Page(
        page=lambda: start_here.run(),
        url_path="start_here",
        title="Start Here"
    ),
    st.Page(
        page=lambda: beginners_guide.run(),
        url_path="beginners_guide",
        title="Beginner's Guide"
    ),
    st.Page(
        page=lambda: trading_simulator.run(),
        url_path="trading_simulator",
        title="Trading Simulator"
    ),
    st.Page(
        page=lambda: support_center.run(),
        url_path="support_center",
        title="Support Center"
    ),
]

# RUN THE MULTI-PAGE APPLICATION
pg = st.navigation(pages)
pg.run()
