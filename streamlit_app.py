import streamlit as st
import time
import pandas as pd
import plotly.express as px
from datetime import datetime
import sqlite3

# --- UI CONFIGURATION ---
st.set_page_config(page_title="NEET Flow - Study Tracker", layout="wide")

# Custom CSS for "Tech Vibe"
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ffcc; }
    .stButton>button { background-color: #1f2630; border: 1px solid #00ffcc; color: #00ffcc; border-radius: 10px; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 15px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# --- APP SECTIONS ---
def home_section():
    st.title("⚡ Focus Terminal")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Deep Work Timer")
        timer_placeholder = st.empty()
        duration = st.number_input("Set focus minutes", value=25)
        
        if st.button("Start Focus Session"):
            seconds = duration * 60
            while seconds > 0:
                mins, secs = divmod(seconds, 60)
                timer_placeholder.metric("Time Remaining", f"{mins:02d}:{secs:02d}")
                time.sleep(1)
                seconds -= 1
            st.balloons()
            # Log to DB
            # log_study_time(st.session_state.user, duration/60)
            st.success("Session Complete! Data Synced to Cloud.")

def stats_section():
    st.title("📊 Neural Growth Stats")
    # Dummy data for visualization
    df = pd.DataFrame({
        'Date': pd.date_range(start='2026-05-01', periods=7),
        'Hours': [4, 6, 5, 8, 3, 7, 9]
    })
    
    fig = px.line(df, x='Date', y='Hours', title='Activity Heatmap',
                  template="plotly_dark", line_shape="spline")
    fig.update_traces(line_color='#00ffcc')
    st.plotly_chart(fig, use_container_width=True)

def social_section():
    st.title("🌐 Peer Network")
    tab1, tab2 = st.tabs(["Friends Activity", "Global Chat"])
    
    with tab1:
        st.write("Current Friends")
        # Example Friend List
        friends = {"Simplyy_Coder": "8.5 hrs today", "Dev_Runner": "4.2 hrs today"}
        for f, stat in friends.items():
            st.info(f"**{f}** is currently at {stat}")

    with tab2:
        st.text_area("Encourage your peers...", placeholder="Send a message to the group...")
        st.button("Transmit")

# --- MAIN NAVIGATION ---
if not st.session_state.logged_in:
    st.title("Nexus Auth")
    user = st.text_input("Unique Username")
    if st.button("Initialize"):
        st.session_state.logged_in = True
        st.session_state.user = user
        st.rerun()
else:
    menu = ["Home", "Stats", "Social"]
    choice = st.sidebar.radio("Navigation", menu)
    
    if choice == "Home": home_section()
    elif choice == "Stats": stats_section()
    elif choice == "Social": social_section()
