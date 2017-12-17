
# coding: utf-8

# # Problem: Can rooks attack one another?
# 
# You are given a configuration of a chessboard with rooks in a 2 dimensional array.
# 
# Example Input:  
# [[1, 0, 0, 0],  
#  [0, 1, 0, 0],  
#  [0, 0, 0, 1],  
#  [0, 0, 0, 0]]
# 
# 1 represents that a rook is in the corresponding space on the board, and 0 represents that there's nothing there.
# 
# ***Remember, rooks are able to move horizontally and vertically over any number of spaces.***
# 
# Write a function, rooks_are_safe(input) which returns True if none of the rooks can attack each other.

# ### NOTE: Make sure to run your program once you write it :)

# # Implement your function below.

# In[19]:


# Input:
#  chessboard: A 2-dimensional array that represents.  Example below.
#  [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0]]
# Returns:
#  True if none of the rooks can attack each other.
#  False if there is at least one pair of rooks that can attack each other.
def rooks_are_safe(chessboard):
    lines = []
    columns = []
    for line in range(len(chessboard)):
        for column in range(len(chessboard[line])):
            if(chessboard[line][column] == 1):
                if(line not in lines):
                    lines.append(line)
                else:
                    return False
                if(column not in columns):
                    columns.append(column)
                else:
                    return False
    return True


# # Use the code below to test your function.

# In[20]:


print("""
Are rooks safe in this board? (Should be True.)
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 0, 0]]
""")

rooks_are_safe(
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 0, 0]])


# In[21]:


print("""
Are rooks safe in this board? (Should be True.)
[[1]]
""")

rooks_are_safe([[1]])


# In[22]:


print("""
Are rooks safe in this board? (Should be False.)
[[1, 0],
 [1, 0]]
""")

rooks_are_safe(
[[1, 0],
 [1, 0]])


# In[23]:


print("""
Are rooks safe in this board? (Should be False.)
[[0, 0, 0],
 [1, 0, 1],
 [0, 0, 0]]
""")

rooks_are_safe(
[[0, 0, 0],
 [1, 0, 1],
 [0, 0, 0]])

