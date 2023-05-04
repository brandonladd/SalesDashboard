import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title= "Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

@st.cache_data
def excel_sheet_cache():
    df = pd.read_excel(
        io="C:\\Users\\Brandon\\Downloads\\super.xlsx",
        engine='openpyxl',
        sheet_name='Orders',
        usecols='A:U',
        nrows=9996,
    )
    return df

df = excel_sheet_cache()


#SIDEBAR
st.sidebar.header("Filter:")

region = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()

 )

state = st.sidebar.multiselect(
    "Select State:",
    options=df["State"].unique(),
    default=df["State"].unique()

 )


category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()

 )


selected = df.query(
    "Region == @region & State == @state & Category == @category"
)


#MAINPAGE

st.title("Sales Dashboard")
st.markdown("##")


#Key Performance Indicators (KPI's)

total_sales = int(selected["Sales"].sum())
total_profit = int(selected["Profit"].sum())
average_profit = round(selected["Profit"].mean(), 2)
highest_profit = round(max(selected["Profit"]), 2)
lowest_profit = round(min(selected["Profit"]), 2)
average_sales = round(selected["Sales"].mean(), 2)
most_discounts = max(selected["Discount"])
least_discounts = min(selected["Discount"])
expenses = int(total_sales - total_profit)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.subheader("Total Sales:")
    st.subheader(f"$ {total_sales:,}")
with col2:
    st.subheader("Total Profit:")
    st.subheader(f"$ {total_profit:,}")
with col3:
    st.subheader("Business Expenses:")
    st.subheader(f"$ {expenses:,}")
with col4:
    st.subheader("Highest Profit:")
    st.subheader(f"$ {highest_profit:,}")
with col5:
    st.subheader("Lowest Profit:")
    st.subheader(f"$ {lowest_profit:,}")
with col6:
    st.subheader("Average Sales:")
    st.subheader(f"$ {average_profit:,}")

st.markdown("---")



#Use Pandas groupby() to organize data by Category and total sales

category_sales = (
    selected.groupby(by=["Category"]).sum()[["Sales"]]

)

#SALES BY PRODUCT LINE [BAR CHART]

bar_chart_figure = px.bar(
    category_sales,
    x="Sales",
    y=category_sales.index,
    orientation="h",

)

#UPDATE BAR CHART SO THAT THE BACKGROUND IS TRANSPARENT
bar_chart_figure.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)"
)

st.plotly_chart(bar_chart_figure)

names = selected["Region"]
values = selected["Sales"]

pie_chart_figure = px.pie(
    category_sales,
    values=values,
    names=names,
    title="Sales by State",
    template="plotly_dark"
)

#UPDATE THE BACKGROUND OF THE CHART TO TRANSPARENT AND COLOR OF THE LEGEND SO THAT IS IS VISIBLE IN LIGHT/DARK MODE:

pie_chart_figure.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    legend=dict(
        bgcolor="Blue"
    )
)

st.plotly_chart(pie_chart_figure)



















