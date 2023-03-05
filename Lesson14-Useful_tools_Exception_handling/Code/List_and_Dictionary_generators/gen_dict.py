pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# с помощью цикла (классический способ):
result = {}
for pair in pairs:
    key = pair[0]
    value = pair[1]
    result[key] = value

print(f'С помощью цикла -> {result}')
result.clear()

# через генератор словаря
result = {pair[0]: pair[1] for pair in pairs}
print(f'С помощью генератора -> {result}')
