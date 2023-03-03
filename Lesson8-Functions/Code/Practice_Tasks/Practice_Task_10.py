# Практическое задание №4:
# Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон
# по формуле:

# damage = damage / armor

# Следовательно, у вас должно быть 2 функции:
# 1) Наносит урон. Это улучшенная версия функции из задачи 3.
# 2) Вычисляет урон по отношению к броне.

# Примечание: Функция номер 2 используется внутри функции номер 1 для вычисления урона
# вычитания его из здоровья персонажа.


import random


def damage_calculation(damage: int, armor: float):
    return damage / armor


def take_damage(damage: float, health: int) -> int:
    return int(health - damage)


def fight(*args) -> dict:
    for i in range(100):
        if i % 2 == 0:
            attacker = args[0]
            victim = args[1]
        else:
            attacker = args[1]
            victim = args[0]

        damage = round(damage_calculation(attacker["damage"], victim["armor"]))
        is_critical_damage = True if 70 < random.randint(0, 100) else False
        damage += round(damage // 2 if is_critical_damage else 0)

        victim["health"] = take_damage(damage=damage,
                                       health=victim["health"])
        print(f'Игрок {victim["name"]} получил(а) {damage} {"критического " if is_сritical_damage else ""}урона,')
        if victim["health"] < 1:
            print(f'этот удар был смертельным для {victim["name"]}...\n')
            return attacker
        print(f'у {victim["name"]} осталось {victim["health"]} HP!\n')


def get_player(bot: bool = False) -> dict:
    """
    Функция возвращает структуру игрока типа:\n
    - имя ("name");\n
    - здоровье ("health");\n
    - урон ("damage").\n
    :param bot: Если значение True, то возвращает случайного бота, иначе игрока.
    :return: Структуру (dict) игрока.
    """
    min_health = 100
    max_health = 300
    min_damage = 50
    max_damage = 100
    min_armor = 0
    max_armor = 50

    player = {
        "name": '',
        "health": 0,
        "damage": 0,
        "armor": 0.0
    }
    if not bot:
        player["name"] = input('Задайте имя Вашему персонажу:\n>>>')
    else:
        bot_names = ['Leo', 'Max', 'Anna', 'Alex', 'Ron', 'Kate']
        name_index = random.randint(0, len(bot_names) - 1)
        player["name"] = bot_names[name_index]

    player["health"] = random.randint(min_health, max_health)
    player["damage"] = random.randint(min_damage, max_damage)
    player["armor"] = random.randint(min_armor, max_armor) / 100 + 1

    low_health = player["health"] < 130
    show_health = 'На вид ты какой-то хилый, всего-то' if low_health else 'Да, таких здоровых еще поискать, целых'
    low_damage = player["damage"] < 55
    show_damage = 'Ты меч в руках удержать сможешь?' if low_damage else 'Интересно, твой оппонент не испугается?'
    protection_rate = int(player["armor"] * 100 - 100)

    print(f'Приветствуем тебя, {player["name"]}!\n'
          f'{show_health} {player["health"]} HP!\n'
          f'{"Модный костюмчик!" if 0 < protection_rate else "Какой срам..."} {protection_rate}% защиты.\n'
          f'{show_damage} Урон -> {player["damage"]}\n')
    return player


def main() -> None:
    """
    Программа создает 2-х игроков:\n
    - одного для пользователя;\n
    - другого для бота.\n
    Игроки сражаются пока здоровье одного из них не достигнет 0.
    :return: None
    """
    player = get_player()
    enemy = get_player(bot=True)
    winner = fight(player, enemy)
    print(f'Поздравляем с победой, {winner["name"]}!')


if __name__ == '__main__':
    main()
