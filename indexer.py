import pandas as pd
import openpyxl
from tkinter import Tk, filedialog



# Create a Tkinter root window (it won't be shown)
root = Tk()
root.withdraw()  # Hide the main window

# Open a file dialog for the user to choose a file
df = filedialog.askopenfilename(title="Pick a file for indexing", filetypes=[("CSV files", "*.csv"),("Excel files", "*.xlsx")])


#Check if the file is an excel or csv file and then read into pandas accordingly  
if df.endswith('.xlsx'):
    df = pd.read_excel(df)
    df.to_csv("df.csv", index=None, header=True)
    indexfile = pd.DataFrame(pd.read_csv("df.csv"))
    
    print("excel file")

elif df.endswith('.csv'):
    indexfile = pd.read_csv(df)
    print("csv file")



#Allows user to give a column and keyword or words
user_column = input("Choose a column to filter by: ")
user_keyword = input("Choose a keyword by: ")

#Remove NAs before filtering
indexfile_clean = indexfile.dropna(subset=[user_column])

filtered_rows = indexfile_clean[indexfile_clean[user_column].str.contains(user_keyword)]
#print(rows)

print(filtered_rows)

newSpreadsheetName = input("Please name the new filtered spreadsheet: ")

#print(filtered_rows)
filtered_rows.to_csv(newSpreadsheetName + ".csv", index = False)
