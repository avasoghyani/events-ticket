import filehandler
import csv


class Events:
    def __init__(self, event_name, time_of_event, place_of_event, total_capacity, remaining_capacity, ticket_type,
                 ticket_fee,
                 discount_code):
        self.event_name = event_name
        self.time_of_event = time_of_event
        self.place_of_event = place_of_event
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.ticket_type = ticket_type
        self.ticket_fee = ticket_fee
        self.discount_code = discount_code

    def add_event(self):
        print('event added')

    def bay_ticket(self, event):
        print(f'you buy this {self.event_name}')

    def __str__(self):
        return f"{self.event_name} occure at {self.time_of_event} in {self.place_of_event} the capacity is {self.total_capacity}" \
               f" and remain capacity is{self.remaining_capacity} and ticket cost is {self.ticket_fee}"


list_events = []


def print_events():
    for i, event in enumerate(list_events):
        print(f'{i + 1}:  {event}')


def get_data():
    event_name = input('what is the event name: ')
    time_of_event = input('enter time of event: ')
    place_of_event = input('enter the event place: ')
    total_capacity = int(input('enter the total capacity: '))
    remaining_capacity = int(input('enter the remain capacity: '))
    ticket_type = input('enter the ticket type: ')
    ticket_fee = int(input('entet the ticket fee: '))
    discount_code = input('enter the discount code: ')
    event = Events(event_name, time_of_event, place_of_event, total_capacity, remaining_capacity, ticket_type,
                   ticket_fee, discount_code)
    filehandler.File('events.csv').write({'event name': event_name, 'time of event': time_of_event, 'place of event':
        place_of_event, 'total capacity': total_capacity, 'remaining capacity': remaining_capacity, 'ticket type':
                                              ticket_type, 'ticket fee': ticket_fee, 'discount code': discount_code})
    return event
