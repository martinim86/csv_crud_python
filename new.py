from db import DataBase

list_actions = ['add', 'edit', 'delete']

def start():
    print("Введите наименование файла и действие")
    file_name, action = input(), input()
    if action in list_actions:
        print("Введите товар и цену")
        name, price = input(), input()
        db = DataBase(name, price)
        if action == "add":
            if name in db.filter():
                print("Продукт уже есть в списке, введите edit")
                exit()
            else:
                db.add_prod()
                print("Продукт добавлен")
                exit()
        elif action == "edit":
            if name in db.filter():
                db.edit_prod(name, price)
            else:
                print("Такого продукта нет в списке, нечего редактировать")
                exit()
        elif action == "delete":
            if name in db.filter():
                db.delete_prod(name)
            else:
                print("Такого продукта нет в списке, нечего удалять")
                exit()

    else:
        exit()


if __name__ == "__main__":
    start()




