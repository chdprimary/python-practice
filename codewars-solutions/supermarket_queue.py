# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to
# calculate the total time required for all the customers to check out!

# The function has two input variables:

# customers: an array (list in python) of positive integers representing the queue. 
# Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# The function should return an integer, the total time required.

# EDIT: A lot of people have been confused in the comments. To try to prevent any more confusion:

# There is only ONE queue, and
# The order of the queue NEVER changes, and
# Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.

def _remove_zeroes(list_):
    return [v for v in list_ if v != 0]

def queue_time(customers, n):
    time = 0
    customers = _remove_zeroes(customers)
    while(len(customers) > 0):
        cutoff = n if n < len(customers) else len(customers)
        for idx in range(cutoff):
            customers[idx] = customers[idx] - 1
        customers = _remove_zeroes(customers)
        time = time + 1
    return time
