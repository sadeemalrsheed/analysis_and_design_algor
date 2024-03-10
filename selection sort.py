# Function to perform selection sort on an array
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        # Iterate over the unsorted part of the array to find the minimum element
        for j in range(i + 1, len(arr)):
            # Check if the current element is smaller than the minimum found so far
            if arr[j] < arr[min_index]:
                # Update the index of the minimum element
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
# Example:
my_array = [7,98,55,20,10]
# Call the selection_sort function to sort the array
selection_sort(my_array)
# Print the sorted array
print("Sorted array:", my_array)
