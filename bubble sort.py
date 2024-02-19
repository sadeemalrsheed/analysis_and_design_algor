def bubble_sort(x):
    n = len(x)  # Get the length of the array
    for i in range(n - 1):  # Outer loop for the number of passes
        for j in range(n - 1):  # Inner loop for pairwise comparisons
            if x[j] > x[j + 1]:  # Check if the current element is greater than the next one
                x[j], x[j + 1] = x[j + 1], x[j]  # Swap the elements if they are in the wrong order
my_list = [90, 65, 400, 23, 89, 5, 29, 44, 12, 234, 58, 6]
bubble_sort(my_list)  # Call the bubble_sort function to sort the list
print("Sorted list using bubble sort:", my_list)  # Print the sorted list
