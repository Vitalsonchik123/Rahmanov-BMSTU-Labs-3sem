def field(items, *args):
    assert len(args) > 0     #если ложно, то остановит программу
    for item in items:
        if len(args) == 1:
            key = args[0]
            value = item.get(key)
            if value is not None:
                yield value    #yield возвращает значение по одному
        else:               #если больше 1 аргумента
            result = {}
            all_none = True
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value
                    all_none = False
            if not all_none:
                yield result

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}, #без цены
    {'title': 'Стул', 'price': 1500 }, #без цвета 
    {'title': None, 'price': 1000, 'color': 'red'}, #без названия
]

print("field(goods, 'title'):")
for value in field(goods, 'title'):
    print(value)

print("\n")

print("field(goods, 'title', 'price'):")
for d in field(goods, 'title', 'price', 'color'):
    print(d)
