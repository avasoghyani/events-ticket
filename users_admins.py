import filehandler
import hashlib
import login
import pandas as pd


class User:
    def __init__(self, full_name, email, mobile, username, password):
        self.full_name = full_name
        self.email = email
        self.mobile = mobile
        self.username = username
        self.password = password

    def __str__(self):
        return f"username {self.username} created"

    def add_user(self, file):
        filehandler.File(file).write(
            {'full name': self.full_name, 'email': self.email, 'mobile': self.mobile, 'username': self.username,
             'password': self.password})

    def user_login(self, file):
        self.username = input('please enter your username: ')
        df = pd.read_csv(file, sep=",")

        if df.loc['username'] == self.username:
            for i in range(3):
                self.password = input('please enter your password: ')
                if df.loc['password'] == self.password:
                    print(f'well come {self.username}')
                    break
                if df.loc['password'] != self.password:
                    print('your password is wrong')
                if df.loc['password'] != self.password and i == 2:
                    print('you enter more than 3time wrong password so your account is block!')
                    login.logger.error(
                        f"admin by username {self.username} enter 3 time wrong password and account block")
        else:
            print('username is not fond')


class Admin(User):
    def __init__(self, full_name, email, mobile, username, password):
        User.__init__(self, full_name, email, mobile, username, password)


def get_data():
    full_name = input('please enter your name and last name: ')
    email = input('please enter your email address: ')
    mobile = input('please enter your mobile number: ')
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    hash_object = hashlib.md5(password.encode())
    password = hash_object.hexdigest()
    user = User(full_name, email, mobile, username, password)
    return user


def login_user(file):
    username = input('please enter your username: ')
    username_value = filehandler.File(file)
    if username_value.check_username(username):
        for i in range(3):
            password = input('please enter your password: ')
            hash_object = hashlib.md5(password.encode())
            hash_pass = hash_object.hexdigest()
            pass_value = filehandler.File(file)
            if pass_value.check_pass(hash_pass):
                print(f'well come {username}')
                break
            if pass_value.check_pass(hash_pass) != True:
                print('your password is wrong')
            if pass_value.check_pass(hash_pass) != True and i == 2:
                print('you enter more than 3time wrong password so your account is block!')
                login.logger.error(f'admin by username {username} enter 3 time wrong password and account block')
                return login_user(file)
    else:
        print('username is not fond')
        return login_user(file)
