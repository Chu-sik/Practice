# question 5 - python1 day3

votes_pizza = int(input('Votes for pizza: '))
votes_chicken = int(input('Votes for chicken: '))
votes_burger = int(input('Votes for burger: '))

votes_total = votes_pizza + votes_chicken\
	+ votes_burger
percent_pizza = (votes_pizza / votes_total) * 100
percent_chicken = (votes_chicken / votes_total) * 100
percent_burger = (votes_burger / votes_total) * 100

print('-' * 24)
print(f'{"MENU":>10}{"VOTE":>6}{"(%)":>8}')
print('-' * 24)
print(f'{"PIZZA":>10}{votes_pizza:>6}{percent_pizza:>8.1f}')
print(f'{"CHICKEN":>10}{votes_chicken:>6}{percent_chicken:>8.1f}')
print(f'{"MENU":>10}{votes_burger:>6}{percent_burger:>8.1f}')
