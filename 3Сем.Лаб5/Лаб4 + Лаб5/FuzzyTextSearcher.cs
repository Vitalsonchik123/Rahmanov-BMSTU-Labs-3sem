using System;
using System.Collections.Generic;

namespace LevenshteinDistanceLibrary
{
    public class SearchResult
    {
        public string Text { get; set; }
        public int Distance { get; set; }
        public int Position { get; set; }

        public SearchResult(string text, int distance, int position)
        {
            Text = text;
            Distance = distance;
            Position = position;
        }

        public override string ToString()
        {
            return $"'{Text}' (расстояние: {Distance}, позиция: {Position})";
        }
    }

    public class FuzzyTextSearcher
    {
        /// <summary>
        /// Поиск приблизительных совпадений в тексте с использованием расстояния Левенштейна
        /// </summary>
        /// <param name="text">Исходный текст</param>
        /// <param name="searchPattern">Паттерн для поиска</param>
        /// <param name="maxDistance">Максимальное расстояние Левенштейна</param>
        /// <returns>Список результатов поиска</returns>
        public static List<SearchResult> Search(string text, string searchPattern, int maxDistance)
        {
            var results = new List<SearchResult>();

            if (string.IsNullOrEmpty(text) || string.IsNullOrEmpty(searchPattern))
                return results;

            // Поиск по словам
            string[] words = text.Split(new[] { ' ', '\t', '\n', '\r', '.', ',', '!', '?', ';', ':' },
                                      StringSplitOptions.RemoveEmptyEntries);

            for (int i = 0; i < words.Length; i++)
            {
                int distance = LevenshteinCalculator.CalculateDistance(words[i], searchPattern);

                if (distance <= maxDistance)
                {
                    int position = FindWordPosition(text, words[i], i);
                    results.Add(new SearchResult(words[i], distance, position));
                }
            }

            return results;
        }

        private static int FindWordPosition(string text, string word, int wordIndex)
        {
            string[] allWords = text.Split(new[] { ' ', '\t', '\n', '\r', '.', ',', '!', '?', ';', ':' },
                                         StringSplitOptions.RemoveEmptyEntries);

            int currentPosition = 0;
            int currentWordIndex = 0;

            for (int i = 0; i < text.Length; i++)
            {
                if (currentWordIndex == wordIndex)
                {
                    // Проверяем, что мы на начале слова
                    if (i == 0 || IsSeparator(text[i - 1]))
                    {
                        return i;
                    }
                }

                if (IsSeparator(text[i]))
                {
                    // Пропускаем разделители
                    while (i < text.Length && IsSeparator(text[i]))
                    {
                        i++;
                    }

                    if (i < text.Length)
                    {
                        currentWordIndex++;
                    }
                }
            }

            return 0;
        }

        private static bool IsSeparator(char c)
        {
            return char.IsWhiteSpace(c) || c == '.' || c == ',' || c == '!' || c == '?' || c == ';' || c == ':';
        }
    }
}