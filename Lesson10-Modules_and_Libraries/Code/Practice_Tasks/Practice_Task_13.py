# Практическое задание №3:
# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.

# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.

from Practice_Task_11 import make_dirs_list, make_dirs, remove_dirs
from Practice_Task_12 import get_rand_list_elem

# make_dirs(make_dirs_list())
remove_dirs(make_dirs_list())
print(get_rand_list_elem([1, 2, 3, 4, 5]))
