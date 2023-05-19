# Interactive Sales Dashboard
Sales Dashboard is a web application written in Python that provides an interactive and visually appealing way to analyze sales data from an Excel file. It leverages the Streamlit API to display data in the form of graphs, charts, and tables, making it easier for users to understand and interpret the information for more informed business decisions.

## Features
- Visual representation of sales data through graphs, charts, and tables.
- Key Performance Indicators (KPIs) displayed at the top of the dashboard.
- Filter functionality to select regions, states, and categories for data analysis.
- Calculation of important metrics such as total sales, total profit, average profit, highest and lowest profits, average sales, and more.
- Dynamic updates to the displayed data based on user-selected filters.

## Installation
- Install Python (https://www.python.org/)
- Install Streamlit (https://streamlit.io/)
- Clone the repository to your local machine.
- Install the necessary dependencies by running the commands `pip install pandas' 'pip install plotly' 'pip install streamlit'
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

## Dependencies
This program relies on the following dependencies:
- pandas
- streamlit
- plotly

## Future Enhancements
- Allow users to upload their own Excel files for data analysis.
- Add more interactive features such as drill-down functionality and data filtering options.
- Improve the user interface and visualizations for better data representation.




