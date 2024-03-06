import queue
import time
import random


class Ticket:
    def __init__(self, ticket_number, timestamp):
        self.ticket_number = ticket_number
        self.timestamp = timestamp

def generate_ticket(num_tickets, ticketing_queue):
    for i in range(num_tickets):
        cur_ts = time.time()
        cur_ticket = Ticket(ticket_number=i, timestamp=cur_ts)
        print(f"ticket number {i}, timestamp: {cur_ts}")
        ticketing_queue.put(cur_ticket)
        time.sleep(random.uniform(1, 3))

def process_tickets(ticketing_queue):
    while not ticketing_queue.empty():
        cur_ticket = ticketing_queue.get()

        print(f"process number {cur_ticket.ticket_number}, timestamp: {cur_ticket.timestamp}")
        time.sleep(random.uniform(1, 3))

def main():
    #simulate ticket system
    ticketing_queue = queue.Queue()

    generate_ticket(num_tickets=5, ticketing_queue=ticketing_queue)
    process_tickets(ticketing_queue=ticketing_queue)
    



main()