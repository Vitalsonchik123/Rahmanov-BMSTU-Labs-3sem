import random

def genRand(numCount, begin, end):
    for a in range(numCount):
        yield random.randint(begin, end)

while True:
    userInput = input("Введите 'стоп' для выхода или нажмите Enter для продолжения: ")

    if userInput.lower() == "стоп":
        break  

    try:
        numCount = int(input("Введите количество чисел для генерации: "))
        begin = int(input("Введите минимальное значение диапазона: "))
        end = int(input("Введите максимальное значение диапазона: "))
    except ValueError:
        print("Ошибка: ввод должен быть числом. Попробуйте снова.")
        continue  

    if begin > end:
        print("Ошибка: минимальное значение больше максимального.")
        continue  
    print("\n")
    print(f"Генерация {numCount} случайных чисел в диапазоне от {begin} до {end}:")#f - чтобы {} работало
    
    ord = 1
    for number in genRand(numCount, begin, end):
        print(f"{ord} - {number}")
        ord += 1


