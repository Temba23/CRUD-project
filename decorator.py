# import json
# def password_required(func):
#     def inner(*args, **kwargs):
#         password = input("Enter the password:")
#         with open("password.json", "r") as fp:
#             data = json.load(fp)
#         if password == data['password']:
#             print("Access given.")
#             return func(*args, **kwargs)
#         else:
#             print("You dont have access.")
#     return inner

