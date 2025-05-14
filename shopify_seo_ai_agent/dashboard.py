import streamlit as st
from pathlib import Path
import subprocess

st.title("Shopify SEO AI Agent Dashboard")

log_files = list(Path("logs").glob("*.log"))
if log_files:
    selected_log = st.selectbox("Select a log file", log_files)
    with open(selected_log, "r") as f:
        st.text(f.read())
else:
    st.warning("No logs found.")

if st.button("Run Agent Now"):
    st.success("Running agent manually...")
    subprocess.run(["python", "main.py"])