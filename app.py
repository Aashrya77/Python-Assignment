from authentication import loginUser

with open("Files/welcome.txt", 'r', encoding='utf-8') as file:
    print(file.read())



loginUser()
