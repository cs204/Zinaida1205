def main():
    greeting = input("Приветствие: ")
    greeting = greeting.lower().strip()  # Приводим к нижнему регистру и убираем пробелы

    if greeting.startswith("здравствуйте"):
        print("$0")
    elif greeting.startswith("з"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
