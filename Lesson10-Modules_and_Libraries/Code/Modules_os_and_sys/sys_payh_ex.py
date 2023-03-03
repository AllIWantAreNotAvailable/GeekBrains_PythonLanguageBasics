# Мы можем импортировать
import math
import sys

# Но не можем импортировать Наш модуль из другой директории

# Как Python находит модули?
import sys

print(sys.path)
print(type(sys.path))

sys.path.append('/Users/unknownman/Library/CloudStorage/OneDrive-Личная/GeekBrains/Python_Language_Basics/Lesson8-Functions/Code/Areas_of_visibility/')
for path in sys.path:
    print(path)

import many_funcs
