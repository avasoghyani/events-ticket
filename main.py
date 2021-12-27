import events
import filehandler
import users_admins
import csv
import login

while True:
    answer_key1 = input('you want to login or register?\nI did not register before-->> 1\n'
                        'I have already registered-->> 2\n')
    answer_key2 = input('you are admin or normal user?\nIm Admin-->> 1 \nIm normal user-->> 2\n')
    # register as admin
    if answer_key1 == '1' and answer_key2 == "1":
        admin_code = "ADMIN"
        check_admin = input('if you are admin enter security code: ')
        if check_admin == admin_code:
            admin = users_admins.get_data()
            admin.add_user('admin.csv')
            print(f"{admin.full_name} successfully registered as admin")
            login.logger.info(f'{admin.username} registered now as admin', exc_info=True)
        else:
            print('your code is wrong please try as user')
    # register in as admin
    if answer_key1 == '1' and answer_key2 == '2':
        user = users_admins.get_data()
        user.add_user('users.csv')
        print(f"{user.username} successfully registered as normal user")
        login.logger.info(f'{user.username} registered now as normal user', exc_info=True)
    # log in as admin
    if answer_key1 == '2' and answer_key2 == '1':
        users_admins.login_user('admin.csv')
        answer_key3 = input("create new event-->>1 \n show event list -->>2 \n")
        # admin create new event
        if answer_key3 == '1':
            event = events.get_data_event()
            event.add_event()
            login.logger.error(f'event {event.event_name} added ')
            print(f"{event.event_name} added successfully")
        # show event list for admin
        if answer_key3 == '2':
            filehandler.read_csv_pandas_admin('events.csv')
    # login as user
    if answer_key1 == '2' and answer_key2 == '2':
        users_admins.login_user('users.csv')
        events.Events.show_event_list()  # list of events
        # Steps to buy a ticket
        answer_key4 = int(input('which event do you want to buy? '))
        event_selected = events.Events.select_event(answer_key4)
        print(f'you choose {event_selected.event_name} and the event has {event_selected.remaining_capacity} capacity')
        while True:
            try:
                ticket_number = float(input('how many ticket do you want for?'))
                if ticket_number <= event_selected.remaining_capacity:
                    while True:
                        discount_code = input('do you have discount code? \n if yes-->enter your code \n if NO-->> 1\n')
                        if discount_code == event_selected.discount_code:  # discount is 10%
                            print(
                                f"the cost of your ticket is:{ticket_number * ((float(event_selected.ticket_fee) * 90) / 100)}")
                            break
                        elif discount_code == '1':
                            print(f"the cost of your ticket is:{ticket_number * float(event_selected.ticket_fee)}")
                            break
                        elif discount_code != event_selected.discount_code:
                            print('wrong code')

                    break
                else:
                    print('you cant choose ticket more than capacity')

            except ValueError:
                print('please enter integer number')
        answer_key5 = input('do you want to pay and buy ticket?\n yes-->>1 \n No-->>2\n')
        if answer_key5 == '1':
            print(event_selected.bay_ticket(ticket_number))
            filehandler.update_colum(answer_key4, event_selected.remaining_capacity)
            login.logger.info(f'{ticket_number} ticket of {event_selected.event_name} bought', exc_info=True)

        if answer_key5 == '2':
            continue
