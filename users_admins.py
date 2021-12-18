import filehandler
import hashlib


class User:
    def __init__(self, full_name, email, mobile, username, password):
        self.full_name = full_name
        self.email = email
        self.mobile = mobile
        self.username = username
        self.password = password

    def __str__(self):
        return f"username {self.username} created"


class Admin(User):
    def __init__(self, full_name, email, mobile, username, password):
        User.__init__(self,full_name, email, mobile, username, password)


def get_data_create_user():
    full_name = input('please enter you name and last name: ')
    email = input('please enter your email address: ')
    mobile = input('please enter your mobile number: ')
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    hash_object = hashlib.md5(password.encode())
    hash_pass = hash_object.hexdigest()
    user = User(full_name, email, mobile, username, password)
    filehandler.File('users.csv').write(
        {'full name': full_name, 'email': email, 'mobile': mobile, 'username': username, 'password': hash_pass, })
    return user


def get_data_create_admin():
    full_name = input('please enter you name and last name: ')
    email = input('please enter your email address: ')
    mobile = input('please enter your mobile number: ')
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    hash_object = hashlib.md5(password.encode())
    hash_pass = hash_object.hexdigest()
    admin = Admin(full_name, email, mobile, username, password)
    filehandler.File('admins.csv').write(
        {'full name': full_name, 'email': email, 'mobile': mobile, 'username': username, 'password': hash_pass, })
    return admin
