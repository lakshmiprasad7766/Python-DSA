# # Hi this is first basic python code to push into GitHub Repository

# #print("Hello Github, this is the first commit from my local machine")

# print("Python coding for learning")

# print(2+3)


# # Variables
# x = 2
# y = 4
 
# print("Sum of x and y is: ", x + y)


# x=9
# print("New value of x is: ", x)


#string
name = "Prasad Tech"
print("Name is: ", name)


#Concatenation
name + 'Channel'
print("Updated Name is: ", name + ' Channel')


# string reversal
reversed_name = name[::-1]
print("Reversed Name is: ", reversed_name)



#print (name[1:5])

print('my name is ' + name[7:])

print(len(name))


#List
nums = [33, 12, 43, 66 , 557, 78, 89, 90]
print(nums)

print(nums[0])

print(nums[1:5])

print(nums[2:])

print(nums[-1])

print(nums[-3:])

# Lists are mutable
nums[0] = 100
print(nums) 

#Pop an element
popped_element = nums.pop(2)
print("Popped Element: ", popped_element)
print("List after popping: ", nums)

#delete an element
del nums[3:]
print("List after deletion: ", nums)
