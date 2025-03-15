#  Create a dictionary from user input where the keys are name, age, city and convert that dictionary into a data frame.

import pandas as pd

input_name = input("Enter approx 7 names separated by spaces: ").title()
input_age = input("\nEnter the ages for the names entered, separated by spaces: ")
input_city = input("\nEnter the cities for names entered, separated by spaces: ").title()

user_dict = {
    'name': input_name.split(),
    'age': list(map(int, input_age.split())),
    'city': input_city.split()
}

df = pd.DataFrame(user_dict)
pd.set_option('display.max_columns', None)
print("\nDataframe generated from the inputs:")
print(df)


"""Output:
Enter approx 7 names separated by spaces: Ajay rohit ravindra virat rahul rishabh arjun

Enter the ages for the names entered, separated by spaces: 28 34 26 27 30 29 31

Enter the cities for names entered, separated by spaces: gwalior delhi gurugram noida bangalore lucknow mumbai

Dataframe generated from the inputs:
       name  age       city
0      Ajay   28    Gwalior
1     Rohit   34      Delhi
2  Ravindra   26   Gurugram
3     Virat   27      Noida
4     Rahul   30  Bangalore
5   Rishabh   29    Lucknow
6     Arjun   31     Mumbai
"""