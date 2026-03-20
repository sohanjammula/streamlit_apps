import streamlit as st
from pint import UnitRegistry

# Initialize
ureg = UnitRegistry()

# Page Config
st.set_page_config(page_title="Universal Unit Converter", page_icon="🌍", layout="centered")

# Title
st.markdown("<h1 style='text-align:center;'>🌍 Universal Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("---")

# Categories
categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Mass": ["gram", "kilogram", "milligram", "pound", "ounce", "ton"],
    "Time": ["second", "minute", "hour", "day", "week", "year"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Volume": ["liter", "milliliter", "cubic_meter", "gallon"],
    "Area": ["square_meter", "square_kilometer", "acre", "hectare"],

    # ⚛️ Physics Units
    "Pressure": ["pascal", "kilopascal", "bar", "atm", "psi"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour"],
    "Power": ["watt", "kilowatt", "horsepower"],
    "Force": ["newton", "kilonewton"],
    "Frequency": ["hertz", "kilohertz", "megahertz"],

    # ⚡ Electrical Units (NEW 🔥)
    "Electric Current": ["ampere", "milliampere", "microampere"],
    "Voltage": ["volt", "millivolt", "kilovolt"],
    "Resistance": ["ohm", "kiloohm", "megaohm"],
    "Capacitance": ["farad", "millifarad", "microfarad", "nanofarad"],
    "Charge": ["coulomb", "millicoulomb"],
    "Conductance": ["siemens"],
}

# Select Category
category = st.selectbox("📂 Select Category", list(categories.keys()))

# Inputs
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Unit", categories[category])

with col2:
    to_unit = st.selectbox("To Unit", categories[category])

value = st.number_input("Enter Value", value=1.0)

st.markdown("---")

# Conversion Logic
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude
    except Exception:
        return None

# Auto Convert (no button needed)
result = convert_units(value, from_unit, to_unit)

# Output
if result is not None:
    st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
else:
    st.error("⚠️ Conversion not supported")

# Footer
st.markdown("---")
st.caption("🚀 Built with Streamlit + Pint | Ready for deployment")