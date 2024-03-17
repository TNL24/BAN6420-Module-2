This script provides functionalities to analyze and export employee details from a CSV file containing salary data.
Dependencies:
pandas
Data File:
The script expects a CSV file named "salaries for San Francisco.csv" located at C:/Users/Ogbemudia/Music/OneDrive/Documents/. Adapt this path to the location of your actual data file.
Functionalities:

get_employee_details(name): This function searches for an employee by name in the loaded data and returns a dictionary containing their details (name, job title, base pay, etc.) if found. If not found, it returns an error message.

employee_details_dict: This dictionary stores employee information retrieved from the CSV data. Each key in the dictionary represents an employee ID (assuming the first column contains the ID), and the corresponding value is another dictionary containing details like name, job title, and base pay.

export_employee_details(employee_name): This function allows you to export the details of a specific employee to a CSV file named "details.csv" within a folder called "Employee Profile". The folder will be created if it doesn't exist. In case of errors during export, the function will print an informative message.

How to Use:

Update Data Path: Modify the path to your CSV file in the first line (after pd.read_csv).
Search Employee Details:
Use get_employee_details("Employee Name") to retrieve details of a specific employee. Replace "Employee Name" with the actual name you want to search.
Export Employee Details:
Use export_employee_details("Employee Name") to export the details of a specific employee. This will create a "details.csv" file in the "Employee Profile" directory.

Margaret Edokpolor 
