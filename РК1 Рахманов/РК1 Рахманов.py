from dataclasses import dataclass
from typing import List

@dataclass  # класс для связи многие-ко-многим
class CDLibraryDisk:
    id: int
    libraryId: int
    diskId: int

@dataclass  # класс данных для Библиотеки CD-дисков
class CDLibrary:
    id: int
    name: str
    location: str

@dataclass  # класс данных для CD-диска
class CDDisk:
    id: int
    title: str
    artist: str
    genre: str
    price: float  # для запроса 2
    year: int

def main():
    libraries = [
        CDLibrary(1, "Главный отдел музыки", "Центральный район"),
        CDLibrary(2, "Отдел классики", "Северный район"),
        CDLibrary(3, "Рок-коллекция", "Западный район"),  #не пишем слово "отдел" для 3 запроса
        CDLibrary(4, "Джазовый отдел", "Восточный район"),
        CDLibrary(5, "Поп-музыка отдел", "Южный район")
    ]

    disks = [
        CDDisk(1, "The Dark Side of the Moon", "Pink Floyd", "Rock", 25, 1973),
        CDDisk(2, "Thriller", "Michael Jackson", "Pop", 19, 1982),
        CDDisk(3, "Kind of Blue", "Miles Davis", "Jazz", 22, 1959),
        CDDisk(4, "Symphony No. 9", "Beethoven", "Classical", 18, 1987),
        CDDisk(5, "Back in Black", "AC/DC", "Rock", 21, 1980),
        CDDisk(6, "The Wall", "Pink Floyd", "Rock", 24, 1979)
    ]

    OneToMany = [ # один диск находится в одной библиотеке
        (lib, disk) for lib in libraries 
        for disk in disks 
        if (lib.id == 1 and disk.id in [1, 2]) or  # главный отдел
           (lib.id == 2 and disk.id == 4) or       # отдел классики
           (lib.id == 3 and disk.id in [1, 5, 6]) or # рок-коллекция
           (lib.id == 4 and disk.id == 3) or       # джазовый отдел
           (lib.id == 5 and disk.id == 2)          # поп-музыка отдел
    ]

    ManyToMany = [ # связи многие-ко-многим
        CDLibraryDisk(1, 1, 1),  # Главный отдел - The Dark Side of the Moon
        CDLibraryDisk(2, 1, 2),  # Главный отдел - Thriller
        CDLibraryDisk(3, 2, 4),  # Отдел классики - Beethoven
        CDLibraryDisk(4, 3, 1),  # Рок-коллекция - The Dark Side of the Moon
        CDLibraryDisk(5, 3, 5),  # Рок-коллекция - Back in Black
        CDLibraryDisk(6, 3, 6),  # Рок-коллекция - The Wall
        CDLibraryDisk(7, 4, 3),  # Джазовый отдел - Kind of Blue
        CDLibraryDisk(8, 5, 2),  # Поп-музыка отдел - Thriller
        CDLibraryDisk(9, 1, 6),  # Главный отдел - The Wall
        CDLibraryDisk(10, 3, 1), # Рок-коллекция - The Dark Side of the Moon
    ]


    print("ЗАПРОС 1")
    print("Список всех связанных библиотек и CD-дисков (один-ко-многим), отсортированный по названиям библиотек:")
    
    sortedLibraryDisks = sorted(OneToMany, key=lambda x: x[0].name)
    
    for library, disk in sortedLibraryDisks:
        print(f"{library.name}: {disk.artist} - {disk.title}")

    print("\n")


    print("ЗАПРОС 2")
    print("Список библиотек с суммарной стоимостью CD-дисков в каждой библиотеке:")
    
    libraryCosts = {}  # группируем по библиотекам и суммируем стоимость
    for library, disk in OneToMany:
        if library.id not in libraryCosts:
            libraryCosts[library.id] = {'library': library, 'total_cost': 0}
        libraryCosts[library.id]['total_cost'] += disk.price
    
    sortedLibraryCosts = sorted(libraryCosts.values(), key=lambda x: x['total_cost'])
    
    for item in sortedLibraryCosts:
        print(f"{item['library'].name}: ${item['total_cost']:.2f}")

    print("\n")


    print("ЗАПРОС 3")
    print("Список библиотек с 'отдел' в названии и имеющиеся в них CD-диски (многие-ко-многим):")
    
    departmentLibraries = [lib for lib in libraries if "отдел" in lib.name.lower()]
    

    for library in departmentLibraries:
        # находим связи для текущей библиотеки
        libraryLinks = [link for link in ManyToMany if link.libraryId == library.id]
        
        # находим CD-диски по связям
        libraryDisks = [disk for link in libraryLinks 
                        for disk in disks if disk.id == link.diskId]
        
        print(f"\n{library.name}:")
        if libraryDisks:
            for disk in libraryDisks:
                print(f"  - {disk.artist} - {disk.title} ({disk.genre})")
        else:
            print("  - Нет CD-дисков")

    print("\n")
    print(f"Всего библиотек: {len(libraries)}")
    print(f"Всего CD-дисков: {len(disks)}")
    print(f"Связей один-ко-многим: {len(OneToMany)}")
    print(f"Связей многие-ко-многим: {len(ManyToMany)}")

if __name__ == "__main__":
    main()
