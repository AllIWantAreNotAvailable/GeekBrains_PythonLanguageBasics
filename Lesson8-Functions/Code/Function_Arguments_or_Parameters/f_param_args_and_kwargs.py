def greeting(*args, say: str = 'Hello'):
    print(say, args)


def get_person(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def main():
    greeting('Kate', 'Max', 'Ron', 'Leo', say='Hi, my friends:')
    get_person(name='Leo', age=20, has_car=True)


if __name__ == '__main__':
    main()
