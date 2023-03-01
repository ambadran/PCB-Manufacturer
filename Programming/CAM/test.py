from enum import Enum


class Mode(Enum):
    Select = 0
    Deselect = 1


print(type(Mode.Select))
print(type(Mode.Select.value))
print(Mode.Select.value)
print(Mode.Select.value)
