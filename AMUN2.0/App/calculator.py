import re  
import math  
  
def calculate(expression):  
    # 去除空格  
    expression = expression.replace(" ", "")  
  
    # 检查是否有未闭合的括号  
    if not is_balanced(expression):  
        raise SyntaxError("The parentheses don't match")  
  
    # 计算表达式的值  
    try:  
        result = eval(expression)  
    except Exception as e:  
        raise SyntaxError("Expressions can't be evaluated") from e  
  
    return result  
  
def is_balanced(expression):  
    # 使用栈来检查括号是否匹配  
    stack = []  
    for char in expression:  
        if char == '(':  
            stack.append(char)  
        elif char == ')':  
            if not stack or stack.pop() != '(':  
                return False  
    return len(stack) == 0  
  
while True:  
    try:  
        # 获取用户输入  
        expression = input("Please enter an arithmetic expression (enter 'exit' to exit): ")  
  
        # 检查用户是否想退出  
        if expression.lower() == "exit":  
            break  
  
        # 尝试计算用户输入的表达式  
        result = calculate(expression)  
  
        # 显示结果  
        print(f"The result is as follows: {result}")  
  
    except ZeroDivisionError:  
        print("The divisor cannot be 0, please re-enter it")  
    except SyntaxError as e:  
        print(f"Expression error: {e}")  
    except Exception as e:  
        print(f"An unknown error occurred:{e}")
