#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = [None] * length

    for ticket in tickets:
        # if source is none, set route[0], it is the beggining
        if ticket.source == "NONE":
            route[0] = ticket.destination
        # else put sources in cache
        if ticket not in cache:
            cache[ticket.source] = ticket.destination


    for e in range(length):
        # if the current e in route is None, look for the prev destination as the key in cache and set as route
        if route[e] is None:
            route[e] = cache[route[e - 1]]

    return route

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# print(reconstruct_trip(tickets, 3))