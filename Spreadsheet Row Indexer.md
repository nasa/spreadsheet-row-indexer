**Notices:**Copyright © 2026 United States Government as represented by the Administrator of the National Aeronautics and Space Administration.  All Rights Reserved.  
  
**Disclaimers**  
  
No Warranty: THE SUBJECT SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR FREEDOM FROM INFRINGEMENT, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL BE ERROR FREE, OR ANY WARRANTY THAT DOCUMENTATION, IF PROVIDED, WILL CONFORM TO THE SUBJECT SOFTWARE. THIS AGREEMENT DOES NOT, IN ANY MANNER, CONSTITUTE AN ENDORSEMENT BY GOVERNMENT AGENCY OR ANY PRIOR RECIPIENT OF ANY RESULTS, RESULTING DESIGNS, HARDWARE, SOFTWARE PRODUCTS OR ANY OTHER APPLICATIONS RESULTING FROM USE OF THE SUBJECT SOFTWARE.  FURTHER, GOVERNMENT AGENCY DISCLAIMS ALL WARRANTIES AND LIABILITIES REGARDING THIRD-PARTY SOFTWARE, IF PRESENT IN THE ORIGINAL SOFTWARE, AND DISTRIBUTES IT "AS IS."  
  
Waiver and Indemnity:  RECIPIENT AGREES TO WAIVE ANY AND ALL CLAIMS AGAINST THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT.  IF RECIPIENT'S USE OF THE SUBJECT SOFTWARE RESULTS IN ANY LIABILITIES, DEMANDS, DAMAGES, EXPENSES OR LOSSES ARISING FROM SUCH USE, INCLUDING ANY DAMAGES FROM PRODUCTS BASED ON, OR RESULTING FROM, RECIPIENT'S USE OF THE SUBJECT SOFTWARE, RECIPIENT SHALL INDEMNIFY AND HOLD HARMLESS THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT, TO THE EXTENT PERMITTED BY LAW.  RECIPIENT'S SOLE REMEDY FOR ANY SUCH MATTER SHALL BE THE IMMEDIATE, UNILATERAL TERMINATION OF THIS AGREEMENT. 

# Introduction

This guide is to help with using the Indexer script to filter entire rows based on a column and keyword provided by the user. This script will work with .xslx and .csv file types. The main goal is to quickly and efficiently create a new .csv file of rows containing one similar parameter. For this guide, a sample directory was created with a number of employees with various roles and locations (Fig 1).

![[Pasted image 20250820133312.png]]*Figure 1. Sample directory of employees containing names, work group, job title, email, phone numbers and desk location.* 

The script uses the Python package pandas as a way of indexing and filtering rows. By providing a column and keyword, pandas will produce all the rows with the given parameters and a new .csv file will be created with the filtered rows. 

As an example, let's run the script and select all of the individuals in the "Sales" work_group. We start by loading the script "indexer.py" (Fig 2). 

![[Pasted image 20250820130434.png]]
*Figure 2. Start the script using the name "python" and the name of the script "indexer.py".*

After the script loads, a Windows Explorer box should open allowing you to choose a .xslx or .csv file. We're going to use directory.csv (Fig 3).

![[Pasted image 20250820130934.png]]
*Figure 3. A .xslx or .csv file can be read into Python for indexing. *

We have 9 columns in this example that could be used for filtering. We want to find all of the employees involved with Sales. So, we will chose the "work_group" column (Fig 4), then we can pick the keyword "Sales" to filter (Fig 5).

![[Pasted image 20250820131346.png]]
*Figure 4. The script needs a column name to filter by. In this case, we picked the "work_group" column.*

![[Pasted image 20250820131501.png]]
*Figure 5. The script requires a keyword to filter all of the rows. We are using the "Sales" keyword to get all individuals involved in Sales.*

Finally, after entering in the two required fields (column and keyword), a new .csv file is created (Fig 6) with our filtered rows containing all individuals from the "Sales" work group (Fig 7). We now have a spreadsheet of all the employees involved with "Sales". 

![[Pasted image 20250820131841.png]]
*Figure 6. After ensuring both required fields are given to the script, a new .csv file (filtered_rows.csv) is written with the desired filtered rows.*

![[Pasted image 20250820132029.png]]
*Figure 7. A .csv file containing all of the employees involved with "Sales"*