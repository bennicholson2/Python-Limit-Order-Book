# Design of Limit Order Book (Python)

I want to create an event based simulator

We are going to start really basic

## Participants

Zero intelligence traders are an object and we create instances of them - each ZI Trader gets their own side, arrival time and price belief 

### Side
Side is determined by a binomial distribution

### Price
Price is determined by a uniform distribution around some overall agreed upon price

### Time of arrival
Exponential Distribution 

## Limit Order Book
Queues are ordered by price and time priority this is done with a deque which is a double ended queue. This allows both entry and exit at both ends of the queue,

To begin we will just use a normal queue where people cannot leave at the end of the queue 

## Trades

The partipcpants come to the Limit Order Book and are sorted by a price time priority queue. Then trades are made with the following configurations

- A new buyer comes in which has a price that is higher than the highest selling point 
- A new seller comes in which has a price that is lower than the highest buying point

## Metrics

- Time in between trades
- Spread
- Buyer queue
- Seller queue 
