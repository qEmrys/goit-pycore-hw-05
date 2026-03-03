from typing import Callable, Iterator
import re

def caching_fibonacci() -> int:
    cache = {}

    def fibonacci(num: int) -> int:
        if num in cache:
            return cache[num]
        if num <= 1:
            return num
        cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return cache[num]
    return fibonacci

def generator_numbers(text: str) -> Iterator[float]:
    pattern = r'-?\d+(?:\.\d+)?'

    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    numbers = list(func(text))
    return sum(numbers)