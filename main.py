import re

def input_data():
    return "input data"

def generate_data():
    return "Generated data"

def process_data(data):
    return "Processed result"

def display_result(result):
    print("Result:", result)

def main():
    data = None
    result = None

    while True:
        print("\nМеню:")
        print("1. Ввод данных вручную")
        print("2. Генерация случайных данных")
        print("3. Выполнение алгоритма")
        print("4. Вывод результата")
        print("5. Завершение работы")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            data = input_data()
            result = None  # Сброс результата
        elif choice == '2':
            data = generate_data()
            result = None  # Сброс результата
        elif choice == '3':
            if data:
                result = process_data(data)
            else:
                print("no entered data")
        elif choice == '4':
            if result:
                display_result(result)
            else:
                print("algorithm failed")
        elif choice == '5':
            print("Completed")
            break
        else:
            print("Wrong choice")

if name == "__main__":
    main()