import streamlit as st

st.set_page_config(page_title="Personal Report Card", layout="centered")
st.title("📊 Personal Report Card")

# Subject marks input
st.subheader("Enter marks for 5 subjects (out of 100):")

subject_names = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
marks = []

for subject in subject_names:
    mark = st.number_input(f"{subject}", min_value=0, max_value=100, step=1, key=subject)
    marks.append(mark)

# Calculate total and percentage
total_marks = sum(marks)
max_marks = 500  # 5 subjects × 100 each
percentage = (total_marks / max_marks) * 100

# Determine grade
if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Display results
st.divider()
st.subheader("📈 Results:")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Marks", f"{total_marks}/500")
with col2:
    st.metric("Percentage", f"{percentage:.2f}%")
with col3:
    st.metric("Grade", grade)

# Display grade with colored message
st.divider()
if grade in ["A", "B"]:
    st.success(f"🎉 Excellent! You scored a Grade **{grade}**")
elif grade == "C":
    st.warning(f"⚠️ Good effort! You scored a Grade **{grade}**")
else:  # F
    st.error(f"❌ You scored a Grade **{grade}** - Need improvement!")

# Show balloons if percentage > 85%
if percentage > 85:
    st.balloons()
