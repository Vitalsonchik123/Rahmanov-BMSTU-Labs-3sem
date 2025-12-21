using System;
using System.Reflection;

//Класс атрибута
[AttributeUsage(AttributeTargets.Property)]
public class DisplayAttribute : Attribute
{
    public string Label { get; }

    public DisplayAttribute(string label)
    {
        Label = label;
    }
}

//Класс, содержащий конструкторы, свойства, методы
public class Person
{
    [Display("Полное имя")] 
    public string FullName { get; set; }

    [Display("Возраст")]
    public int Age { get; set; }

    public string Email { get; set; } // Свойство без атрибута

    public Person() { }

    public Person(string fullName, int age)
    {
        FullName = fullName;
        Age = age;
    }

    public Person(string fullName, int age, string email) : this(fullName, age)
    {
        Email = email;
    }

    // Методы
    public void DisplayInfo()
    {
        Console.WriteLine($"Имя: {FullName}, Возраст: {Age}");
    }

    public string GetGreeting(string prefix)
    {
        return $"{prefix}, {FullName}!";
    }

    private void PrivateMethod()
    {
        Console.WriteLine("Это приватный метод");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Type personType = typeof(Person);

        Console.WriteLine("Информация о классе Person");
        Console.WriteLine($"Имя класса: {personType.Name}");
        Console.WriteLine($"Пространство имен: {personType.Namespace}");
        Console.WriteLine();

        Console.WriteLine("Конструкторы");
        ConstructorInfo[] constructors = personType.GetConstructors();
        foreach (var constructor in constructors)
        {
            Console.Write($"{constructor.Name}(");
            ParameterInfo[] parameters = constructor.GetParameters();
            for (int i = 0; i < parameters.Length; i++)
            {
                Console.Write($"{parameters[i].ParameterType.Name} {parameters[i].Name}");
                if (i < parameters.Length - 1) Console.Write(", ");
            }
            Console.WriteLine(")");
        }
        Console.WriteLine();

        Console.WriteLine("Свойства");
        PropertyInfo[] properties = personType.GetProperties();
        foreach (var property in properties)
        {
            Console.WriteLine($"- {property.PropertyType.Name} {property.Name} " +
                            $"{{ get; set; }}");
        }
        Console.WriteLine();

        Console.WriteLine("Публичные методы");
        MethodInfo[] methods = personType.GetMethods(BindingFlags.Public | BindingFlags.Instance | BindingFlags.DeclaredOnly);
        foreach (var method in methods)
        {
            if (method.IsSpecialName) continue;

            Console.Write($"{method.ReturnType.Name} {method.Name}(");
            ParameterInfo[] parameters = method.GetParameters();
            for (int i = 0; i < parameters.Length; i++)
            {
                Console.Write($"{parameters[i].ParameterType.Name} {parameters[i].Name}");
                if (i < parameters.Length - 1) Console.Write(", ");
            }
            Console.WriteLine(")");
        }
        Console.WriteLine();

        //только те свойства, которым назначен атрибут
        Console.WriteLine("Свойства с атрибутом Display");
        foreach (var property in properties)
        {
            var attribute = property.GetCustomAttribute<DisplayAttribute>();
            if (attribute != null)
            {
                Console.WriteLine($"{property.Name} -> {attribute.Label}");
            }
        }
        Console.WriteLine();

        Console.WriteLine("Вызов метода с помощью рефлексии");

        Person person = new Person("Иван Иванов", 30, "ivan@example.com");

        MethodInfo getGreetingMethod = personType.GetMethod("GetGreeting");

        if (getGreetingMethod != null)
        {
            object result = getGreetingMethod.Invoke(person, new object[] { "Привет" });
            Console.WriteLine($"Результат вызова метода: {result}");
        }

        Console.WriteLine();

        Console.WriteLine("Вызов метода DisplayInfo");
        MethodInfo displayInfoMethod = personType.GetMethod("DisplayInfo");
        if (displayInfoMethod != null)
        {
            displayInfoMethod.Invoke(person, null);
        }

        Console.WriteLine();
        Console.WriteLine("Нажмите любую клавишу для выхода...");
        Console.ReadKey();
    }
}