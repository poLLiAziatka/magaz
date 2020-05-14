import datetime

user_name = None
flag = True
d = {
    'магазин_1': [['продукт_1', 29, 10], ['продукт_2', 12, 12], ['продукт_3', 1234, 9], ['продукт_4', 234, 10]]
}


def main(user_name):
    print('Выбирите из следующих пунктах че вам надо:')
    print('1. Купить',
          '2. Поиск по товару',
          '3. Поиск по товарам',
          '4. Сортировка по цене товара',
          '5. Сортировка по количеству товара',
          '6. Выйти ААААА', sep='\n')
    answer = foolproof(['1', '2', '3', '4', '5', '6'], input('Введите че хотите: '))

    if answer == '1':
        if user_name is None:
            print("Звать то Вас как?")
            user_name = input("Ваше имя:  ")
            print('Приятно (нет) познакомиться,', user_name)

        print('Какой магаз?')
        print(*d.keys(), sep=', ')
        shop_name = foolproof(d.keys(), input('Введите магаз: '))

        product_lst = [prod[0] for prod in [p for p in d[shop_name]]]
        print('Какой продукт?')
        print(*product_lst, sep=', ')
        product_name = foolproof(product_lst, input('Введите продукт: '))

        for i in d[shop_name]:
            if i[0] == product_name:
                quantity = i[2]
                break

        print("Сколько?")
        print(quantity)
        count = input("Введите количество: ")
        # вот эту пакость нужно нужно незабыть переделать
        while not count.isdigit():
            print('Нам кажется, что вы дурак, попробуйте снова')
            count = input('Место для нормального ответа: ')
            if count.isdigit():
                if int(count) > quantity:
                    print('Нам кажется, что вы дурак, попробуйте снова')
                    count = input('Место для нормального ответа: ')
                print("А не дофига ли?")

        print("Чек нужен? Да, нет? Можете не отвечать")
        check = input('Введите ответ(можно пропустить)')
        if check.lower() == "да":
            save_check = True
        else:
            save_check = False
        user_buy(user_name, shop_name, product_name, count, save_check)

    if answer == '2':
        pass

    if answer == '3':
        pass

    if answer == '4':
        pass

    if answer == '5':
        pass

    if answer == '6':
        print('Не возвращайтесь')
        return False


def user_buy(user_name, shop_name, product_name, count, save_check=False):
    for i in d[shop_name]:
        if i[0] == product_name:
            product_price = i[1]
            i[2] -= int(count)
            if i[2] == 0:
                del i
            print('Покупка совершена')
        if save_check:
            with open(f'{user_name}_{datetime.date()}_{datetime.time()}', "r", encoding='utf-8') as file:
                file.write(f'''
ПОКУПАТЕЛЬ: {user_name}
МАГАЗИН: {shop_name}
ПРОДУКТ: {product_name}
ЦЕНА ЗА ШТ: {product_price}
КОЛ_ВО: {count}
НДС 100500%
ИТОГО {float(product_price) * count}
''')


def load_data(file_name='data', rewrite=False):
    global d
    if rewrite:
        d = dict
        data = []
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                data.append(line.split(':'))
            for i in data:
                d = {date[0]: date[1] for date in data}

        file.close()
        print(d)
    else:
        data = []
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                data.append(line.split(':'))
                # d.update[data]
        file.close()


def save_changes(file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for line in d.items():
            file.write(f'{line[0]}: {line[1]}' + '\n')


def foolproof(lst, ans):
    while not ans in lst:
        print('Нам кажется, что вы дурак, попробуйте снова')
        ans = input('Место для нормального ответа: ')
    return ans


def find_product(product_name, count=-1):
    pass


def find_products(products):
    pass


def sort_shops_by_product_price(product):
    pass


def sort_shops_by_product_count(product):
    pass


print('Добро пожаловать в сеть магазинов "КакойБлинМагазЗаколебалаИнфа" "Продавщица тетя Дуся"')

load_data()
while flag:
    flag = main(user_name)

