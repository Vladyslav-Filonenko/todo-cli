import json

TEXT = "Что вы хотите сделать?\n1. Добавить задачу\n2. Показать все задачи\n3. Отметить как выполненную\n4. Удалить задачу\n0. Выход\nВведите цифру в соответствии с действием которое вы хотите совершить: "


def main():
    action = int(input(TEXT))
    while action != 0:
        if action == 1:
            add_task()
        elif action == 2:
            all_tasks()
        elif action == 3:
            check_task()
        elif action == 4:
            del_task()
        action = int(input(TEXT))


def load_tasks():
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("todos.json", "w") as f:
        json.dump(tasks, f)


def add_task():
    lst = load_tasks()
    id_list = lst[-1]["id"]
    for _ in range(int(input("Сколько задач вы хотите записать: "))):
        id_list += 1
        lst.append({"id": id_list, "task": input("Введите задачу: "), "done": False})
    save_tasks(lst)
    del lst
    del id_list


def all_tasks():
    lst = load_tasks()
    for line in range(len(lst)):
        temp = lst[line]
        print(
            f'{temp["id"]}: {temp["task"]} - {"Выполнено" if temp["done"] else "Не выполнено"}'
        )
    del lst
    del temp


def check_task():
    lst = load_tasks()
    number = int(input("Введите номер задачи которую хотите выполнить: ")) - 1
    lst[number]["done"] = True
    save_tasks(lst)
    del lst
    del number


def del_task():
    lst = load_tasks()
    number = int(input("Введите номер задачи которую хотите удалить: ")) - 1
    del lst[number]
    save_tasks(lst)
    del lst
    del number


if __name__ == "__main__":
    main()
