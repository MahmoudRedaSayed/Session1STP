from data import usernames,passwords,secret
# #remon
# for i in usernames:#Ahmed Sara Mahmoud
#     if Name == i:
#         if passwords[counter]==password:
#             print("your data is correct")
#             break
#     else:
#         counter+=1
# #Reem
# for i in usernames:
#     if Name == i:
#         for j in passwords:
#             if  password ==j:
#                 print("your data is correct")
# if Name in usernames :
#     if password in passwords:
#         print("your data is correct")
#anothor sol
Name=input("Enter your name: ")
password=input ("Enter your pass : ")
for i in range(len(usernames)):
    if Name==usernames[i]:
        if password==passwords[i]:
            print("your data is correct")
        else:
            print('your password is not')
