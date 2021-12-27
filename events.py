import filehandler
import csv
import pandas as pd


class Events:
    def __init__(self, event_name, time_of_event, place_of_event, total_capacity, remaining_capacity, ticket_type,
                 ticket_fee, discount_code):
        self.event_name = event_name
        self.time_of_event = time_of_event
        self.place_of_event = place_of_event
        self.total_capacity = total_capacity
        self.remaining_capacity = float(remaining_capacity)
        self.ticket_type = ticket_type
        self.ticket_fee = ticket_fee
        self.discount_code = discount_code

    def add_event(self):
        filehandler.File('events.csv').write(
            {'event name': self.event_name, 'time of event': self.time_of_event, 'place of event': self.place_of_event,
             'total capacity': self.total_capacity, 'remaining capacity': self.remaining_capacity,
             'ticket type': self.ticket_type, 'ticket fee': self.ticket_fee, 'discount code': self.discount_code})

    def bay_ticket(self, ticket_number):
        self.remaining_capacity -= ticket_number
        return f'you buy {ticket_number} ticket of {self.event_name}'

    @classmethod
    def select_event(cls, event_num):
        event_selected = filehandler.select_row_object(event_num, 'events.csv')
        return event_selected

    def __str__(self):
        return f"{self.event_name} occure at {self.time_of_event} in {self.place_of_event} the capacity is" \
               f" {self.total_capacity} and remain capacity is{self.remaining_capacity} and ticket cost is" \
               f" {self.ticket_fee}"

    @staticmethod
    def show_event_list():
        print('List of available events:')
        filehandler.read_csv_pandas_user('events.csv')


def get_data_event():
    event_name = input('what is the event name: ')
    time_of_event = input('enter time of event: ')
    place_of_event = input('enter the event place: ')
    total_capacity = float(input('enter the total capacity: '))
    remaining_capacity = float(input('enter the remain capacity: '))
    ticket_type = input('enter the ticket type: ')
    ticket_fee = float(input('entet the ticket fee: '))
    discount_code = input('enter the discount code: ')
    event = Events(event_name, time_of_event, place_of_event, total_capacity, remaining_capacity, ticket_type,
                   ticket_fee, discount_code)
    return event
