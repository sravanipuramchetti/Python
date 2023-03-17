# lists in python
value = [22, 85, "python", 3.5, 89, 90, "udemy"]  # --> in python array will accept all kind of data types
print(value[0]) # out put is 22
print(value[2:4])  #  output will start from 2nd index and it exclueds the 4th index
value.insert(3, "sylabus")  # inserting a new value in to list at run time
print(value)
value.append("End") # this will get appended at the end of the list
print(value)
value[2] = "PYTHON" # updating th list
print(value)
print(value[-1]) # this will return the last index of list
del value[0]
print(value)

# Tuples in python same as List but its immutable

val = (1, 2, 3, "sravani", 8.9)
print(val[1])
# val[2] = "testing"  # This is not possible in tuple value assigning at run time
print(val)

# Dictionaries in python

dic = {1: 345, 4: "grapes", 7: "orange"}
print(dic[4])

# create a empty dict and insert the values at run time.
dict = {}
dict["firstname"] = "automation"
dict["lastname"] = "testing"
dict["Active"] = "yes"
print(dict)
print(dict.keys())

