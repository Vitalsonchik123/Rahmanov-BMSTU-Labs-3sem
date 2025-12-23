import unittest
from rk2 import CDLibrary, CDDisk, CDLibraryDisk, CDLibrarySystem


class TestCDLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        self.system = CDLibrarySystem()
        
        self.library1 = CDLibrary(1, "Главный отдел музыки", "Центральный район")
        self.library2 = CDLibrary(2, "Отдел классики", "Северный район")
        self.library3 = CDLibrary(3, "Рок-коллекция", "Западный район")
        
        self.disk1 = CDDisk(1, "The Dark Side of the Moon", "Pink Floyd", "Rock", 25.0, 1973)
        self.disk2 = CDDisk(2, "Thriller", "Michael Jackson", "Pop", 19.0, 1982)
        self.disk3 = CDDisk(3, "Kind of Blue", "Miles Davis", "Jazz", 22.0, 1959)
        
        self.relation1 = CDLibraryDisk(1, 1, 1)  
        self.relation2 = CDLibraryDisk(2, 1, 2)
        self.relation3 = CDLibraryDisk(3, 2, 3)
    
    def test_1_add_and_retrieve_libraries_disks(self): # тест1: Добавление и извлечение библиотек и дисков
        self.system.add_library(self.library1)
        self.system.add_library(self.library2)
        
        self.system.add_disk(self.disk1)
        self.system.add_disk(self.disk2)
        
        self.assertEqual(len(self.system.libraries), 2)
        self.assertEqual(len(self.system.disks), 2)
        
        self.assertEqual(self.system.libraries[0].name, "Главный отдел музыки")
        self.assertEqual(self.system.disks[0].title, "The Dark Side of the Moon")
        self.assertEqual(self.system.disks[1].artist, "Michael Jackson")
    
    def test_2_library_disk_relations_and_sorting(self): # тест2: Связи библиотек с дисками и сортировка
        self.system.add_library(self.library1)
        self.system.add_library(self.library2)
        self.system.add_library(self.library3)
        
        self.system.add_disk(self.disk1)
        self.system.add_disk(self.disk2)
        self.system.add_disk(self.disk3)
        
        self.system.add_library_disk_relation(self.relation1)
        self.system.add_library_disk_relation(self.relation2)
        self.system.add_library_disk_relation(self.relation3)
        
        relations = self.system.create_one_to_many_relations()
        self.assertEqual(len(relations), 3)
        
        self.assertEqual(relations[0][0].id, 1)  
        self.assertEqual(relations[0][1].id, 1)  
        
        sorted_relations = self.system.get_sorted_library_disks()
        
        # Проверяем, что библиотеки отсортированы
        library_names = [lib.name for lib, _ in sorted_relations]
        self.assertEqual(library_names[0], "Главный отдел музыки")
        self.assertEqual(library_names[1], "Главный отдел музыки") 
        self.assertEqual(library_names[2], "Отдел классики")
        self.assertEqual(len(sorted_relations), 3)
    
    def test_3_library_costs_and_department_filter(self): # тест3: Расчет стоимости и фильтрация по отделу
        self.system.add_library(self.library1)  
        self.system.add_library(self.library2)  
        self.system.add_library(self.library3)  
        
        self.system.add_disk(self.disk1)  
        self.system.add_disk(self.disk2)  
        self.system.add_disk(self.disk3)
        
        self.system.add_library_disk_relation(self.relation1)  
        self.system.add_library_disk_relation(self.relation2)  
        self.system.add_library_disk_relation(self.relation3)  
        
        library_costs = self.system.get_library_costs()
        
        self.assertEqual(len(library_costs), 2)
        
        library_costs_sorted = sorted(library_costs, key=lambda x: x['library'].id)
        
        self.assertEqual(library_costs_sorted[0]['total_cost'], 44.0)  # 25.0 + 19.0
        
        self.assertEqual(library_costs_sorted[1]['total_cost'], 22.0)
        
        department_data = self.system.get_department_libraries_with_disks()
        
        self.assertEqual(len(department_data), 2)
        
        library_names = [item['library'].name for item in department_data]
        self.assertIn("Главный отдел музыки", library_names)
        self.assertIn("Отдел классики", library_names)
        self.assertNotIn("Рок-коллекция", library_names)
        
        department_data_sorted = sorted(department_data, key=lambda x: x['library'].id)
        
        self.assertEqual(len(department_data_sorted[0]['disks']), 2)  
        self.assertEqual(len(department_data_sorted[1]['disks']), 1)  


class CustomTestRunner:
    
    @staticmethod
    def run_tests():
        print("Запуск тестов...")
        
        test_instance = TestCDLibrarySystem()
        
        test_methods = [
            ('Тест1', test_instance.test_1_add_and_retrieve_libraries_disks),
            ('Тест2', test_instance.test_2_library_disk_relations_and_sorting),
            ('Тест3', test_instance.test_3_library_costs_and_department_filter)
        ]
        
        for test_name, test_method in test_methods:
            try:
                test_instance.setUp()
                test_method()
                print(f"{test_name} выполнен")
            except AssertionError as e:
                print(f"{test_name} не выполнен: {e}")
            except Exception as e:
                print(f"{test_name} ошибка: {e}")
            finally:
                test_instance.tearDown() if hasattr(test_instance, 'tearDown') else None


if __name__ == '__main__':
    CustomTestRunner.run_tests()
