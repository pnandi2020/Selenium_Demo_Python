#Length of the List
numbers = [2, 5, 7, 9]
print(len(numbers))
#returns the item in the list with the maximum value
numbers = [2, 5, 7, 9]
print(max(numbers))
#returns the item in the list with the minimum value
numbers = [2, 5, 7, 9]
print(min(numbers))
#Delete the element from the list
values = [2, 5, 7, 9]
values.remove(2)
print(values)
#reverse the object of the list
values = [2, 5, 7, 10]
values.reverse()
print(values)
#To get the sum of all values
values = [2, 5, 10]
sum_of_values = sum(values)
print(sum_of_values)
# To sort the values in ascending order:
values = [1, 7, 9, 3, 5]
values.sort()
print(values)
# To sort the values in descending order:
values = [2, 10, 7, 14, 50]
values.sort(reverse = True)
print(values)