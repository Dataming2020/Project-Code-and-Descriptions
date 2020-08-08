import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f = open('paramater_1season_00325.txt', 'rb')
cl = pickle.load(f)
HomeAdv = [];
rho = [];
def get_right_number(numbers, i):

    if i >= len(numbers) - 1:
        right = -99
    else:
        right = numbers[i + 1]
        if right == -99:
            right = get_right_number(numbers, i+1)
    return right

def clean_missing_data(numbers):

    if all(x == -99 for x in numbers):
        print('All values in list are invalid. Could not compute.')
        return
    clean_numbers = []

    for i in range(len(numbers)):
        if numbers[i] != -99:
            clean_numbers.append(numbers[i])
        else:
            valid_count = 0

            if i == 0:
                left = 0
            else:
                left = clean_numbers[i - 1]
                valid_count += 1

            right = get_right_number(numbers, i)
            if right == -99:
                right = 0
            else:
                valid_count += 1

            average = (left + right) / valid_count
            clean_numbers.append(average)

    return clean_numbers
for elem in cl:
	if elem == 0:
		rho.append(-99)
	else:
		rho.append(elem['rho'])
for elem in cl:
	if elem == 0:
		HomeAdv.append(-99)
	else:
		HomeAdv.append(elem['home_adv'])
print(np.exp(clean_missing_data(HomeAdv)))

plt.plot(range(99,-1,-3), np.exp(clean_missing_data(rho)), 'go-', label='line 1', linewidth=2)
plt.plot(range(99,-1,-3), np.exp(clean_missing_data(HomeAdv)), 'go-', label='line 2', linewidth=2, color = 'blue')
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([0,2.0])
plt.xlabel('days ago')
plt.ylabel('rho_homeAdv')
plt.savefig('rho_HomeAdv')	

