contacts = {}

while True:
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Редактировать контакт")
    print("4. Поиск по имени")
    print("5. Список контактов")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя контакта: ")
        phone_numbers = input("Введите номер(а) телефона : ").split()

        if name in contacts:
            contacts[name].update(phone_numbers)
        else:
            contacts[name] = set(phone_numbers)

        print("Контакт успешно добавлен.")

    elif choice == "2":
        name = input("Введите имя контакта, которого нужно удалить: ")

        if name in contacts:
            del contacts[name]
            print("Контакт успешно удален.")
        else:
            print("Контакт не найден.")

    elif choice == "3":
        name = input("Введите имя контакта, которого нужно отредактировать: ")

        if name in contacts:
            phone_numbers = input("Введите новый номер(а) телефона : ").split()
            contacts[name] = set(phone_numbers)
            print("Контакт успешно отредактирован.")
        else:
            print("Контакт не найден.")

    elif choice == "4":
        name = input("Введите имя контакта для поиска: ")

        if name in contacts:
            print("Имя контакта:", name)
            print("Номер(а) телефона:", contacts[name])
        else:
            print("Контакт не найден.")

    elif choice == "5":
        print("Список контактов:")
        if not contacts:
            print("Контактов нет.")
        else:
            for name, phone_numbers in contacts.items():
                print("Имя контакта:", name)
                print("Номер(а) телефона:", phone_numbers)
                print("----------------------")


        contacts["Иван"] = {"+380991234567"}
        contacts["Мария"] = {"+380991111111", "+380992222222"}
        contacts["Алексей"] = {"+380993333333"}
        contacts["Елена"] = {"+380994444444"}
        contacts["Андрей"] = {"+380995555555"}
        contacts["Ольга"] = {"+380996666666"}
        contacts["Николай"] = {"+380997777777"}
        contacts["Светлана"] = {"+380998888888"}
        contacts["Петр"] = {"+380999999999"}
        contacts["Анна"] = {"+380990000000"}

    elif choice == "6":
        break

    else:
        print("Некорректный выбор. Попробуйте еще раз.")
