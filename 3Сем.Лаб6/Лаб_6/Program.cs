using System;

namespace Lab6_Delegates
{
    class Program
    {
        // 2 определение делегата, принимающего несколько параметров различных типов и возвращающего значение произвольного типа
        delegate double OperationDelegate(int a, double b, string operation);

        // 3 метод данного делегата
        static double PerformOperation(int a, double b, string operation)
        {
            Console.WriteLine($"Выполняется операция: {a} {operation} {b}");

            switch (operation)
            {
                case "+":
                    return a + b;
                case "-":
                    return a - b;
                case "*":
                    return a * b;
                case "/":
                    if (b != 0)
                        return a / b;
                    else
                        throw new DivideByZeroException("Деление на ноль!");
                case "^":
                    return Math.Pow(a, b);
                default:
                    throw new ArgumentException($"Неизвестная операция: {operation}");
            }
        }

        // 4 принимает разработанный делегат в качестве одного из входных параметров
        static void ProcessNumbers(int x, double y, string op, OperationDelegate operationDelegate)
        {
            Console.WriteLine($"\nОбработка чисел: {x}, {y}");
            Console.WriteLine($"Операция: {op}");

            try
            {
                double result = operationDelegate(x, y, op);
                Console.WriteLine($"Результат: {result:F2}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
        }

        //5 обобщенный делегат Func<>
        static void ProcessNumbersWithFunc(int x, double y, string op, Func<int, double, string, double> operationFunc)
        {
            Console.WriteLine($"\nОбработка с использованием Func<>: {x}, {y}");
            Console.WriteLine($"Операция: {op}");

            try
            {
                double result = operationFunc(x, y, op);
                Console.WriteLine($"Результат: {result:F2}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
        }

        static void Main(string[] args)
        {
            // 4. Вызов метода, передавая в качестве параметра-делегата:

            // а) метод, разработанный в пункте 3
            Console.WriteLine("\nКастомный делегатт с именованным методом");
            OperationDelegate delegate1 = PerformOperation;
            ProcessNumbers(10, 3.5, "+", delegate1);
            ProcessNumbers(15, 4.0, "*", delegate1);
            ProcessNumbers(20, 5.0, "/", delegate1);

            // б) лямбда-выражение
            Console.WriteLine("\nКастомный делегат с лямбда-выражением");
            OperationDelegate delegate2 = (int a, double b, string op) =>
            {
                Console.WriteLine($"Лямбда: {a} {op} {b}");
                return op switch
                {
                    "+" => a + b,
                    "-" => a - b,
                    "*" => a * b,
                    "/" => b != 0 ? a / b : throw new DivideByZeroException("Деление на ноль в лямбде!"),
                    "^" => Math.Pow(a, b),
                    _ => throw new ArgumentException($"Неизвестная операция в лямбде: {op}")
                };
            };

            ProcessNumbers(8, 2.0, "-", delegate2);
            ProcessNumbers(5, 2.0, "^", delegate2);

            // 5. Использование обобщенного делегата Func<>
            Console.WriteLine("\nОбобщенного делегат Func<>");

            // а) с именованным методом
            ProcessNumbersWithFunc(12, 6.0, "/", PerformOperation);

            // б) с лямбда-выражением
            ProcessNumbersWithFunc(7, 3.0, "*", (a, b, op) =>
            {
                Console.WriteLine($"Func-лямбда: {a} {op} {b}");
                return a * b;
            });

            // в) с разными операциями через Func<>
            Func<int, double, string, double> powerFunc = (a, b, op) => Math.Pow(a, b);
            ProcessNumbersWithFunc(2, 8.0, "^", powerFunc);

            // Проверка ошибок
            Console.WriteLine("\nПроверка обработки ошибок");
            ProcessNumbers(10, 0, "/", PerformOperation);
            ProcessNumbersWithFunc(10, 0, "/", PerformOperation);

            Console.WriteLine("\nПрограмма завершена. Нажмите любую клавишу...");
            Console.ReadKey();
        }
    }
}