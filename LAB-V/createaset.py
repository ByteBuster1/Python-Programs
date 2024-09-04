#it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Part 1: Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of it_companies:", len(it_companies))
# Part 2: Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Updated it_companies after adding 'Twitter':", it_companies)
# Part 3: Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla', 'Netflix', 'Samsung'])
print("Updated it_companies after adding multiple companies:", it_companies)
# Part 4: Remove one of the companies from the set it_companies
it_companies.remove('Oracle')  # you can also use discard()
print("Updated it_companies after removing 'Oracle':", it_companies)
# Part 5: Difference between remove and discard
# `remove` raises an error if the element is not found
# `discard` does not raise an error if the element is not found