import io

from typing import Callable


class Redirector(io.StringIO):
    def __init__(self, hook: Callable[[str], None]):
        super().__init__()
        self._hook = hook

    def write(self, s: str) -> int:
        result = super().write(s)
        self._hook(s)
        return result
