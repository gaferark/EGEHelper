class GeometryProgression:
    def __init__(self, start, step):
        self.__start, self.__step = self.__soft_float_to_int(start), self.__soft_float_to_int(step)
        self.__is_growing = abs(self.__step) > 1
        self.__current_value = self.__soft_float_to_int(self.__start / self.__step)

    def __next__(self):
        self.__current_value *= self.__step
        return self.__soft_float_to_int(self.__current_value)

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if type(item) != int or item < 0:
            raise TypeError
        return self.__soft_float_to_int(self.__start * (self.__step ** item))

    def sum_to(self, limit):
        return self.__start / (self.__step - 1) * (self.__step ** limit - 1)

    def sum_infinite(self):
        if self.__is_growing:
            raise ValueError('Absolute step value is more than 1')
        return self.__start / (1 - self.__step)

    @staticmethod
    def __soft_float_to_int(x):
        if x % 1 != 0:
            return x
        return int(x)


class Rationale:
    def __init__(self, numerator: int, denominator: int):
        from math import gcd

        if all(map(lambda x: False if type(x) in (int, Rationale) else True, [numerator, denominator])):
            raise TypeError
        if not denominator:
            raise ZeroDivisionError

        self.__num = numerator // gcd(numerator, denominator)
        self.__dem = denominator // gcd(numerator, denominator)
        if self.__sign(self.__num) == self.__sign(self.__dem):
            self.__num, self.__dem = abs(self.__num), abs(self.__dem)
        else:
            self.__num, self.__dem == -abs(self.__num), abs(self.__dem)

    def get_numerator(self):
        return self.__num

    def get_denominator(self):
        return self.__dem

    def change_denominator(self, new):
        self.__dem = new

    def change_numerator(self, new):
        self.__num = new

    def __str__(self):
        return f'{self.__num}/{self.__dem}'

    def __add__(self, other):
        if type(other) == int:
            return Rationale(self.__num + (self.__dem * other), self.__dem)
        elif type(other) == Rationale:
            return Rationale(self.__num * other.get_denominator() + other.get_numerator() * self.__dem,
                             self.__dem * other.get_denominator())
        else:
            return TypeError

    def __radd__(self, other):
        if type(other) == int:
            return Rationale(self.__num + (self.__dem * other), self.__dem)
        elif type(other) == Rationale:
            return None
        else:
            return TypeError

    def __sub__(self, other):
        if type(other) == int:
            return Rationale(self.__num - (self.__dem * other), self.__dem)
        elif type(other) == Rationale:
            return Rationale(self.__num * other.get_denominator() - other.get_numerator() * self.__dem, self.__dem * other.get_denominator())
        else:
            return TypeError

    def __rsub__(self, other):
        if type(other) == int:
            return Rationale(self.__dem * other - self.__num, self.__dem)
        elif type(other) == Rationale:
            return None
        else:
            return TypeError

    def __mul__(self, other):
        if type(other) == int:
            return Rationale(self.__num * other, self.__dem)
        elif type(other) == Rationale:
            return Rationale(self.__num * other.get_numerator(), self.__dem * other.get_denominator())
        else:
            return TypeError

    def __rmul__(self, other):
        if type(other) == int:
            return Rationale(self.__num * other, self.__dem)
        elif type(other) == Rationale:
            return None
        else:
            return TypeError

    def __truediv__(self, other):
        if type(other) == int:
            return Rationale(self.__num, self.__dem * other)
        elif type(other) == Rationale:
            return Rationale(self.__num * other.get_denominator(), self.__dem * other.get_numerator())
        else:
            return TypeError

    def __rtruediv__(self, other):
        if type(other) == int:
            return Rationale(other * self.__dem, self.__num)
        elif type(other) == Rationale:
            return None
        else:
            return TypeError

    def __neg__(self):
        return Rationale(-self.__num, self.__dem)

    def __pos__(self):
        return Rationale(self.__num, self.__dem)

    def __abs__(self):
        return Rationale(abs(self.__num), self.__dem)

    def __float__(self):
        return self.__num / self.__dem

    @staticmethod
    def __sign(x):
        if not x:
            return 0
        return x // abs(x)


def mult(list_value):
    if len(list_value) > 1:
        return list_value[0] * mult(list_value[1:])
    return list_value[0]


def factorization(n):
    i = 2
    primes = []
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 1
    if n > 1:
        primes.append(n)
    return primes


def check_amount_of_devs(n, lim):
    i = 2
    devs = 2
    while i * i <= n:
        while n % i == 0:
            devs += 1
            n //= i
        i += 1
        if devs > lim:
            return False
    if n > 1:
        devs += 1
    return devs == lim


def devs_numbers(n):
    from itertools import combinations

    prime_devs = factorization(n)
    all_combinations = sorted(list(set([mult(c) for i in range(1, len(prime_devs)) for c in combinations(prime_devs, i)])))
    return all_combinations


def split_number(n):
    return list(str(n))


def is_digits_growing(n):
    return sum([1 for i, j in list(zip([None] + split_number(n), split_number(n) + [None]))[1:-1] if i < j]) == len(split_number(n)) - 1