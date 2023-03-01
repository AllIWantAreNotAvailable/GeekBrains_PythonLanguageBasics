super_hero = 'Superman'
hero = 'Batman'

if super_hero.find('man') != -1:
    print('Есть')
else:
    print('Нету')

if 'man' in hero:
    print('Есть')
else:
    print('Нету')

goals = ['Стать гуру языка Python', 'Здоровье', 'накормить кота']

if 'Здоровье' in goals:
    print('"Здоровье" есть в целях')