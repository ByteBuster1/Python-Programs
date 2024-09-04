A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Part 1: Join A and B
A_B_union = A.union(B)
print("Union of A and B:", A_B_union)
# Part 2: Find A intersection B
A_B_intersection = A.intersection(B)
print("Intersection of A and B:", A_B_intersection)
# Part 3: Is A subset of B
is_A_subset_B = A.issubset(B)
print("Is A a subset of B?", is_A_subset_B)
# Part 4: Are A and B disjoint sets
are_A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_A_B_disjoint)
# Part 5: Join A with B and B with A
A.update(B)
print("Updated A after joining with B:", A)
B.update(A)
print("Updated B after joining with A:", B)
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff)
# Part 7: Delete the sets completely
del A
del B
print("Sets A and B have been deleted.")