import pandas as pd 

# adapt data path to my environment

salary_data = pd.read_csv("C:/Users/Ogbemudia/Music/OneDrive/Documents/salaries for San Francisco.csv")

def get_employee_details(name):
    try:
        employee_details = salary_data[salary_data['Name'] == name].to_dict(orient='records')[0]
        return employee_details
    except IndexError:
        return f"No employee found with the name {name}"
    
    employee_details_dict = {}

for index, row in salary_data.iterrows():
    # Assuming the first column is the employee ID or unique identifier
    employee_id = row.iloc[0]  # Adjust if needed

    # Create a dictionary for each employee
    employee_details_dict[employee_id] = {
         "EmployeeName": row.iloc[0],  # Assuming the second column is the employee name
        "JobTitle": row.iloc[1],  # Assuming the third column is the job title
        "BasePay": row.iloc[2],  # Assuming the fourth column is the Base Pay
        # Add other relevant details as needed
    }

# Now you can use the dictionary for analysis, manipulation, etc.
    
def get_employee_details(employee_name):
    global salary_data

    try:
        employee_details = salary_data.loc[salary_data["Name"] == employee_name].to_dict("records")[0]
        return employee_details
    except IndexError:
        print(f"Employee '{employee_name}' not found in data.")
        return None
    except KeyError as e:
        print(f"Error: Invalid key '{e}' in employee data.")
        return None

# Use try-except blocks in other functions as needed
    
import os
import csv

def export_employee_details(employee_name):
    employee_details = get_employee_details(employee_name)

    if employee_details:
        try:
            os.mkdir("Employee Profile")  # Create folder if it doesn't exist
            with open("Employee Profile/details.csv", "w", newline="") as f:  # Added closing parenthesis
                writer = csv.DictWriter(f, fieldnames=employee_details.keys())
                writer.writeheader()
                writer.writerow(employee_details)  # Added missing closing parenthesis
        except Exception as e:  # Handle potential errors
            print(f"Error exporting employee details: {e}")
            return None  # Optional: return None to indicate failure