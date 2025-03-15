# Load JSON data and store it into a dataframe.

import pandas as pd

df = pd.read_json('employee_sales_data.json')
pd.set_option('display.max_columns', None)
print(df.head())


"""Output:
  Employee_ID  Employee_Name Department  Sales_Amount  Sales_Target  \
0      EMP001       John Doe      Sales         10000         12000   
1      EMP002     Jane Smith  Marketing         15000         14000   
2      EMP003     Sam Wilson         IT          7000          8000   
3      EMP004   Linda Taylor    Finance         12000         10000   
4      EMP005  Michael Brown      Sales         11000         13000   

   Achieved_Target  
0            False  
1             True  
2            False  
3             True  
4            False  
"""