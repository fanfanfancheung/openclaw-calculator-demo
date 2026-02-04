#!/usr/bin/env python3
"""
计算器功能测试脚本
"""

from calculator import Calculator

def test_calculator():
    """测试计算器的各项功能"""
    calc = Calculator()
    
    print("🧪 开始测试计算器功能...\n")
    
    # 测试基本运算
    print("1. 测试基本运算:")
    tests = [
        ('+', 5, 3, 8),
        ('-', 10, 4, 6),
        ('*', 7, 6, 42),
        ('/', 15, 3, 5)
    ]
    
    for op, a, b, expected in tests:
        result = calc.calculate(op, a, b)
        status = "✅" if result == expected else "❌"
        print(f"   {status} {a} {op} {b} = {result} (期望: {expected})")
    
    # 测试连续计算
    print("\n2. 测试连续计算:")
    calc.reset()
    calc.calculate('+', 10, 5)  # 10 + 5 = 15
    result1 = calc.get_result()
    print(f"   首次计算: 10 + 5 = {result1}")
    
    result2 = calc.calculate('*', 2)  # 15 * 2 = 30
    print(f"   连续计算: {result1} * 2 = {result2}")
    
    # 测试除零错误
    print("\n3. 测试除零错误处理:")
    calc.reset()
    result = calc.calculate('/', 10, 0)
    status = "✅" if result is None else "❌"
    print(f"   {status} 10 / 0 = {result} (应该返回None并显示错误)")
    
    # 测试重置功能
    print("\n4. 测试重置功能:")
    calc.calculate('+', 100, 200)
    before_reset = calc.get_result()
    calc.reset()
    after_reset = calc.get_result()
    status = "✅" if after_reset == 0 else "❌"
    print(f"   {status} 重置前: {before_reset}, 重置后: {after_reset}")
    
    print("\n🎉 计算器功能测试完成！")

if __name__ == "__main__":
    test_calculator()