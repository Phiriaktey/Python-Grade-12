my_str = "Hello World!"
print(my_str)
#remove the spaces in our string
print (my_str.strip())
# replace old word with new words sometime can also "***"
print(my_str.replace("Hello", "Bye Bye"))
# split function will split your string example e then the e will gone
print(my_str.split("e"))

#new lesson 1/24/2024

str_one = "Hello"
str_two = "World"

print(str_one +" " + str_two)
print("Hello," + str_two) 

# format string
print(f"Hello, {str_two}") 

print("Hello," + str_two + "add more string here")
print(f"{str_two} {str_two}")

# my name is name I'm here
# escape character
print('my name is name I\'m here')