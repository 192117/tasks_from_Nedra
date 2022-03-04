# **Тестовое задание**
## **Требования**

1. _Сервис-калькулятор_

    `С помощью фреймворка FastAPI реализовать сервис, вычисляющий результат арифметического выражения предоставляющий 
    возможность просмотреть история запросов.
    
    _Общие требования_
    
    - Сервис должен соответствовать Rest соглашениям: Get, Post запросы, HTTP коды ответов и т.д.
    - Аутентификация и авторизация не требуется.
    - Сервис должен быть "самодокументированным" - предоставлять описание форматов данных и
    запросов/ответов в формате OpenAPI с интерфейсом Swagger.
    
    _Описание конечных точек (endpoints)_
    
    **_/calc_**
    
    Принимает в качестве входного значения арифметическое выражение и выдаёт либо ответ, либо ошибку.
    
    _Обобщённый вид арифметического выражения: **\[операция1](число)[(операция2)(число)]***_, где:
    
    - операция1: плюс или минус: + -
    - операция2: плюс, минус, умножение, деление: + - * /
    - число: положительное вещественное число (decimal), имеющее ноль и более знаков после запятой
    - круглые скобки: обязательный элемент
    - квадратные скобки: необязательный элемент
    - звёздочка (*): ноль и более повторений
    - пробелы игнорируются
    
    _Примеры выражений и результат расчёта (информация по расчёту: см. ниже):_
    
    - `+100.1 = 100.1`
    - `-0 = 0`
    - `-7 / 34.2 = -0.205`
    - `- 6 * 2 = -11.98`
    - `2. / 1. = 2`
    - `5 + - 4 = ошибка`
    - `*1 + 7 = ошибка`
    - `4 / 3 + = ошибка`
    
    _Замечания по расчёту:_
    
    - арифметический приоритет операций игнорируется – все операции выполняются слева направо, то есть выражение 
    5 - 4 * 2 считается как (5 - 4) * 2, результат: 2
    - количество значащих цифр после запятой: до 3 включительно, незначащих нули должны быть обрезаны
    - округление математическое: 1.1234 → 1.123, 1.1235 → 1.124
    
    _Замечание по реализации:_
    
    - использование eval не допускается;
    - будет плюсом написать реализацию, учитывающую приоритет операций и допускающей использование скобок (подсказка: 
    польская нотация).
    
    **_/history_**
    
    Конечная точка возвращает последние 30 (по умолчанию) запросов к сервису в формате json (массив), где каждый 
    запрос/ответ имеет вид:
    
    - Успешно рассчитанный: {"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}
    - Запрос с ошибкой: {"request": "5 + - 4", "response": "", "status": "fail"}
    
    Пример ответа для двух запросов: 
    
    `[{"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}, {"request": "5 + - 4", "response": "", "status": "fail"}]`
    
    _Дополнительные параметры запроса (могут использоваться совместно):_
    
    - limit (int) - ограничить количество выводимых запросов; при значениях меньше 1 и больше 30, возвращается ошибка;
    - status (str) - отфильтровать успешные запросы или запросы с ошибкой; допустимые значения: success, fail. При других 
    значениях возвращается ошибка.
    
    Замечание по реализации: имеет смысл ограничить внутренне хранилище истории количеством значений по умолчанию (30), 
    дабы постоянно запущенный сервис не съел память.`

2. _Сервис-калькулятор_

    Реализовать программу, играющую в игру Крестики-нолики на поле 3*3.
    
    _Общие требования_
    
    - Один запуск программы - одна игра.
    - Компьютер играет сам с собой за двух игроков. В конце игры выводится история ходов обоих "игроков" и результат 
    ("Ничья", "Выиграл игрок 1", "Выиграл игрок 2")
    
    _Будет плюсом_
    
    - Возможность задать произвольный размер поля, например 4*20.
    - Возможность задать количество подряд идущих крестиков/ноликов для победы, например 5 для поля 20*20.
    - Использование осмысленного алгоритма или иного способа игры компьютера, отличного от случайного проставления 
    крестиков/ноликов.