import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f = open('paramater_1season_00325.txt', 'rb')
cl = pickle.load(f)
defence_Newcastle = [];
defence_Bournemouth = [];
defence_Brighton = [];
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
		defence_Newcastle.append(-99)
	else:
		defence_Newcastle.append(elem['defence_Newcastle'])
for elem in cl:
	if elem == 0:
		defence_Bournemouth.append(-99)
	else:
		defence_Bournemouth.append(elem['defence_Bournemouth'])
for elem in cl:
	if elem == 0:
		defence_Brighton.append(-99)
	else:
		defence_Brighton.append(elem['defence_Brighton'])
clean_missing_data(defence_Newcastle)
clean_missing_data(defence_Bournemouth)
clean_missing_data(defence_Brighton)
print(clean_missing_data(defence_Newcastle))	
plt.plot(range(99,-1,-3), np.exp(clean_missing_data(defence_Newcastle)), 'go-', label='line 1', linewidth=2)
plt.plot(range(99,-1,-3), np.exp(clean_missing_data(defence_Bournemouth)), 'go-', label='line 2', linewidth=2, color = 'blue')
plt.plot(range(99,-1,-3), np.exp(clean_missing_data(defence_Brighton)), 'go-', label='line 3', linewidth=2, color = 'yellow')
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([0,1])
plt.xlabel('days ago')
plt.ylabel('defence strength')
plt.savefig('defence Parameter')	
#print(a.append(cl[0]['defence_Newcastle']))
#for dicts in cl:
#	a.append(dicts["defence_Newcastle"])
#print(cl['defence_Newcastle'])
