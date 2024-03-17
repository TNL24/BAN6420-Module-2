# Install required packages if not already installed
if (!require("unzip")) install.packages("unzip")
if (!require("dplyr")) install.packages("dplyr")

# Specify file paths
zipped_folder_path <- "path/to/Employee_Profile.zip"  # Replace with your path
unpacked_folder_path <- "path/to/unpacked_folder"     # Replace with your path
csv_file_path <- paste0(unpacked_folder_path, "/details.csv")

# Unzip the folder
tryCatch({
  unzip(zipped_folder_path, exdir = unpacked_folder_path)
}, error = function(e) {
  print(paste0("Error unzipping:", e))
})

# Read the CSV data
if (test.path(csv_file_path)) {
  employee_data <- read.csv(csv_file_path)
  
  # Display data summary (optional)
  summary(employee_data)
  
  # Explore or analyze the data as needed
  # ... your code here ...
  
  # Clean up (optional)
  unlink(csv_file_path)  # Remove CSV file
  unlink(unpacked_folder_path, recursive = TRUE)  # Remove unpacked folder
} else {
  print("CSV file not found.")
}


