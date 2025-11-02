import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент уравнения
    '''
    try:
        coef_str = sys.argv[index]
    except IndexError:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения a*x^2 + b*x + c = 0

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней (может быть пустым)
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root) 
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.extend([root1, root2])
    return result


def main():
    '''
    Основная функция для решения биквадратного уравнения A*x^4 + B*x^2 + C = 0
    Цикл продолжается до ввода "стоп" вместо коэффициента
    '''
    while True:
        print('Если желаете закончить работу с программой, введите "стоп"')
        def inputOrStop(index, prompt):
            try:
                coef_str = sys.argv[index] 
                return float(coef_str), False
            except IndexError:
                print(prompt)
                coef_str = input().strip() 
                if coef_str.lower() == 'стоп':
                    return None, True
                return float(coef_str), False

        a, stop = inputOrStop(1, 'Введите коэффициент A:')
        if stop:
            break
        b, stop = inputOrStop(2, 'Введите коэффициент B:')
        if stop:
            break
        c, stop = inputOrStop(3, 'Введите коэффициент C:')
        if stop:
            break

        if a == 0.0:
            if b == 0.0:
                if c == 0.0:
                    print('Бесконечно много корней (тождество 0=0)')
                else:
                    print('Корней нет')
                continue

            y = -c / b
            roots = []
            if y > 0:
                roots.append(math.sqrt(y))
                roots.append(-math.sqrt(y))
            elif y == 0:
                roots.append(0.0)
        else:
            y_roots = get_roots(a, b, c)
            roots = []
            for y in y_roots:
                if y > 0:
                    roots.append(math.sqrt(y))
                    roots.append(-math.sqrt(y)) 
                elif y == 0:
                    roots.append(0.0)

        if len(roots) == 0:
            print("Нет действительных корней")
        else:
            roots = sorted(set(roots))
            if len(roots) == 1:
                print(f"Один корень: {roots[0]}")
            else:
                print("Корни:", ", ".join(str(r) for r in roots))


if __name__ == "__main__":
    main()
