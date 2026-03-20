import streamlit as st

st.title("💪 Advanced BMI Calculator")

# Sidebar
st.sidebar.header("Enter Your Details")

name = st.sidebar.text_input("Name")

# Height Unit Selection
height_unit = st.sidebar.radio("Select Height Unit", ["cm", "feet & inches"])

if height_unit == "cm":
    height_cm = st.sidebar.number_input("Height (cm)", min_value=50.0, max_value=250.0)
else:
    feet = st.sidebar.number_input("Feet", min_value=1, max_value=8)
    inches = st.sidebar.number_input("Inches", min_value=0, max_value=11)
    height_cm = (feet * 30.48) + (inches * 2.54)

# Weight Unit Selection
weight_unit = st.sidebar.radio("Select Weight Unit", ["kg", "pounds"])

if weight_unit == "kg":
    weight = st.sidebar.number_input("Weight (kg)", min_value=10.0, max_value=300.0)
else:
    pounds = st.sidebar.number_input("Weight (pounds)", min_value=20.0, max_value=600.0)
    weight = pounds * 0.453592  # convert to kg

# Button
if st.sidebar.button("Calculate BMI"):

    if height_cm > 0 and weight > 0:

        # BMI Calculation
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        st.subheader(f"Hello {name} 👋")
        st.write(f"Your BMI is: **{bmi:.2f}**")

        # Progress Bar
        progress_value = min(int(bmi * 2), 100)
        st.progress(progress_value)

        # Category Logic
        if bmi < 18.5:
            st.warning("⚠️ Underweight")
            st.write("You may need to gain some weight.")

        elif 18.5 <= bmi <= 24.9:
            st.success("✅ Normal Weight")
            st.write("Great job! Keep maintaining your health.")
            st.balloons()

        elif 25 <= bmi <= 29.9:
            st.warning("⚠️ Overweight")
            st.write("Consider a balanced diet and exercise.")

        else:
            st.error("❌ Obese")
            st.write("It's recommended to consult a healthcare provider.")

    else:
        st.error("Please enter valid values.")