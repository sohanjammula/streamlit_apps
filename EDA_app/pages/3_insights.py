import pandas as pd
import streamlit as st

st.title("Insights page")

if st.session_state.get("df") is None:
    st.warning("No Dataset please upload the dataset in the home page")
    st.page_link("app.py",label="Go to home page")
    st.stop
df = st.session_state.df

num_col = df.select_dtypes(include = "number").columns.tolist()

st.subheader(f"Auto-generation of insights for: {st.session_state.filename}")

st.markdown("### Data overview")

st.info(f"your dataset has {df.shape[0]} rows and {df.shape[1]} columns")

missing_values = df.isna().sum().sum()

if missing_values == 0:
    st.write("success your dataset does not have any missing values")
else:
    st.warning(f"OH NO! your dataset have {missing_values} missing values")
duplicated = df.duplicated().sum()
if duplicated == 0:
    st.write("success your dataset does not have any duplicate values")
else:
    st.warning(f"OH NO! your dataset have {duplicated} duplicate values")

st.divider()

if num_col:
    st.markdown('### Numarical Column Insights')
    for col in num_col:
        with st.expander(f'{col}'):
            col1, col2, col3, col4, = st.columns(4)
            col1.metric('Mean',f'{df[col].mean():.2f}')  
            col2.metric('Max',f'{df[col].max():.2f}')
            col3.metric('Min',f'{df[col].min():.2f}')  
            col4.metric('STD DEV',f'{df[col].std():.2f}')
            
            if df[col].std() > df[col].mean():
                st.warning(f"{col} has high variability of std dev")
            else:
                st.success(f"{col} looks stable and consistent")

st.success("We are successfully completed the summary of your dataset")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/2_Visualization.py",label="visualization")

with col2:
    st.page_link("app.py",label="home page",use_container_width=True)