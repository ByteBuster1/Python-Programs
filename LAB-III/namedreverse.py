def reverse_list(arr):
  reversed_list = []
  for i in arr:
    reversed_list.insert(0, i)
  return reversed_list

original_list = [1,2,3,4,5]
reversed_list = reverse_list(original_list)
print(f"Original list is {original_list}")
print(f"Reversed list is {reversed_list}")