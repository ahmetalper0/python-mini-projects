array = [ -3, 6, -5, 2, 1, -2, 4, -4, -6, 3, 5, -1, 0 ]

def selection_sort(array):

    for i in range(len(array) - 1):

        min_index = i

        for j in range(i + 1, len(array)):

            if array[j] < array[min_index]:

                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array

print(f'\n{array}')
print(f'\n{selection_sort(array)}\n')
