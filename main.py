import events
import filehandler
import users_admins
import csv
import login

events_list = []
while True:
    answer_key1 = input('you want to login or register?\nI did not register before-->> 1\nI have already registered-->>'
                        ' 2\n')
    answer_key2 = input('you are admin or normal user?\nIm Admin-->> 1 \nIm normal user-->> 2\n')
    if answer_key1 == '1' and answer_key2 == "1":
        admin_code = "ADMIN"
        check_admin = input('if you are admin enter security code: ')
        if check_admin == admin_code:
            admin = users_admins.get_data_create_admin()
            print(f"{admin.username} successfully registered as admin")
            login.logger.info(f'{admin.username} registered now as admin', exc_info=True)
        else:
            print('your code is wrong please try as user')
    if answer_key1 == '1' and answer_key2 == '2':
        user = users_admins.get_data_create_user()
        print(f"{user.username} successfully registered as normal user")
        login.logger.info(f'{user.username} registered now as normal user', exc_info=True)
    if answer_key1 == '2' and answer_key2 == '1':
        # user.user_login()
        users_admins.login('admins.csv')
        answer_key3 = input("create new event-->>1 \n show event list -->>2 \n")
        if answer_key3 == '1':
            event = events.add_event()
            print(f"{event.event_name} added successfully")
        if answer_key3 == '2':
            filehandler.File('events.csv').show_event_for_admin()

    if answer_key1 == '2' and answer_key2 == '2':
        # user.user_login()
        users_admins.login('users.csv')
        print('List of available events:')
        events_list = events.Events.show_event_list()  # list of events
        answer_key4 = int(input('which event do you want to buy? '))
        for i in range(len(events_list)):
            if i == answer_key4:
                print(f"you choose {events_list[i]['event name']}\nremaining ticket for this event is "
                      f"{events_list[i]['remaining capacity']}")
                ticket_number = float(input('how many ticket do you want for?'))
                if ticket_number <= float(events_list[i]['remaining capacity']):
                    discount_code = input('do you have discount code? \n if yes-->enter your code \n if NO-->> 1\n')
                    if discount_code == events_list[i]['discount code']:  # discount is 10%
                        print(
                            f"the cost of your ticket is:{ticket_number * ((float(events_list[i]['ticket fee']) * 90) / 100)}")
                    elif discount_code == '1':
                        print(f"the cost of your ticket is:{ticket_number * float(events_list[i]['ticket fee'])}")
                    elif discount_code != events_list[i]['discount code']:
                        print('your code is wrong!')

                    answer_key5 = input('do you want to pay and buy ticket?\n yes-->>1 \n No-->>2\n')
                    if answer_key5 == '1':
                        events_list[i]['remaining capacity'] = float(events_list[i]['remaining capacity']) - ticket_number
                        filehandler.update_colum(i, events_list[i]['remaining capacity'])
                        print(f"you buy {events_list[i]['event name']} it occur in {events_list[i]['place of event']}"
                              f" at {events_list[i]['time of event']} ")
                        login.logger.info(f'{ticket_number} ticket buy', exc_info=True)
                else:
                    print('Capacity is complete and there is no ticket')

        # i = 0
        # while i < 3:
        #     user_name = input('please enter your username: ')
        #     pass_word = input('please enter your password: ')
        #     hash_object = hashlib.md5(pass_word.encode())
        #     hash_pass = hash_object.hexdigest()
        #     value = filehandler.File('users.csv')
        #     if value.find_row(user_name, hash_pass) != True:
        #         if i != 2:
        #             print('your password or username is wrong')
        #             i += 1
        #         elif i == 2:
        #             login.logger.error(f'user by username {user_name} enter 3 time wrong password and account block')
        #             print('you enter more than 3time wrong password so your account is block!')
        #             break
        #     else:
        #         filehandler.File('events.csv').show_row_of_event()
        #         answer_key3 = int(input('what event do you want to choose? '))
        #         selected_event = filehandler.File('events.csv').select_special_row(answer_key3)
        #         print(f" you choose {selected_event['event name']} event , and it happen at"
        #               f"{selected_event['time of event']} in {selected_event['place of event']} ")
        #         ticket_number = int(input("how many ticket do you want? "))
        #         a = int(selected_event['remaining capacity'])
        #         a -= ticket_number
        #         selected_event['remaining capacity'] = a
        #     with open('events.csv', 'a', newline='') as file:
        #         fields = list(selected_event.keys())
        #         writer = csv.DictWriter(file, fieldnames=fields)
        #         for row in writer:
        #             if row['event name'] == selected_event['event name']:
        #                 row['remain capacity'] = a
        # # filehandler.File('events.csv').edit_row(selected_event)
