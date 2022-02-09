##the data 
usernames = ["Ahmed", "Sara", "Mahmoud"]
passwords = ["1234", "5432", "1412"]
secret = ["Dont like tea", "Can sing", "Speak Chinese"]
################################################
Name=input("Enter the name :: ")
Password=input("Enter the password : ")
index=0
for i in usernames:# Ahmed Sara Mahmoud
    if i == Name:
        break
    else:
        index=index+1
if index == len(usernames):
    print("your name is not correct")
else:
    if passwords[index] == Password:
        print(secret[index])
    else:
        print("the password is not correct")



