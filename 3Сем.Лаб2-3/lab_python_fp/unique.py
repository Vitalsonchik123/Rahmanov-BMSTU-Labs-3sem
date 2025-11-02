class Unique(object):
    #передаёт в функцию переменное количество аргументов с ключевыми словами
    def __init__(self, items, **kwargs): 
        self.ignoreCase = kwargs.get('ignoreCase', False)
        self.items = items
        self.seen = set()
        self._iterator = iter(items)

    def __next__(self):
        for element in self._iterator:
            key = element
            if self.ignoreCase and isinstance(element, str):
                key = element.lower()
            if key not in self.seen:
                self.seen.add(key)
                return element
        raise StopIteration

    def __iter__(self):
        return self
# без __ не работает цикл for согласно протоколам питона
inputStr = input("Введите элементы через пробел: ")
items = inputStr.split()

ic = input("Игнорировать регистр при сравнении (да/нет, по умолчанию нет)? ").strip().lower()
ignoreCase = ic == 'да'

uniqueIter = Unique(items, ignoreCase=ignoreCase)

print("\nУникальные элементы:")
for element in uniqueIter:
    print(element)
