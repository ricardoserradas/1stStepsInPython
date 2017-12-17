
# coding: utf-8

# # Problem: Counting the number of negative numbers.
# 
# You are given a 2-dimensional array with integers.
# 
# Example Input:  
# [[-4, -3, -1, 1],  
# &nbsp;[-2, -2,  1, 2],  
# &nbsp;[-1,&nbsp; 1,&nbsp; 2, 3],  
# &nbsp;[ 1,&nbsp; 2,&nbsp; 4, 5]]
# 
# Write a function, count_negatives(input), which finds and returns the number of negative integers in th array.

# ### NOTE: Make sure to run your program once you write it :)

# # Implement your function below.

# In[22]:


# Input: A 2-dimensional array with integers.  Example below.
#[[-4, -3, -1, 1],
# [-2, -2,  1, 2],
# [-1,  1,  2, 3],
# [ 1,  2,  4, 5]]
# Returns:
#  The number of negative numbers in the array.
#  In the above case, this function should return 6
#  since there are 6 negative numbers in the array.
def count_negatives(given_array):
    # O(n^2) solution
    # count = 0
    # size = len(given_array)
    # Iterating over lines
    
    # for i in range(size):
    #    for j in range(size):
    #        if(given_array[i][j] < 0):
    #            count+=1
                
    #return count
    
    # O(n) solution
    
    count = 0
    row = 0
    column = len(given_array) - 1
    
    while column >= 0 and row < len(given_array):
        if(given_array[row][column] < 0):
            count = count + column + 1
            row+=1
        else:
            column-=1
    return count


# # Use the code below to test your function.

# In[23]:


print("""
How many negative numbers are there in the following array?
(There are 6.)

[[-4, -3, -1, 1],
 [-2, -2,  1, 2],
 [-1,  1,  2, 3],
 [ 1,  2,  4, 5]]
""")

count_negatives(
[[-4, -3, -1, 1],
 [-2, -2,  1, 2],
 [-1,  1,  2, 3],
 [ 1,  2,  4, 5]])


# In[24]:


print("""
How many negative numbers are there in the following array?
(There is 1.)

[[-1, 0],
 [0,  0]]
""")

count_negatives(
[[-1, 0],
 [0,  0]])


# In[25]:


print("""
How many negative numbers are there in the following array?
(There are 2.)

[[-2, 0],
 [-1, 0]]
""")

count_negatives(
[[-2, 0],
 [-1, 0]])


# In[26]:


print("""
How many negative numbers are there in the following array?
(There are none.)

[[0]]
""")

count_negatives([[0]])

