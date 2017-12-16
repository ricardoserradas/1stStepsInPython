
# coding: utf-8

# # Problem: Compare two strings as numbers!
# 
# You are given two non-negative integers in strings.
# 
# Example: "1221" and "123"
# 
# Write a function, larger_than(a, b) which returns True if the first number is larger than the second one.
# 
# ***Solve this problem without converting the strings to numbers!***
# 
# ## Examples:
# 
# - **larger_than( "112", "111" )** should return True.
# - **larger_than( "525", "1111" )** should return False.
# - **larger_than( "11", "0" )** should return True.
# - **larger_than( "1", "1" )** should return False.

# ### NOTE: Make sure to run your program once you write it :)

# # Implement your function below.

# In[ ]:


# Remember, you can compare single-character numbers in strings as follows:
"3" > "1"


# In[6]:


# Input:
#  a: The first non-negative integer in string. Example: "123"
#  b: The second non-negative integer in string. Example: "3344"
# Returns:
#  True if a is larger than b.
#  False if a is smaller than or equal to b.
def larger_than(a, b):
    difference = len(a) - len(b)
    zeros = ""
    
    if(difference < 0):
        difference = difference * (-1)
        
    if(difference > 0):
        for i in range(difference):
            zeros = zeros + "0"
        if(len(a) < len(b)):
            a = zeros + a
        else:
            b = zeros + b
    
    for i in range(len(a)):
        if(i == len(a) - 1):
            if(a[i] <= b[i]):
                return False
        elif(a[i] < b[i]):
            return False
    return True
    


# # Use the code below to test your function.

# In[7]:


print('Is "112" larger than "111"? (Should be True.)')
print(larger_than( "112", "111" ))


# In[8]:


print('Is "525" larger than "1111"? (Should be False.)')
print(larger_than( "525", "1111" ))


# In[9]:


print('Is "11" larger than "0"? (Should be True.)')
print(larger_than( "11", "0" ))


# In[10]:


print('Is "1" larger than "1"? (Should be False.)')
print(larger_than( "1", "1" ))

