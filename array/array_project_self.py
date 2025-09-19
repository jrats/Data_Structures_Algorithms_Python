import numpy as np
days = int(input("How many days temperature do you want to enter"))
temp_array = np.array([], dtype=int)
for i in range (0, days):
    temp = int(input(f"Enter Day {i+1}'s temperature: "))
    temp_array = np.append(temp_array, temp)
avg = np.average(temp_array)
print(avg)
count = 0
for j in temp_array:
    if (j > avg):
        count = count +1
print(f"{count} day(s) temperature above average")

