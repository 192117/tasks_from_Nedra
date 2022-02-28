'''
    Модуль для проверки соответствия условию задачи входных данных и получения результата вычисления выражения.
'''
import re
import operator
import string

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '?': operator.neg,
    '!': operator.pos
    }

weight_operators = {
    '(': 1,
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '?': 4,
    '!': 4
    }

def check_value(val: str) -> list:
    '''
        Функция обрабатывает исходные данные, проверяет с помощью регулярного выражения на соответствие правильности.
        Если данные не проходят, то возвращает пустой список.
        Если данные проходят, то обрабатывает данные из строки получает целые числа или дробные (формотирование) и
        операторы.

    :param val
    :return: result
    '''
    pattern = r"(?P<op1>([\+\-]?\s*(\d+)|[\+\-]?\s*(\d+\.{1}\d*))\s*)" \
              r"(?P<op2>((\/\s*(\d+)\s*|\/\s*(\d+\.{1}\d*)\s*)|(\*\s*(\d+)\s*|\*\s*(\d+\.{1}\d*)\s*)|" \
              r"(\+\s*(\d+)\s*|\+\s*(\d+\.{1}\d*)\s*)|(\-\s*(\d+)\s*|\-\s*(\d+\.{1}\d*\s*)))*)$"
    comp = re.compile(pattern)
    result = []
    if comp.match(val):
        value = comp.match(val).group().translate({ord(c): None for c in string.whitespace}) # Удаление пробельных символов.
        if '+' in comp.match(value).groupdict()['op1']:
            if '.' in comp.match(value).groupdict()['op1']:
                result.append('+')
                result.append(float(comp.match(value).groupdict()['op1'][1:]))
            else:
                result.append('+')
                result.append(int(comp.match(value).groupdict()['op1'][1:]))
        elif '-' in comp.match(value).groupdict()['op1']:
            if '.' in comp.match(value).groupdict()['op1']:
                result.append('-')
                result.append(float(comp.match(value).groupdict()['op1'][1:]))
            else:
                result.append('-')
                result.append(int(comp.match(value).groupdict()['op1'][1:]))
        else:
            if '.' in comp.match(value).groupdict()['op1']:
                result.append(float(comp.match(value).groupdict()['op1']))
            else:
                result.append(int(comp.match(value).groupdict()['op1']))
        if len(comp.match(value).groupdict()['op2']) > 0:
            ans = []
            for elem in comp.match(value).groupdict()['op2']:
                if elem in operators and len(ans) == 0:
                    result.append(elem)
                elif elem.isdigit() or elem == '.':
                    ans.append(elem)
                elif elem in operators and len(ans) != 0:
                    if '.' in ans:
                        s = ''.join(ans)
                        result.append(float(s))
                        del ans[:]
                    else:
                        s = ''.join(ans)
                        result.append(int(s))
                        del ans[:]
                    result.append(elem)
            else:
                if '.' in ans:
                    s = ''.join(ans)
                    result.append(float(s))
                else:
                    s = ''.join(ans)
                    result.append(int(s))
        else:
            pass
    return result

def RPN(line: list) -> list:
    '''
        Функция для получения обратной польской нотации, учитывающей приоритет операций. Поддерживает унарные
        операторы (- и +). В случае "-" преобразует в "?", в случае "+" в "!".
        Если получили пустой список (данные не соотвествуют условиям в функции "check_value"), то передаем его дальше.

    :param line
    :return: result
    '''
    if len(line) > 0:
        result = []
        stack = []
        for element in line:
            if element not in operators:
                result.append(element)
            else:
                last = None if not stack else stack[-1]
                if last is None:
                    if len(result) == 0:
                        if element == "-":
                            stack.append('?')
                        elif element == "+":
                            stack.append('!')
                    else:
                        stack.append(element)
                else:
                    while weight_operators[last] >= weight_operators[element]:
                        result.append(stack.pop())
                        last = None if not stack else stack[-1]
                        if last is None:
                            break
                    stack.append(element)
        for e in reversed(stack):
            result.append(e)
        return result
    else:
        return line

def polska(line: list) -> str:
    '''
        Функция, вычисляет выражение и возвращает результат в строковом виде.
        Если получили пустой список (данные не соотвествуют условиям в функции "check_value"), то возвращаем пустую
        строку.

    :param line
    '''
    if len(line) > 0:
        stack = []
        for element in line:
            if type(element) is int or type(element) is float:
                stack.append(element)
            else:
                if element == "?" or element == "!":
                    v = stack.pop()
                    stack.append(operators[element](v))
                elif element in '+-/*':
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(operators[element](v2, v1))
                else:
                    stack.append(element)
        if type(stack[0]) is float:
            return str(round(stack.pop(), 3))
        else:
            return str(stack.pop())
    else:
        return str(line)
