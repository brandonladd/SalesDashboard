import pandas as pd
import plotly.express as px
import streamlit as st



# SET PAGE CONFIGURATION:
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":balloon:",
                   layout="wide")

# HIDE THE HAMBURGER ICON IN TOP RIGHT:
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;} 
    </style>
    """,
    unsafe_allow_html=True
)

# ADD THE TITLE:
st.title("Superstore Sales Dashboard")
st.markdown("---")


# CACHE THE EXCEL FILE SO YOU DON'T HAVE TO KEEP RELOADING IT:
@st.cache_data
def excel_sheet_cache():
    dfx = pd.read_excel(
        io="C:\\Users\\Brandon\\Downloads\\super.xlsx",
        engine='openpyxl',
        sheet_name='Orders',
        usecols='A:U',
        nrows=9996,
    )
    return dfx


# NAME THE DATAFRAME AFTER CACHING IT:
df = excel_sheet_cache()

# ASSIGN STATES TO THE PROPER REGIONS:

regions = {
    'East': ['Pennsylvania', 'Delaware', 'New York', 'Ohio', 'Connecticut', 'New Jersey', 'Massachusetts',
             'Rhode Island', 'New Hampshire', 'Maryland', 'District of Columbia', 'Vermont', 'Maine', 'West Virginia'],
    'West': ['California', 'Washington', 'Utah', 'Arizona', 'Oregon', 'Colorado', 'New Mexico', 'Nevada', 'Montana',
             'Idaho', 'Wyoming'],
    'Central': ['Texas', 'Wisconsin', 'Nebraska', 'Illinois', 'Minnesota', 'Michigan', 'Indiana', 'Iowa', 'Missouri',
                'Oklahoma', 'Kansas', 'South Dakota', 'North Dakota'],
    'South': ['Kentucky', 'Florida', 'North Carolina', 'Virginia', 'Tennessee', 'Alabama', 'South Carolina',
              'Louisiana', 'Georgia', 'Mississippi', 'Arkansas']
}

# SIDEBAR
st.sidebar.header("Filter:")

# SELECT REGION:
region = st.sidebar.multiselect(
    "Select Region:",
    options=list(regions.keys()),
    default=list(regions.keys())

)

# DYNAMICALLY UPDATE STATES BASED ON SELECTED REGION:
states = [state for r in region for state in regions.get(r, [])]

# SELECT STATE:
state = st.sidebar.multiselect(
    "Select State:",
    options=states,
    default=states

)

# SELECT CATEGORY:
category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()

)

# UPDATE THE DATAFRAME TO INCLUDE ONLY THE SELECTED OPTIONS:
selected = df.query(
    "Region == @region & State in @state & Category == @category"
)

# IF NOTHING IS SELECTED, THROW A WARNING MESSAGE:
if selected.empty:
    st.warning("Please select a valid option.")


# CALCULATE KEY PERFORMANCE INDICATORS (KPI'S):
else:
    total_sales = int(selected["Sales"].sum())
    total_profit = int(selected["Profit"].sum())
    average_profit = round(selected["Profit"].mean(), 2)
    highest_profit = round(max(selected["Profit"]), 2)
    lowest_profit = round(min(selected["Profit"]), 2)
    average_sales = round(selected["Sales"].mean(), 2)
    most_discounts = max(selected["Discount"])
    least_discounts = min(selected["Discount"])
    expenses = int(total_sales - total_profit)

    # CREATE 6 DIFFERENT COLUMNS TO DISPLAY KPI'S:
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

    # USE PANDAS GROUPBY() TO ORGANIZE DATA BY CATEGORY AND TOTAL SALES:

    category_sales = (
        selected.groupby(by=["Category"]).sum()[["Sales"]]

    )

    # SALES BY PRODUCT LINE [BAR CHART]

    bar_chart_figure = px.bar(
        category_sales,
        x="Sales",
        y=category_sales.index,
        orientation="h",

    )

    # UPDATE BAR CHART SO THAT THE BACKGROUND IS TRANSPARENT AND GIVE IT A TITLE
    bar_chart_figure.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        title={
            'text': '<b>Sales by Category</b>',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24}
        }
    )

    # DEFINE NAMES AND VALUES FOR PIE CHART:
    names = selected["Region"]
    values = selected["Sales"]

    # SALES BY REGION [PIE CHART]:
    pie_chart_figure = px.pie(
        category_sales,
        values=values,
        names=names,
        template="plotly_dark"
    )

    # UPDATE THE BACKGROUND OF THE CHART TO TRANSPARENT AND GIVE IT A TITLE:

    pie_chart_figure.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(0,0,0,0)"
        ),
        title={
            'text': '<b>Sales by Region</b>',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24}
        }
    )
    # CREATE 2 COLUMNS TO FORMAT THE BAR AND PIE CHART ON THE SCREEN:
    maincol1, maincol2 = st.columns(2)

    maincol1.plotly_chart(bar_chart_figure, use_container_width=True)
    maincol2.plotly_chart(pie_chart_figure, use_container_width=True)

    # HIGHEST PROFITING STATES TABLE:

    highest_profit_state = selected.groupby("State").sum().sort_values("Profit", ascending=False).head(10).reset_index()
    highest_profit_state.index = highest_profit_state.index + 1
    highest_profit_state["Profit"] = highest_profit_state["Profit"].apply(lambda x: "{:.2f}".format(x))
    st.subheader("Highest Profiting States")
    st.table(highest_profit_state[["State", "Profit"]])

    # TOTAL SALES BY REGION TABLE:

    total_sales_by_region = selected.groupby("Region").sum().sort_values("Sales", ascending=False).reset_index()
    total_sales_by_region.index = total_sales_by_region.index + 1
    total_sales_by_region["Sales"] = total_sales_by_region["Sales"].apply(lambda x: "{:.2f}".format(x))
    st.subheader("Total Sales by Region")
    st.table(total_sales_by_region[["Region", "Sales"]])


