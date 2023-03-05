# слово -> СлОвО

word = 'Какое-то слово'

# условный оператор
result_if = []
for i in range(len(word)):
    char = word[i]
    if i % 2 == 0:
        result_if.append(char.upper())
    else:
        result_if.append(char.lower())

result_if = ''.join(result_if)
print(result_if)


# Тернарный оператор
result_ter = []
for i in range(len(word)):
    char = word[i]
    result_ter.append(char.upper() if i % 2 == 0 else char.lower())

result_ter = ''.join(result_ter)
print(result_ter)