"""打印小于给定上限的斐波那契数列。"""


def fib_sequence(limit):
    """生成小于 limit 的斐波那契数。"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def fib_sum(limit):
    """返回小于 limit 的所有斐波那契数之和。"""
    return sum(fib_sequence(limit))


if __name__ == "__main__":
    LIMIT = 500
    numbers = list(fib_sequence(LIMIT))
    print("sequence:", ",".join(str(n) for n in numbers))
    print("count:", len(numbers))
    print("sum:", fib_sum(LIMIT))
