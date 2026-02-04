#!/usr/bin/env python3
"""
简单计算器程序
支持基本四则运算和连续计算
"""

import sys


class Calculator:
    """简单计算器类"""
    
    def __init__(self):
        self.result = 0
        self.history = []  # 新增：计算历史记录
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
    
    def add(self, x, y):
        """加法"""
        return x + y
    
    def subtract(self, x, y):
        """减法"""
        return x - y
    
    def multiply(self, x, y):
        """乘法"""
        return x * y
    
    def divide(self, x, y):
        """除法，包含除零检查"""
        if y == 0:
            raise ValueError("错误：不能除以零！")
        return x / y
    
    def calculate(self, operation, num1, num2=None):
        """执行计算"""
        try:
            if operation in self.operations:
                if num2 is None:
                    # 连续计算模式，使用当前结果作为第一个数
                    result = self.operations[operation](self.result, num1)
                    calculation = f"{self.result} {operation} {num1} = {result}"
                else:
                    # 新计算
                    result = self.operations[operation](num1, num2)
                    calculation = f"{num1} {operation} {num2} = {result}"
                
                # 记录到历史
                self.history.append(calculation)
                self.result = result
                return result
            else:
                raise ValueError(f"不支持的运算符：{operation}")
        except ValueError as e:
            print(f"计算错误：{e}")
            return None
    
    def reset(self):
        """重置计算器"""
        self.result = 0
        self.history = []  # 同时清空历史记录
    
    def get_result(self):
        """获取当前结果"""
        return self.result
    
    def get_history(self):
        """获取计算历史"""
        return self.history
    
    def show_history(self):
        """显示计算历史"""
        if not self.history:
            print("📝 暂无计算历史")
            return
        
        print("\n📝 计算历史：")
        print("-" * 30)
        for i, calc in enumerate(self.history[-10:], 1):  # 只显示最近10次
            print(f"{i:2d}. {calc}")
        
        if len(self.history) > 10:
            print(f"... (共 {len(self.history)} 次计算)")
        print("-" * 30)


def print_menu():
    """打印菜单"""
    print("\n" + "="*40)
    print("🧮 简单计算器")
    print("="*40)
    print("操作说明：")
    print("1. 输入：数字1 运算符 数字2  (例：5 + 3)")
    print("2. 连续计算：运算符 数字     (例：* 2)")
    print("3. 输入 'history' 查看计算历史")
    print("4. 输入 'reset' 重置结果")
    print("5. 输入 'quit' 或 'q' 退出")
    print("="*40)


def parse_input(user_input):
    """解析用户输入"""
    user_input = user_input.strip().lower()
    
    if user_input in ['quit', 'q', 'exit']:
        return 'quit', None, None, None
    
    if user_input == 'reset':
        return 'reset', None, None, None
    
    if user_input == 'history':
        return 'history', None, None, None
    
    # 分割输入
    parts = user_input.split()
    
    if len(parts) == 2:
        # 连续计算模式：运算符 数字
        try:
            operator = parts[0]
            num = float(parts[1])
            return 'continue', operator, num, None
        except ValueError:
            return 'error', None, None, None
    
    elif len(parts) == 3:
        # 新计算模式：数字1 运算符 数字2
        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            return 'new', operator, num1, num2
        except ValueError:
            return 'error', None, None, None
    
    return 'error', None, None, None


def main():
    """主函数"""
    calculator = Calculator()
    print_menu()
    
    while True:
        # 显示当前结果
        print(f"\n当前结果：{calculator.get_result()}")
        
        # 获取用户输入
        user_input = input("\n请输入计算表达式: ").strip()
        
        if not user_input:
            continue
        
        # 解析输入
        action, operator, num1, num2 = parse_input(user_input)
        
        if action == 'quit':
            print("\n感谢使用计算器！👋")
            sys.exit(0)
        
        elif action == 'reset':
            calculator.reset()
            print("✅ 计算器已重置")
        
        elif action == 'history':
            calculator.show_history()
        
        elif action == 'error':
            print("❌ 输入格式错误！请参考操作说明")
        
        elif action == 'continue':
            # 连续计算
            result = calculator.calculate(operator, num1)
            if result is not None:
                print(f"✅ {calculator.get_result()} {operator} {num1} = {result}")
        
        elif action == 'new':
            # 新计算
            result = calculator.calculate(operator, num1, num2)
            if result is not None:
                print(f"✅ {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()