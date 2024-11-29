import numpy as np
import matplotlib.pyplot as plt


days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
cities = ['London', 'Kyiv', 'New York']


arr = np.array([
    [10, 11, 40],
    [15, 18, 20],
    [11, 0, 6],
    [5, 8, 10],
    [7, 10, 12],
    [12, 15, 10],
    [9, 10, 8]
], dtype=np.float32)


print(f'Initial array: {arr}')


mean_arr = np.mean(arr, axis=0)
max_arr = np.max(arr, axis=0)
min_arr_day_index = np.argmin(arr, axis=0)

arr += np.random.uniform(0, 1, size=[7, 3]) - 0.5

cities_mean_arr = np.mean(arr, axis=0)
days_mean_arr = np.mean(arr, axis=1)


for i in range(len(cities)):
    print(f'Avg temperature for {cities[i]}: {np.round(mean_arr[i])}')
    print(f'Max temperature for {cities[i]}: {np.round(max_arr[i])}')
    print(f'Min temperature in {cities[i]} was in {days[min_arr_day_index[i] - 1]} \n')


print(f'Modified array: {arr} \n')


for i in range(len(cities)):
    print(f'Avg temperature for {cities[i]} with noise: {int(cities_mean_arr[i])} \n')


for i in range(len(days)):
    print(f'Avg temperature for {days[i]} with noise: {int(days_mean_arr[i])} \n')


plt.scatter(cities, cities_mean_arr)
plt.title('Average temperature for cities')
plt.show()
