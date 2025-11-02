def print_result(func):
    def wrapper():
        result = func()  
        print(func.__name__)  
        if isinstance(result, list): #проверка, является ли result экземпляром list
            for item in result:
                print(item)
                
        elif isinstance(result, dict):  #для тест 3
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return wrapper


@print_result # декоратор расширяет функциональность функции
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
