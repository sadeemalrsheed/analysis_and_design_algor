# Function to perform insertion sort on a subarray from index low to high
def insertion_sort(arr, low, high):
    # Loop through the elements starting from the second one in the subarray
    for i in range(low + 1, high + 1):
        # Save the current element to be compared
        key = arr[i]
        # Move elements greater than key to one position ahead of their current position
        j = i - 1
        while j >= low and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key at its correct position in the sorted array
        arr[j + 1] = key
# Function to perform the quicksort algorithm on the entire array
def quick_sort(arr, low, high, threshold=10):
    # Check if there are more than one element in the subarray
    if low < high:
        # If the size of the subarray is less than or equal to the threshold, use insertion sort
        if high - low + 1 <= threshold:
            insertion_sort(arr, low, high)
        else:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)
            # Recursively sort the subarrays on both sides of the pivot
            quick_sort(arr, low, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, high)
# Function to partition the array and choose a pivot
def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1
    # Loop through the elements in the subarray from index 'low' to 'high'
    for j in range(low, high):
        # Check if the current element is less than or equal to the pivot
        if arr[j] <= pivot:
            # Increment the index of the smaller elements (i)
            i += 1
            # Swap the current element with the element at index 'i'
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
# Example:
# Create an array to be sorted
my_array = [28,5,20,99,32,1,10,66,43,90]
# Call the quick_sort function to sort the entire array
quick_sort(my_array, 0, len(my_array) - 1)
# Print the sorted array
print("Sorted array:", my_array)
