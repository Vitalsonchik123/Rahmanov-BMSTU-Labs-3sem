using System;

namespace LevenshteinDistanceLibrary
{
    public static class LevenshteinCalculator
    {
        /// <summary>
        /// Вычисляет расстояние Левенштейна между двумя строками используя алгоритм Вагнера-Фишера
        /// </summary>
        /// <param name="s1">Первая строка</param>
        /// <param name="s2">Вторая строка</param>
        /// <returns>Расстояние Левенштейна</returns>
        public static int CalculateDistance(string s1, string s2)
        {
            // Проверка на пустые строки
            if (string.IsNullOrEmpty(s1))
            {
                return string.IsNullOrEmpty(s2) ? 0 : s2.Length;
            }

            if (string.IsNullOrEmpty(s2))
            {
                return s1.Length;
            }

            // Создаем матрицу (s1.Length + 1) x (s2.Length + 1)
            int[,] matrix = new int[s1.Length + 1, s2.Length + 1];

            // Инициализация первой строки (от 0 до длины s2)
            for (int i = 0; i <= s1.Length; i++)
            {
                matrix[i, 0] = i;
            }

            // Инициализация первого столбца (от 0 до длины s1)
            for (int j = 0; j <= s2.Length; j++)
            {
                matrix[0, j] = j;
            }

            // Заполнение матрицы по алгоритму Вагнера-Фишера
            for (int i = 1; i <= s1.Length; i++)
            {
                for (int j = 1; j <= s2.Length; j++)
                {
                    // Стоимость операции: 0 если символы совпадают, 1 если разные
                    int cost = (s1[i - 1] == s2[j - 1]) ? 0 : 1;

                    // Вычисляем минимальную стоимость из трех возможных операций:
                    // 1. Удаление символа из s1: matrix[i-1, j] + 1
                    // 2. Вставка символа в s1: matrix[i, j-1] + 1  
                    // 3. Замена символа: matrix[i-1, j-1] + cost
                    matrix[i, j] = Math.Min(
                        Math.Min(
                            matrix[i - 1, j] + 1,      // удаление
                            matrix[i, j - 1] + 1       // вставка
                        ),
                        matrix[i - 1, j - 1] + cost    // замена
                    );
                }
            }

            // Результат находится в правом нижнем углу матрицы
            return matrix[s1.Length, s2.Length];
        }
    }
}