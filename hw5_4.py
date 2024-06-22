import re

def evaluate_expression(expression):
    try:
        # 檢查是否有不支持的字符
        if re.search(r'[^0-9+\-*/().\s]', expression):
            raise ValueError("不支持的字符錯誤")

        # 檢查括號是否匹配
        if expression.count('(') != expression.count(')'):
            raise ValueError("括號不平衡錯誤")

        # 移除所有空格
        expression = expression.replace(' ', '')

        # 使用 eval 函數進行計算，並捕獲 ZeroDivisionError 錯誤
        result = eval(expression)
        return result

    except ZeroDivisionError:
        return "除以零錯誤"
    except SyntaxError:
        return "操作數錯誤"
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"發生意外錯誤：{str(e)}"

def main():
    print("請輸入算術表達式以進行評估。輸入 'q' 退出程序。")
    while True:
        expression = input("請輸入表達式：")
        if expression.lower() == 'q':
            break
        result = evaluate_expression(expression)
        print(f"結果：{result}")

if __name__ == "__main__":
    main()
