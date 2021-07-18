user_name = input("Please, a user name enter : ").title()
users = {
    "Emma": "1234",
    "Jack": "5678",
    "Amy": "9982",
    "Joseph": "W@12"
}
 
if user_name in users :
    print("Hello, {}! The password is : {}".format(user_name, users[user_name]))
else :
    print("Hello, {}! See you later.".format(user_name))