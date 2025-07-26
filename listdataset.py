

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()  # Remove the last element
my_list.sort()  # Sort in ascending order
index_of_30 = my_list.index(30)  # Find the index of 30
print(index_of_30)  # Print the index of 30
print(my_list)  # Print the final list to see the result    