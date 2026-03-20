import streamlit as st

# Title
st.title(":red[Digital Calculator] 🖩")

# Initialize session state
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Utilities for safe evaluation
def _safe_eval(expr: str):
    try:
        # Restrict globals for safety
        value = eval(expr, {"__builtins__": None}, {})
        # Show integers without a .0
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return value
    except Exception:
        return None

# Function to update expression
# (Keeps display updated on every click and evaluates when an operator is entered)
def update_expression(value):
    expr = st.session_state.expression

    if value == "C":
        st.session_state.expression = ""
        st.session_state.result = ""
        return

    if value == "=":
        result = _safe_eval(expr)
        st.session_state.result = str(result) if result is not None else "Error"
        return

    # When an operator is pressed, evaluate the current expression first (if possible)
    if value in "+-*/":
        # allow starting with a negative number (e.g., "-5")
        if expr == "" and value == "-":
            st.session_state.expression = "-"
            st.session_state.result = ""
            return

        if expr and expr[-1] in "+-*/":
            # Replace the last operator if the user changed it
            st.session_state.expression = expr[:-1] + value
            return

        result = _safe_eval(expr)
        if result is not None:
            st.session_state.expression = f"{result}{value}"
            st.session_state.result = str(result)
        else:
            st.session_state.expression = expr + value
        return

    # Digit / decimal point pressed
    st.session_state.expression = expr + value
    st.session_state.result = ""

# Display placeholders (wrapped in a container to prevent layout shift)
display_container = st.container(border=True, height=100)
with display_container:
    expr_placeholder = st.empty()
    result_placeholder = st.empty()

# Create button layout
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("7", use_container_width=True):
        update_expression("7")
    if st.button("4", use_container_width=True):
        update_expression("4")
    if st.button("1", use_container_width=True):
        update_expression("1")
    if st.button("0", use_container_width=True):
        update_expression("0")

with col2:
    if st.button("8", use_container_width=True):
        update_expression("8")
    if st.button("5", use_container_width=True):
        update_expression("5")
    if st.button("2", use_container_width=True):
        update_expression("2")
    if st.button(".", use_container_width=True):
        update_expression(".")

with col3:
    if st.button("9", use_container_width=True):
        update_expression("9")
    if st.button("6", use_container_width=True):
        update_expression("6")
    if st.button("3", use_container_width=True):
        update_expression("3")
    if st.button("=", use_container_width=True):
        update_expression("=")

with col4:
    if st.button("/", use_container_width=True):
        update_expression("/")
    if st.button("*", use_container_width=True):
        update_expression("*")
    if st.button("-", use_container_width=True):
        update_expression("-")
    if st.button("+", use_container_width=True):
        update_expression("+")

with col5:
    st.write("")  # Spacer
    st.write("")  # Spacer
    st.write("")  # Spacer
    if st.button("Clear", use_container_width=True):
        update_expression("C")

# Update display after button handling (with fixed container to prevent shift)
expr_text = f"Expression: {st.session_state.expression}"
result_text = f"Result: {st.session_state.result}"
expr_placeholder.write(expr_text)
result_placeholder.write(result_text)
