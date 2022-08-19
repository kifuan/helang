from typing import Optional, List, Union
from .exceptions import (
    CyberArithmeticException, CyberU8ComparingException,
    CyberNotSupportedException
)


class U8:
    """
    The Saint He's specific type.
    """
    def __init__(self, value: Optional[Union[List[int], int]] = None):
        if value is None:
            self.value = []
        elif isinstance(value, int):
            self.value = [value]
        elif isinstance(value, list):
            self.value = value
        else:
            raise CyberNotSupportedException('u8 can only contain integers')

    def __str__(self) -> str:
        return ' | '.join(str(element) for element in self.value)

    def __repr__(self):
        return str(self)

    def __mul__(self, other: 'U8'):
        a, b = self.value, other.value
        # Makes a the shorter list
        if len(a) > len(b):
            a, b = b, a
        expected_length = len(b)
        a += [0] * (expected_length - len(a))
        return U8(sum(a[i] * b[i] for i in range(expected_length)))

    def __neg__(self):
        return U8([-v for v in self.value])

    def increment(self):
        self.value = [v+1 for v in self.value]

    def __eq__(self, other):
        if isinstance(other, U8):
            return self == other.value

        if isinstance(other, list):
            if len(other) != len(self.value):
                return False
            return all(self.value[i] == other[i] for i in range(len(other)))

        raise CyberU8ComparingException(f'cannot compare u8 with {type(other)}')

    def __sub__(self, other: 'U8'):
        if len(other.value) == 1:
            # Normal subtraction.
            return U8([v - other.value[0] for v in self.value])

        if len(other.value) == len(self.value):
            # Vector subtraction.
            return U8([self.value[i] - other.value[i] for i in range(len(self.value))])

        raise CyberArithmeticException(f'illegal operation: {self} - {other}')

    def __add__(self, other: 'U8'):
        a, b = self, other

        if len(a.value) == 1:
            a, b = b, a

        if len(b.value) == 1:
            # Normal addition.
            return U8([v + b.value[0] for v in a.value])

        if len(a.value) == len(b.value):
            # Vector addition.
            return U8([a.value[i] + b.value[i] for i in range(len(a.value))])

        raise CyberArithmeticException(f'illegal operation: {self} + {other}')

    def __getitem__(self, subscripts: 'U8'):
        # Like the operation of sublist.
        # And Saint He likes arrays whose subscript start from 1.
        return U8([self.value[i-1] for i in range(1, len(self.value) + 1) if i in subscripts.value])

    def __setitem__(self, subscripts: 'U8', value: 'U8'):
        if len(value.value) > 1:
            raise CyberNotSupportedException('no high dimension u8')
        if len(value.value) == 0:
            raise CyberNotSupportedException('you must set u8 with single value')
        val = value.value[0]

        # Set all elements if subscript is single 0.
        if subscripts == [0]:
            self.value = [val] * len(self.value)
            return

        # Set the elements one by one.
        for subscript in subscripts.value:
            if subscript == 0:
                raise CyberNotSupportedException('subscript 0 is designed for setting all elements,'
                                                 'you should write like array[0] = 10')
            self.value[subscript-1] = val
