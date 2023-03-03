import random


# 1. Загадать случайное число от 0 до 100:
l_bound = 0
u_bound = 100
print(f'1. Загадать случайное число от {l_bound} до {u_bound}:\n{random.randint(l_bound, u_bound)}')

# 2. Выбрать победителя лотереи из списка players:
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(f'2. Выбрать победителя лотереи из списка {players}:\nПобедитель -> {random.choice(players)}')

# 3. Выбрать 3-х победителей лотереи из списка players:
print(f'3. Выбрать 3-х победителей лотереи из списка {players}:\nПобедители: {random.sample(players, 3)}')

# 4. Перемешать карты в колоде (списке) cards:
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(f'4. Перемешать карты в колоде (списке) {cards}:')
random.shuffle(cards)
print(cards)
