# Create a dictionary from user input where the keys are name, age, city, state (3 entries) and convert that dictionary into a data frame.

import pandas as pd

empty_dict = {'name': [], 'age': [], 'city': [], 'state': []}
key_list = ['name', 'age', 'city', 'state']

for _ in range(3):
    for key in key_list:
        user_input = input(f"Enter {key.title()} of User: ").title()
        empty_dict[key].append(user_input)
    print()

print("Dictionary generated post 3 user entries:")
print(empty_dict)

df = pd.DataFrame(empty_dict)
print("\nDataframe generated from dictionary:")
print(df)


"""Output:
Enter Name of User: vijay
Enter Age of User: 24
Enter City of User: mumbai
Enter State of User: maharashtra

Enter Name of User: bijoy
Enter Age of User: 28
Enter City of User: cuttack
Enter State of User: odisha

Enter Name of User: samarth
Enter Age of User: 26
Enter City of User: noida
Enter State of User: uttar pradesh

Dictionary generated post 3 user entries:
{'name': ['Vijay', 'Bijoy', 'Samarth'], 'age': ['24', '28', '26'], 'city': ['Mumbai', 'Cuttack', 'Noida'], 'state': ['Maharashtra', 'Odisha', 'Uttar Pradesh']}

Dataframe generated from dictionary:
      name age     city          state
0    Vijay  24   Mumbai    Maharashtra
1    Bijoy  28  Cuttack         Odisha
2  Samarth  26    Noida  Uttar Pradesh
"""