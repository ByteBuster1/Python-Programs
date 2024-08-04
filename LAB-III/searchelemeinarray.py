def search_element(arr, element):
    if element in arr:
        return arr.index(element)
    else:
        return -1

array = [1, 2, 3, 4, 5]
element = 3
index = search_element(array, element)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")