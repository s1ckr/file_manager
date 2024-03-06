import os

with open("directory.txt", "r") as f:
    ROOT_DIRECTORY = f.read().strip()
    if ROOT_DIRECTORY == "":
        ROOT_DIRECTORY = os.getcwd()
    WORKING_DIRECTORY = ROOT_DIRECTORY


def create_folder(folder_name):
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Папка '{folder_name}' создана.")


def delete_folder(folder_name):
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)
    try:
        os.rmdir(folder_path)
        print(f"Папка '{folder_name}' удалена.")
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не найдена.")


def move_to_folder(folder_name):
    global WORKING_DIRECTORY
    if folder_name == "..":
        new_path = os.path.dirname(WORKING_DIRECTORY)
        if len(new_path) > len(ROOT_DIRECTORY):
            WORKING_DIRECTORY = new_path
            print("Перешли в родительскую директорию.")
        else:
            print(f"Папка '{new_path}' выше корневой.")
    else:
        new_path = os.path.join(WORKING_DIRECTORY, folder_name)
        if os.path.isdir(new_path):
            WORKING_DIRECTORY = new_path
            print(f"Спустились в папку '{folder_name}'.")
        else:
            print(f"Папка '{folder_name}' не найдена.")


def list_contents():
    print("Содержимое папки:")
    for item in os.listdir(WORKING_DIRECTORY):
        print(item)


def create_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    open(file_path, "w").close()
    print(f"Файл '{file_name}' создан.")


def write_to_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    text = input(f"Введите текст для записи в '{file_name}': ")
    with open(file_path, "w") as f:
        f.write(text)
    print(f"Текст записан в '{file_name}'.")


def view_file_contents(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    print(f"Содержимое файла '{file_name}':")
    with open(file_path, "r") as f:
        print(f.read())


def delete_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    try:
        os.remove(file_path)
        print(f"Файл '{file_name}' удалён.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")


def copy_file(source_file, destination):
    source_path = os.path.join(WORKING_DIRECTORY, source_file)
    destination_path = os.path.join(WORKING_DIRECTORY, destination)
    try:
        with open(source_path, "rb") as src, open(destination_path, "wb") as dest:
            dest.write(src.read())
        print(f"Файл '{source_file}' скопирован в '{destination}'.")
    except FileNotFoundError:
        print(f"Файл '{source_file}' не найден.")


def move_file(source_file, destination):
    source_path = os.path.join(WORKING_DIRECTORY, source_file)
    destination_path = os.path.join(WORKING_DIRECTORY, destination)
    try:
        os.rename(source_path, destination_path)
        print(f"Файл '{source_file}' перемещён в '{destination}'.")
    except FileNotFoundError:
        print(f"Файл '{source_file}' не найден.")


def rename_file(old_name, new_name):
    old_path = os.path.join(WORKING_DIRECTORY, old_name)
    new_path = os.path.join(WORKING_DIRECTORY, new_name)
    try:
        os.rename(old_path, new_path)
        print(f"Файл '{old_name}' переименован в '{new_name}'.")
    except FileNotFoundError:
        print(f"Файл '{old_name}' не найден.")


while True:
    print("\nТекущая рабочая директория:", WORKING_DIRECTORY)
    print("1. Создать папку")
    print("2. Удалить папку")
    print("3. Перемещение по папкам")
    print("4. Создать файл")
    print("5. Записать в файл")
    print("6. Показать содержимое файл")
    print("7. Удаление файла")
    print("8. Копирование файла")
    print("9. Переместить файл")
    print("10. Переименовать файл")
    print("11. Просмотр содержимого папки")
    print("12. Выход")

    choice = input("Введите число для выбора: ")

    if choice == "1":
        inp = input("Введите название папки: ")
        create_folder(inp)
    elif choice == "2":
        inp = input("Введите название папки для удаления: ")
        delete_folder(inp)
    elif choice == "3":
        inp = input("Введите название папки: ")
        move_to_folder(inp)
    elif choice == "4":
        inp = input("Введите название файла: ")
        create_file(inp)
    elif choice == "5":
        inp = input("Введите название файла: ")
        write_to_file(inp)
    elif choice == "6":
        inp = input("Введите название файла: ")
        view_file_contents(inp)
    elif choice == "7":
        inp = input("Введите название файла: ")
        delete_file(inp)
    elif choice == "8":
        source_file = input("Введите название файла: ")
        destination = input("Введите путь для копирования: ")
        copy_file(source_file, destination)
    elif choice == "9":
        source_file = input("Введите название файла: ")
        destination = input("Введите путь для перемещения: ")
        move_file(source_file, destination)
    elif choice == "10":
        old_name = input("Введите название файла: ")
        new_name = input("Введите новое название файла: ")
        rename_file(old_name, new_name)
    elif choice == "11":
        list_contents()
    elif choice == "12":
        print("Выход")
        break
    else:
        print("Нет такого варианта")
