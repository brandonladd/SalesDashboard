# Interactive Sales Dashboard
Sales Dashboard is a web application written in Python that provides an interactive and visually appealing way to analyze sales data from an Excel file. It leverages the Streamlit API to display data in the form of graphs, charts, and tables, making it easier for users to understand and interpret the information for more informed business decisions.

![dashgiffy](https://github.com/brandonladd/SalesDashboard/assets/124627243/4062a077-8663-49d9-9852-6650f9c1df8f)

## Features
- Visual representation of sales data through graphs, charts, and tables.
- Key Performance Indicators (KPIs) displayed at the top of the dashboard.
- Filter functionality to select regions, states, and categories for data analysis.
- Calculation of important metrics such as total sales, total profit, average profit, highest and lowest profits, average sales, and more.
- Dynamic updates to the displayed data based on user-selected filters.
- Works on Mac, Linux, and Windows.

## Installation
- Install Python (https://www.python.org/)
- Install Streamlit (https://streamlit.io/)
- Download (`super.xlsx`) from the Github repository by clicking on it, then clicking 'view raw' and downloading the file.
- Clone the repository to your local machine.
- Install the necessary dependencies in the command line or terminal by running the commands `pip install pandas==1.5.0' 'pip install plotly-express' 'pip install streamlit' 'pip install openpyxl'
- Ensure that you have the original Excel file (`super.xlsx`) used for the project available on your local machine. This can be found for download in the github repository.
- Open the `main.py` file in a text editor.
- Locate the `excel_sheet_cache` function in the code.
- In the `io` parameter of the `pd.read_excel` function within the `excel_sheet_cache` function, replace the existing file path (`C:\\Users\\Brandon\\Downloads\\super.xlsx`) with the file path of the original Excel file on your machine.
- Save the `main.py` file.
- Run the application by executing the command `streamlit run main.py` in your terminal or command prompt.
- The Sales Dashboard web application will launch in your default web browser.
- Explore the dashboard by interacting with the graphs, charts, and tables.
- Use the sidebar filters to select regions, states, and categories for data analysis.
- The dashboard will dynamically update the displayed data based on your filter selections.
- To end the streamlit session, simply press Ctrl + C with the command line interface open

## Dependencies
This program relies on the following dependencies:
- pandas
- streamlit
- plotly

## Future Enhancements
- Allow users to upload their own Excel files for data analysis.
- Add more interactive features such as drill-down functionality and data filtering options.
- Improve the user interface and visualizations for better data representation.

## Works Cited
- The video used for inspiration: https://www.youtube.com/watch?v=Sb0A9i6d320&ab_channel=CodingIsFun
- Used streamlit's website for almost everything: https://docs.streamlit.io/
- I also used plotly's website, mainly for the pie chart: https://plotly.com/python/graphing-multiple-chart-types/  and also https://plotly.com/python/templates/
- This was used to help edit the legend transparency/color: https://www.geeksforgeeks.org/python-plotly-how-to-customize-legend/#
- For misc. of course I referenced the almighty: https://stackoverflow.com/
- For the dataset, I found it at this website: https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls

## Dataset Info
- This dataset is an excel sheet full of information from a national Superstore that sells Furniture, Office Supplies, and Technology. It is significant because my app can leverage this information to help a business owner make proper decisions based of visual representations of said data.

## Possible "datetime" Error
- If you see this error when running the program:

![datetimeerror](https://github.com/brandonladd/SalesDashboard/assets/124627243/053952f9-dcba-4a1f-9dfb-dcf25c61325f)

- Go into terminal or command prompt
- type: pip uninstall pandas, pip install pandas==1.5.0
