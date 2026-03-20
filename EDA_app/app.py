import pandas as pd
import streamlit as st

st.title("Dataset story app")
st.subheader("upload your dataset and lets explore it")

col1,col2 = st.columns(2)

with col1 :
    st.markdown("### your journey")
    st.write("**Page 1** - upload your file")
    st.write("**Page 2** - Explore the data")
    st.write("**Page 3** - visualize the data")
    st.write("**Page 4** - Get insights")

with col2 :
    st.markdown("### files supported")
    st.write("csv or excel files only")
    st.write("any dataset you like")
    st.write("Titanic,sales,iris,..etc")
    st.write("even your own data")

st.divider()

upload_file = st.file_uploader("upload your file here", type = ["csv","xlsx"])

if upload_file is not None :
    if upload_file.name.endswith(".xlsx"):
        df = pd.read_excel(upload_file)
    else:
        df = pd.read_csv(upload_file)

    unnamed = [col for col in df.columns if "unnamed" in col]
    df.drop(unnamed,axis=1,inplace=True)

    #session state
    st.session_state['df'] = df
    st.session_state['filename'] = upload_file.name

if "df" in st.session_state:
    df = st.session_state['df']
    st.success(f"{st.session_state['filename']} is loaded successfully")

    st.subheader("Quick preview")
    col1,col2,col3 = st.columns(3)
    col1.metric("rows :",df.shape[0])
    col2.metric("columns :",df.shape[1])
    col3.metric("null values:",df.isna().sum().sum())
st.dataframe(df.head())

st.divider()

col1,col2 = st.columns(2)
with col2:
    st.page_link("pages/1_Data_exploration.py",label = "next data exploration",use_container_width=True)
