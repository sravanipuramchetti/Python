str = "This is the string sentence in python"
string1 = "SubString example"
string2 = " example "

print (str[2])  # return the position
print(string1[0:5])  # return the values for 0 to 4th index
print(string2 in string1)  # substring check in str --> this returns boolean values
value = str.split("string")   # split method in python
print(value)
print(string2.strip())  # this will remove the white spaces acts like trim
print(string2.lstrip())  # this will remove the left space
print(string2.rstrip())  # this will remove the right space
