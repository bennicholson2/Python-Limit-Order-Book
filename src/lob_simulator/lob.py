import enum
from dataclasses import dataclass  

class Side(enum.Enum):
    BUY = 1
    SELL = 2

@dataclass
class Order:
    order_id: str
    side: Side
    price: float
    quantity: int

class OrderBook:
    def __init__(self):
    # in the orderbook we have a two side heapq where people can join and leave at either side
    # it needs to be time and price dependent
        buyers_queue = []
        sellers_queue = []

    def 


######### below is the test ########

list_orders = []
num_orders = 10

import numpy as np
side = np.random.binomial(1, 0.5, num_orders)
quantity = np.random.uniform(1,10,num_orders)
price = np.random.uniform(50,100,num_orders)

for i in range(num_orders):
    order = Order(order_id = i, side = (1 if side[i] > 0.5 else 0), price = price[i], quantity = quantity[i])
    list_orders.append(order)
    print(order)
    print(f'\n')

print(list_orders)