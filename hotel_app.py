import streamlit as st
import random

st.set_page_config(page_title="Hotel Emergency System", layout="wide")

st.title("🏨 Hotel Emergency Response System")

# ---- Hotel Staff ----
responders = {
    "Fire": ["Fire Safety Team"],
    "Medical": ["Hotel Medic"],
    "Security": ["Hotel Security"]
}

if "alerts" not in st.session_state:
    st.session_state.alerts = []

# ---- Role ----
mode = st.sidebar.radio("Select Role", ["Guest", "Staff"])

# ================= GUEST =================
if mode == "Guest":
    st.header("🛎️ Guest Emergency Panel")

    room = st.text_input("📍 Enter Room Number (e.g., 203)")
    floor = st.selectbox("🏢 Select Floor", ["1", "2", "3", "4", "5"])

    st.subheader("🚨 Request Help")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔥 Fire"):
            st.session_state.alerts.append({
                "type": "Fire",
                "room": room,
                "floor": floor,
                "status": "Alert Sent",
                "responder": responders["Fire"][0]
            })

    with col2:
        if st.button("🏥 Medical"):
            st.session_state.alerts.append({
                "type": "Medical",
                "room": room,
                "floor": floor,
                "status": "Alert Sent",
                "responder": responders["Medical"][0]
            })

    with col3:
        if st.button("🛡️ Security"):
            st.session_state.alerts.append({
                "type": "Security",
                "room": room,
                "floor": floor,
                "status": "Alert Sent",
                "responder": responders["Security"][0]
            })

    st.subheader("📊 Your Requests")

    for i, alert in enumerate(st.session_state.alerts):
        st.write(f"### 🚨 Case {i+1}")
        st.write(f"Room: {alert['room']} | Floor: {alert['floor']}")
        st.write(f"Type: {alert['type']}")
        st.write(f"Status: {alert['status']}")
        st.divider()

# ================= STAFF =================
elif mode == "Staff":
    st.header("🧑‍💼 Hotel Staff Dashboard")

    if len(st.session_state.alerts) == 0:
        st.info("No active emergencies")
    else:
        for i, alert in enumerate(st.session_state.alerts):
            st.write(f"### 🚨 Case {i+1}")
            st.write(f"Room: {alert['room']} | Floor: {alert['floor']}")
            st.write(f"Type: {alert['type']}")
            st.write(f"Responder: {alert['responder']}")
            st.write(f"Status: {alert['status']}")

            col1, col2 = st.columns(2)

            if alert["status"] == "Alert Sent":
                if col1.button("🚑 Dispatch", key=f"a{i}"):
                    st.session_state.alerts[i]["status"] = "On The Way"

            elif alert["status"] == "On The Way":
                if col2.button("✅ Resolve", key=f"b{i}"):
                    st.session_state.alerts[i]["status"] = "Resolved"

            elif alert["status"] == "Resolved":
                st.success("Resolved")

            st.divider()
