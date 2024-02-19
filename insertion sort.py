def insertion_sort(x):
    for i in range(1, len(x)):  #Iterate over the elements starting from the second one
        key = x[i]  # Current element to be compared and inserted
        j = i - 1  # Index of the previous element
        while j >= 0 and key < x[j]:#Move elements greater than key to one position ahead
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key  #Insert key into the sorted part
my_list = [90, 65, 400, 23, 89, 5, 29, 44, 12, 234, 58, 6]
insertion_sort(my_list)  # Call the insertion_sort function to sort the list
print("Sorted list using insertion sort:", my_list)  # Print the sorted list
