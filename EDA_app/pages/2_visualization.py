import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("data visualization")

if st.session_state.get("df") is None:
    st.warning("No Dataset please upload the dataset in the home page")
    st.page_link("app.py",label="Go to home page")
    st.stop
df = st.session_state.df

num_cols = df.select_dtypes(include = "number").columns.tolist()

cat_cols = df.select_dtypes(include = "object").columns.tolist()

st.subheader("Choose your chart and columns")

st.divider()

chart_type = st.selectbox("Select Chart Type",["Bar Chart","Line Chart","Scatter Plot","Histogram"])

if chart_type == "Bar Chart":

    st.subheader("Bar Chart")

    if cat_cols:

        col = st.selectbox("Select Categorical column (x-axis)",cat_cols)

        val = st.selectbox("Select numerical column (Y-axis)",num_cols)

        chart_data = df.groupby(col)[val].mean().reset_index()

        st.bar_chart(chart_data.set_index(col))

    else:

        st.warning("No Catergorical column found")

elif chart_type == "Line Chart":

    st.subheader("Line Chart")

    col = st.selectbox("Select numerical column",num_cols)

    st.line_chart(df[col])

elif chart_type == "Scatter Plot":

    st.subheader("Scatter plot")

    x_col = st.selectbox("Select numerical column x-axis",num_cols,key="x")

    y_col = st.selectbox("Select numerical column y-axis",num_cols,key="y")

    st.scatter_chart(df[[x_col,y_col]].dropna(),x=x_col,y=y_col)

elif chart_type == "Histogram":

    st.subheader("Histogram")

    col = st.selectbox("Select numeric column", num_cols)

    fig,ax = plt.subplots()

    ax.hist(df[col].dropna(),bins=20,color = "#9969CC")

    ax.set_xlabel(col)

    ax.set_ylabel("Count")

    ax.set_title("Distribution of {col}")

    st.pyplot(fig)

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.page_link("pages/1_Data_exploration.py",label="Exploration page")

with col2:

    st.page_link("pages/3_insights.py",label="Insighits page",use_container_width=True)