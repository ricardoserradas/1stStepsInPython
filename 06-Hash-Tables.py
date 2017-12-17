
# coding: utf-8

# # Problem: Find a pair of numbers that add up to 10.
# 
# You are given a list / array with integers.
# 
# Example Input:  
# [3, 4, 1, 2, 9]
# 
# Write a function, pair10(input), which finds and prints out a pair (any of them) of numbers that add up to 10.

# ### NOTE: Make sure to run your program once you write it :)

# # Implement your function below.

# In[3]:


# Input: A list / array with integers.  For example:
# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".
def pair10(given_list):
    myPairs = {}
    for item in given_list:
        sum = 10 - item
        
        if sum in given_list and sum not in myPairs and item != 5:
            myPairs[item] = sum
            
    if len(myPairs) > 0:
        for key in myPairs:
            print(str(key) + ', ' + str(myPairs[key]))
    else:
        print("There is no pair that adds up to 10.")


# # Use the code below to test your function.

# In[4]:


print("""
Which pair adds up to 10? (Should print 1, 9)

[3, 4, 1, 2, 9]
""")

pair10([3, 4, 1, 2, 9])


# In[5]:


print("""
Which pair adds up to 10? (Should print -20, 30)

[-11, -20, 2, 4, 30]
""")

pair10([-11, -20, 2, 4, 30])


# In[6]:


print("""
Which pair adds up to 10? (Should print 1, 9 or 2, 8)

[1, 2, 9, 8]
""")

pair10([1, 2, 9, 8])


# In[7]:


print("""
Which pair adds up to 10? (Should print 1, 9)

[1, 1, 1, 2, 3, 9]
""")

pair10([1, 1, 1, 2, 3, 9])


# In[8]:


print("""
Which pair adds up to 10? (Should print "There is no pair that adds up to 10.")

[1, 1, 1, 2, 3, 4, 5]
""")

pair10([1, 1, 1, 2, 3, 4, 5])

