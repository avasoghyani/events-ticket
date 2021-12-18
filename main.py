import events
import filehandler
import users_admins
import csv
import login

events_list = []
answer_key1 = input('you want to login or register?\nI did not register before-->> 1\nI have already registered-->>'
                    ' 2\n')
answer_key2 = input('you are admin or normal user?\nIm Admin-->> 1 \nIm normal user-->> 2\n')
if answer_key1 == '1' and answer_key2 == "1":
    admin = users_admins.get_data_create_admin()
    print(f"{admin.username} successfully registered az admin")
    login.logger.info(f'{admin.username} registered now az admin', exc_info=True)
if answer_key1 == '1' and answer_key2 == '2':
    user = users_admins.get_data_create_user()
    print(f"{user.username} successfully registered az normal user")
    login.logger.info(f'{user.username} registered now az normal user', exc_info=True)
if answer_key1 == '2' and answer_key2 == '1':
    i = 0
    while i < 3:
        user_name = input('please enter your username: ')
        pass_word = input('please enter your password: ')
        hash_object = hashlib.md5(pass_word.encode())
        hash_pass = hash_object.hexdigest()
        value = filehandler.File('admin.csv')
        if value.find_row(user_name, hash_pass) != True:
            if i != 2:
                print('your password or username is wrong')
                i += 1
            elif i == 2:
                print('you enter more than 3time wrong password so your account is block!')
                login.logger.error(f'admin by username {user_name} enter 3 time wrong password and account block')

                break
        else:
            event1 = events.get_data()
            print("you create new event")
            events_list.append(event1)
            break

if answer_key1 == '2' and answer_key2 == '2':
    i = 0
    while i < 3:
        user_name = input('please enter your username: ')
        pass_word = input('please enter your password: ')
        hash_object = hashlib.md5(pass_word.encode())
        hash_pass = hash_object.hexdigest()
        value = filehandler.File('users.csv')
        if value.find_row(user_name, hash_pass) != True:
            if i != 2:
                print('your password or username is wrong')
                i += 1
            elif i == 2:
                login.logger.error(f'user by username {user_name} enter 3 time wrong password and account block')
                print('you enter more than 3time wrong password so your account is block!')
                break
        else:
            filehandler.File('events.csv').show_row_of_event()
            answer_key3 = int(input('what event do you want to choose? '))
            selected_event = filehandler.File('events.csv').select_special_row(answer_key3)
            print(f" you choose {selected_event['event name']} event , and it happen at"
                  f"{selected_event['time of event']} in {selected_event['place of event']} ")
            ticket_number = int(input("how many ticket do you want? "))
            a = int(selected_event['remaining capacity'])
            a -= ticket_number
            selected_event['remaining capacity'] = a
        #     with open('events.csv', 'a', newline='') as file:
        #         fields = list(selected_event.keys())
        #         writer = csv.DictWriter(file, fieldnames=fields)
        #         for row in writer:
        #             if row['event name'] == selected_event['event name']:
        #                 row['remain capacity'] = a
        # # filehandler.File('events.csv').edit_row(selected_event)
