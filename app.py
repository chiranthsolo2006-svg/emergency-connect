import streamlit as st
import pandas as pd

st.set_page_config(page_title="Emergency Connect", layout="wide")

st.title("🚨 Emergency Connect System")

responders = {
    "Medical": ["Dr. Smith", "Nurse John"],
    "Fire": ["Fire Team A", "Fire Team B"],
    "Security": ["Security Team 1", "Security Team 2"]
}

if "alerts" not in st.session_state:
    st.session_state.alerts = []

st.sidebar.header("Report Emergency")

crisis_type = st.sidebar.selectbox(
    "Select Crisis Type",
    ["Medical", "Fire", "Security"]
)

location = st.sidebar.text_input("Enter Location (e.g., Room 203)")

assigned_responder = st.sidebar.selectbox(
    "Assign Responder",
    responders[crisis_type]
)

if st.sidebar.button("🚨 Send Alert"):
    alert = {
        "type": crisis_type,
        "location": location,
        "status": "Alert Sent",
        "responder": assigned_responder
    }

    st.session_state.alerts.append(alert)
    st.sidebar.success("Alert Sent Successfully!")

st.subheader("📊 Live Emergency Dashboard")

if len(st.session_state.alerts) == 0:
    st.info("No active emergencies")
else:
    df = pd.DataFrame(st.session_state.alerts)
    st.dataframe(df)

    for i, alert in enumerate(st.session_state.alerts):
        if alert["status"] == "Alert Sent":
            if st.button(f"Assign Case {i+1}"):
                st.session_state.alerts[i]["status"] = "Responder Assigned"

        elif alert["status"] == "Responder Assigned":
            if st.button(f"Mark 'On The Way' {i+1}"):
                st.session_state.alerts[i]["status"] = "On The Way"

        elif alert["status"] == "On The Way":
            if st.button(f"Resolve Case {i+1}"):
                st.session_state.alerts[i]["status"] = "Resolved"

st.markdown("---")
st.markdown("⚡ Hackathon Demo: Crisis Response System")
