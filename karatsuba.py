''' Integer multiplication with Karatsuba's Algorithm '''
from popup import popup
import time
from decimal import Decimal


class BigInt(int):
    def __new__(cls, value):
        return int.__new__(cls, value)

    def __mul__(self, other):
        ''' Karatsuba Multiplication '''

        if len(str(self)) == 1 or len(str(other)) == 1:
            return int.__mul__(self, other)

        n = max(len(str(self)), len(str(other)))
        n2 = n // 2

        a = self // 10**n2
        b = self % 10**n2
        c = other // 10**n2
        d = other % 10**n2

        ac = a * c
        bd = b * d
        ab_cd = ((a+b) * (c+d)) - ac - bd

        return ac * 10**(2*n2) + ab_cd * 10**n2 + bd


def karatsuba(valores):
    start = time.perf_counter()
    total = BigInt(1)
    for num in valores:
        num = BigInt(abs(num))
        total = total * num

    total_time = round(time.perf_counter() - start, 2)
    popup(f"Multiplicamos {len(valores)} números\n"
          + f"Total: {Decimal(total):.8e}\n"
          + f"Tiempo de ejecución: {total_time}")
