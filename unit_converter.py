import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

st.title("🔁 Unit Converter")

# Choose category
category = st.selectbox("Select a category", ["Length", "Weight", "Temperature"])

# Define units for each category
units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value to convert", min_value=0.0)

result = None

# Conversion functions
def convert_length(val, from_u, to_u):
    factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return val * factors[from_u] / factors[to_u]

def convert_weight(val, from_u, to_u):
    factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return val * factors[from_u] / factors[to_u]

def convert_temperature(val, from_u, to_u):
    if from_u == to_u:
        return val
    if from_u == "Celsius":
        if to_u == "Fahrenheit":
            return (val * 9/5) + 32
        elif to_u == "Kelvin":
            return val + 273.15
    elif from_u == "Fahrenheit":
        if to_u == "Celsius":
            return (val - 32) * 5/9
        elif to_u == "Kelvin":
            return (val - 32) * 5/9 + 273.15
    elif from_u == "Kelvin":
        if to_u == "Celsius":
            return val - 273.15
        elif to_u == "Fahrenheit":
            return (val - 273.15) * 9/5 + 32

# Perform conversion
if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
