from typing import Optional, List
from .exceptions import CyberSubtractionException, CyberU8ComparingException


class U8:
    """
    The Saint He's specific type.
    """
    def __init__(self, value: Optional[List[int]] = None):
        self.value = [] if value is None else value

    def __str__(self) -> str:
        return ' | '.join(str(element) for element in self.value)

    def __repr__(self):
        return str(self)

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

        raise CyberSubtractionException(f'illegal subtraction: {self.value} - {other.value}')
