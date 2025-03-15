# Create a dictionary from user input where the keys are the employee's ID, name, salary, and department  (5 entries) and convert that dictionary into a data frame.

import pandas as pd

employee_dict = {'ID': [], 'name': [], 'salary': [], 'department': []}
key_list = ['ID', 'name', 'salary', 'department']

for _ in range(5):
    for key in key_list:
        user_input = input(f"Enter {key.title()} of User: ").title()
        employee_dict[key].append(user_input)
    print()

print("Dictionary generated post 3 user entries:")
print(employee_dict)

df = pd.DataFrame(employee_dict)
print("\nDataframe generated from dictionary:")
print(df)


"""Output:
Enter Id of User: 001
Enter Name of User: vijay
Enter Salary of User: 25000
Enter Department of User: operations

Enter Id of User: 002
Enter Name of User: bijoy
Enter Salary of User: 30000
Enter Department of User: recruitment

Enter Id of User: 003
Enter Name of User: samarth
Enter Salary of User: 40000
Enter Department of User: marketing

Enter Id of User: 004
Enter Name of User: rishabh
Enter Salary of User: 35000
Enter Department of User: sales

Enter Id of User: 005
Enter Name of User: vipin
Enter Salary of User: 5000
Enter Department of User: software

Dictionary generated post 3 user entries:
{'ID': ['001', '002', '003', '004', '005'], 'name': ['Vijay', 'Bijoy', 'Samarth', 'Rishabh', 'Vipin'], 'salary': ['25000', '30000', '40000', '35000', '5000'], 'department': ['Operations', 'Recruitment', 'Marketing', 'Sales', 'Software']}

Dataframe generated from dictionary:
    ID     name salary   department
0  001    Vijay  25000   Operations
1  002    Bijoy  30000  Recruitment
2  003  Samarth  40000    Marketing
3  004  Rishabh  35000        Sales
4  005    Vipin   5000     Software
"""

