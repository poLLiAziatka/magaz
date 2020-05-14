user_name = None
flag = True
d = {
    'магазин_1': [('продукт_1', 29, 10), ('продукт_2', 12, 12), ('продукт_3', 1234, 9), ('продукт_4', 234, 10)]
}


def main(user_name):
    print('Выбирите из следующих пунктах че вам надо:')
    print('1. Купить',
          '2. Поиск по товару',
          '3. Поиск по товарам',
          '4. Сортировка по цене товара',
          '5. Сортировка по количеству товара',
          '6. Выйти ААААА', sep='\n')
    answer = input('Введите че хотите: ')
    foolproof(['1', '2', '3', '4', '5', '6'], answer)

    if answer == '1':
        if user_name is None:
            print("Звать то Вас как?")
            user_name = input("Ваше имя:  ")
            print('Приятно (нет) познакомиться,', user_name)

        print('Какой магаз?')
        shop_name = input('Введите магаз: ')
        foolproof(shops_lst, shop_name)

        product_lst = []
        print('Какой продукт?')
        product_name = input('Введите продукт: ')
        foolproof(product_lst, product_name)

        quantity = []
        print("Сколько?")
        count = input("Введите количество: ")
        foolproof(quantity, count)
        print("А не дофига ли?")

        print("Чек нужен? Да, нет? Можете не отвечать")
        check = input('Введите ответ(можно пропустить)')
        if check.lower() == "да":
            save_check = True
        else:
            save_check = False
        user_buy(user_name, shop_name, product_name, count, save_check)

    if answer == '2':
        find_product(product_name, count=-1)

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
    pass


def load_data(file_name='data.txt', rewrite=False):
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
    pass


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