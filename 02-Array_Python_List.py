
# coding: utf-8

# # Problem: Find the second largest number in an array!
# 
# You are given an array (or a Python list) of integers.
# 
# For example, [1, 3, 4, 5, 0, 2].
# 
# Write a function, second_largest(given_list), which takes the list as the input, and returns the second largest number.
# 
# ## Examples:
# 
# - **second_largest( [1, 3, 4, 5, 0, 2] )** should return 4.
# - **second_largest( [-2, -1] )** should return -2.
# - **second_largest( [2, 2, 1] )** should return 2.
# - **second_largest( [2] )** should return None.
# - **second_largest( [] )** should return None.

# ### NOTE: Feel free to use any other language or any other IDE for solving this problem.
# 
# ### NOTE 2: Make sure to run your program once you write it.
# 
# #### Oh, and most importantly, have fun solving it! :)

# # Implement your function below.

# In[5]:


# Input:
#  a: The given list/array of integers.  Example: [1, -2, 3, 4]
# Returns:
#  The second largest number in the list or None if
#  the array's length is only 1 or 2.
def second_largest(given_list):
    if(len(given_list) < 2):
        return None
    else:
        largest = 0
        second_largest = 0
        
        for i in range(len(given_list)):
            if(i == 0):
                largest = given_list[i]
                second_largest = given_list[i]
            elif(given_list[i] > largest):
                second_largest = largest
                largest = given_list[i]
            elif(given_list[i] > second_largest):
                second_largest = given_list[i]
        return second_largest


# # Use the code below to test your function.

# In[6]:


print('The second largest number in [1, 3, 4, 5, 0, 2] is (should be 4):')
print(second_largest([1, 3, 4, 5, 0, 2]))


# In[7]:


print('The second largest number in [-2, -1] is: (should be -2)')
print(second_largest([-2, -1]))


# In[8]:


print('The second largest number in [2, 2, 1] is: (should be 2)')
print(second_largest([2, 2, 1]))


# In[9]:


print('The second largest number in [2] is: (should be None)')
print(second_largest([2]))


# In[10]:


print('The second largest number in [] is: (should be None)')
print(second_largest([]))

