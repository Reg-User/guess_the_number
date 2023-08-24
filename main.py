import random

def randoms():
    return random.randrange(1, 10)

def main():
    while True:
        input_text = input("Угадайте число, загаданное компьютером.\n"
                           "Введите число от 1 до 10: ")
        if int(input_text) == 0:
            print("До скорых встреч")
            break
        else:
            int_number = int(input_text)
            comp_number = randoms()
            print("Введенное число: ", int_number)
            print("Число загаданное компьютером: ", comp_number)
            if int_number == comp_number:
                print("УУУУРРРРАААА, Вы угадали")
            else:
                print("Не фортануло, не повезло")

if __name__ == '__main__':
    main()