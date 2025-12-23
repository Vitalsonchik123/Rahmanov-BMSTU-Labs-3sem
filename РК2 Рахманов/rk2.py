from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class CDLibraryDisk:
    id: int
    library_id: int
    disk_id: int

@dataclass
class CDLibrary:
    id: int
    name: str
    location: str

@dataclass
class CDDisk:
    id: int
    title: str
    artist: str
    genre: str
    price: float
    year: int


class CDLibrarySystem:
    def __init__(self):
        self.libraries: List[CDLibrary] = []
        self.disks: List[CDDisk] = []
        self.library_disks: List[CDLibraryDisk] = []
    
    def add_library(self, library: CDLibrary) -> None:
        self.libraries.append(library)
    
    def add_disk(self, disk: CDDisk) -> None:
        self.disks.append(disk)
    
    def add_library_disk_relation(self, relation: CDLibraryDisk) -> None:
        self.library_disks.append(relation)
    
    def create_one_to_many_relations(self) -> List[Tuple[CDLibrary, CDDisk]]:
        relations = []
        
        for disk in self.disks:
            for relation in self.library_disks:
                if relation.disk_id == disk.id:
                    library = next((lib for lib in self.libraries 
                                  if lib.id == relation.library_id), None)
                    if library:
                        relations.append((library, disk))
        
        return relations
    
    def get_sorted_library_disks(self) -> List[Tuple[CDLibrary, CDDisk]]: # Запрос 1
        relations = self.create_one_to_many_relations()
        return sorted(relations, key=lambda x: x[0].name)
    
    def get_library_costs(self) -> List[Dict]: # Запрос 2
        relations = self.create_one_to_many_relations()
        library_costs = {}
        
        for library, disk in relations:
            if library.id not in library_costs:
                library_costs[library.id] = {
                    'library': library, 
                    'total_cost': 0.0
                }
            library_costs[library.id]['total_cost'] += disk.price
        
        return sorted(
            library_costs.values(), 
            key=lambda x: x['total_cost']
        )
    
    def get_department_libraries_with_disks(self) -> List[Dict]: # Запрос 3
        department_libraries = [
            lib for lib in self.libraries 
            if "отдел" in lib.name.lower()
        ]
        result = []
        
        for library in department_libraries:
            # Находим связи для текущей библиотеки
            library_links = [
                link for link in self.library_disks 
                if link.library_id == library.id
            ]
            
            # Находим CD-диски по связям
            library_disks = []
            for link in library_links:
                for disk in self.disks:
                    if disk.id == link.disk_id:
                        library_disks.append(disk)
            
            result.append({
                'library': library,
                'disks': library_disks
            })
        
        return result
    
    def get_statistics(self) -> Dict[str, int]:
        return {
            'total_libraries': len(self.libraries),
            'total_disks': len(self.disks),
            'one_to_many_relations': len(self.create_one_to_many_relations()),
            'many_to_many_relations': len(self.library_disks)
        }


def create_test_data() -> CDLibrarySystem:
    system = CDLibrarySystem()
    
    system.add_library(CDLibrary(1, "Главный отдел музыки", "Центральный район"))
    system.add_library(CDLibrary(2, "Отдел классики", "Северный район"))
    system.add_library(CDLibrary(3, "Рок-коллекция", "Западный район"))
    system.add_library(CDLibrary(4, "Джазовый отдел", "Восточный район"))
    system.add_library(CDLibrary(5, "Поп-музыка отдел", "Южный район"))
    
    system.add_disk(CDDisk(1, "The Dark Side of the Moon", "Pink Floyd", "Rock", 25, 1973))
    system.add_disk(CDDisk(2, "Thriller", "Michael Jackson", "Pop", 19, 1982))
    system.add_disk(CDDisk(3, "Kind of Blue", "Miles Davis", "Jazz", 22, 1959))
    system.add_disk(CDDisk(4, "Symphony No. 9", "Beethoven", "Classical", 18, 1987))
    system.add_disk(CDDisk(5, "Back in Black", "AC/DC", "Rock", 21, 1980))
    system.add_disk(CDDisk(6, "The Wall", "Pink Floyd", "Rock", 24, 1979))
    
    # Связи многие-ко-многим
    system.add_library_disk_relation(CDLibraryDisk(1, 1, 1))
    system.add_library_disk_relation(CDLibraryDisk(2, 1, 2))
    system.add_library_disk_relation(CDLibraryDisk(3, 2, 4))
    system.add_library_disk_relation(CDLibraryDisk(4, 3, 1))
    system.add_library_disk_relation(CDLibraryDisk(5, 3, 5))
    system.add_library_disk_relation(CDLibraryDisk(6, 3, 6))
    system.add_library_disk_relation(CDLibraryDisk(7, 4, 3))
    system.add_library_disk_relation(CDLibraryDisk(8, 5, 2))
    system.add_library_disk_relation(CDLibraryDisk(9, 1, 6))
    
    return system


def main():
    system = create_test_data()
    
    print("\nЗАПРОС 1")
    print("Список всех связанных библиотек и CD-дисков (один-ко-многим), отсортированный по названиям библиотек:")
    
    sorted_library_disks = system.get_sorted_library_disks()
    for library, disk in sorted_library_disks:
        print(f"{library.name}: {disk.artist} - {disk.title}")
    
    print("\nЗАПРОС 2")
    print("Список библиотек с суммарной стоимостью CD-дисков в каждой библиотеке:")
    
    library_costs = system.get_library_costs()
    for item in library_costs:
        print(f"{item['library'].name}: ${item['total_cost']:.2f}")
    
    print("\nЗАПРОС 3")
    print("Список библиотек с 'отдел' в названии и имеющиеся в них CD-диски:")
    
    department_data = system.get_department_libraries_with_disks()
    for item in department_data:
        print(f"\n{item['library'].name}:")
        if item['disks']:
            for disk in item['disks']:
                print(f"  - {disk.artist} - {disk.title} ({disk.genre})")
        else:
            print("  - Нет CD-дисков")
    
    print("\nСТАТИСТИКА СИСТЕМЫ:")
    stats = system.get_statistics()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
