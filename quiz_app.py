# file name quiz_app.py
name = input("what is your name? ")
print("Hello", name)

# file name
# name = input("what is your name? ")
# print("Hello!", name)

total_point = 0
print("Let's start!!!")
question = input ("A for? ")
if question.lower() == "apple":
   total_point = total_point + 1
   print('correct')
else:
    print('incorrect')

question = input("20 - 10? ")
total_point = total_point + 1
if question == "10":
    print('correct')
else:
    print('incorrect')

question = input("15 + 5? ")
total_point = total_point + 1
if question == "20":
    print('correct')
else:
    print('incorrect')

question = input("5 * 5? ")
total_point = total_point + 1
if question == "25":
    print('correct')
else:
    print('incorrect')

question = input("1 + 2? ")
total_point = total_point + 1
if question == "3":
    print('correct')
else:
    print('incorrect')

question = input("3 + 3? ")
total_point = total_point + 1
if question == "6":
    print('correct')
else:
    print('incorrect')

print(f"your total point is: {int(total_point/6*100)}%")




