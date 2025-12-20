using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;
using LevenshteinDistanceLibrary;

namespace Лаб4_Рахманов
{
    public partial class Form1 : Form
    {
        private List<string> words = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        //загрузка файла
        private void btnLoadFile_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Text files (*.txt)|*.txt";

            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                Stopwatch stopwatch = Stopwatch.StartNew();

                try
                {
                    string fileContent = File.ReadAllText(openFileDialog.FileName);

                    char[] separators = { ' ', ',', '.', '!', '?', ';', ':', '\n', '\r', '\t' };
                    string[] allWords = fileContent.Split(separators, StringSplitOptions.RemoveEmptyEntries);

                    words.Clear();

                    foreach (string word in allWords)
                    {
                        string cleanWord = word.Trim().ToLower();
                        if (!string.IsNullOrEmpty(cleanWord) && !words.Contains(cleanWord))
                        {
                            words.Add(cleanWord);
                        }
                    }

                    stopwatch.Stop();

                    lblTime.Text = $"Время загрузки: {stopwatch.ElapsedMilliseconds} мс";
                    lblWordCount.Text = $"Уникальных слов: {words.Count}";
                    lstResults.Items.Clear();
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ошибка: {ex.Message}");
                }
            }
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            string searchWord = txtSearch.Text.Trim().ToLower();

            if (string.IsNullOrEmpty(searchWord))
            {
                MessageBox.Show("Введите слово для поиска");
                return;
            }

            lstResults.Items.Clear();




            //алгоритм Левенштейна
            foreach (string word in words)
            {
                int distance = LevenshteinCalculator.CalculateDistance(word, searchWord);

                //максимальное расстояние 2 для нахождения похожих слов
                if (distance <= 2)
                {
                    lstResults.Items.Add($"{word} (расстояние: {distance})");
                }
            }
            if (lstResults.Items.Count == 0)
            {
                lstResults.Items.Add("Слов не найдено");
            }
        }




        //поиск при нажатии Enter в поле ввода
        private void txtSearch_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Enter)
            {
                btnSearch_Click(sender, e);
                e.Handled = true;
            }
        }
    }
}
//это копия 4 лабы

