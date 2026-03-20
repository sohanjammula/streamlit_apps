import streamlit as st

# Page Config
st.set_page_config(page_title="Interest Calculator", page_icon="💰", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>💰 Interest Calculator</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
st.subheader("📥 Enter Details")

col1, col2, col3 = st.columns(3)

with col1:
    principal = st.number_input("Principal (₹)", min_value=0.0, step=100.0)

with col2:
    rate = st.number_input("Rate (%)", min_value=0.0, step=0.1)

with col3:
    time = st.number_input("Time (Years)", min_value=0.0, step=0.5)

st.markdown("---")

# Functions
def calculate_simple_interest(p, r, t):
    si = (p * r * t) / 100
    total = p + si
    return si, total

def calculate_compound_interest(p, r, t):
    total = p * (1 + r / 100) ** t
    ci = total - p
    return ci, total

# Tabs for better UX
tab1, tab2 = st.tabs(["📊 Simple Interest", "📈 Compound Interest"])

# Simple Interest Tab
with tab1:
    if st.button("Calculate SI"):
        if principal > 0 and rate > 0 and time > 0:
            si, total = calculate_simple_interest(principal, rate, time)

            st.success(f"💵 Simple Interest: ₹{si:,.2f}")
            st.info(f"📦 Total Amount: ₹{total:,.2f}")
        else:
            st.error("⚠️ Please enter valid values.")

# Compound Interest Tab
with tab2:
    if st.button("Calculate CI"):
        if principal > 0 and rate > 0 and time > 0:
            ci, total = calculate_compound_interest(principal, rate, time)

            st.success(f"💰 Compound Interest: ₹{ci:,.2f}")
            st.info(f"📦 Total Amount: ₹{total:,.2f}")
        else:
            st.error("⚠️ Please enter valid values.")