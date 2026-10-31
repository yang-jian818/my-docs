def add(a, b):
    return a * b  # 错误的实现：用于验证工作流能否发现测试失败


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("3 * 4 =", multiply(3, 4))
