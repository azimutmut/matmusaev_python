data = input("Enter number or name: ")
name1 = 'John'
numb = 7
try:
    if int(data) > numb:
        print("Hello")
    else:
        print("The number should be greater than 7")
except:
    if data == name1:
        print("Hello, ", data)
    else:
        print("There is no such name")
