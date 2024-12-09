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

        try:
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
                    print("no input data")
            elif choice == '4':
                if result:
                    display_result(result)
                else:
                    print("algorithm failed")
            elif choice == '5':
                print("program completed")
                break
            else:
                print("invalid input")
        except Exception as e:
            print(f"Warning: {e}")

if name == "__main__":
    main()