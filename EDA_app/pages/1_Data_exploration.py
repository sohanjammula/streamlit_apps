import pandas as pd
import streamlit as st

st.title("Data Exploration")

if st.session_state.get("df") is None:
    st.warning("No Dataset please upload the dataset in the home page")
    st.page_link("app.py",label="Go to home page")
    st.stop()

df = st.session_state.df
st.subheader(f"Exploration on {st.session_state.filename}")
st.divider()

col1,col2,col3,col4 = st.columns(4)
col1.metric("rows :",df.shape[0])
col2.metric("columns :",df.shape[1])
col3.metric("null values:",df.isna().sum().sum())
col4.metric("duplicate values:",df.duplicated().sum())
st.divider()

tab1,tab2,tab3,tab4 = st.tabs(["Raw data","Statistics","Missing values","data types"])

with tab1:
    st.subheader("Raw data of the data uploaded")
    rows = st.slider("How many rows you want to use",max_value=len(df))
    st.dataframe(df.head(rows),use_container_width=True)

with tab2 :
    st.subheader("statistical summary")
    st.dataframe(df.describe(),use_container_width=True)

with tab3:
    st.subheader("Missing values per column")
    missing = df.isna().sum().sum()
    if missing:
        st.write(df.isna().sum())
    else:
        st.write("there are no missing values")

with tab4:
    st.subheader("datatypes of the data")
    st.write(df.dtypes)

st.divider()

col1,col2 = st.columns(2)
with col1:
    st.page_link("app.py",label="Go to homepage")
with col2:
    st.page_link("pages/2_visualization.py",label = "data visualization",use_container_width=True)