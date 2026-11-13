def f(n):
    return 4**n + 6*n - 1  # вираз із варіанта 11

m = 9  # дільник

bad = [n for n in range(1, 101) if f(n) % m != 0]

print("Контрприкладів не знайдено" if not bad else bad)