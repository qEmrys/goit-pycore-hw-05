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