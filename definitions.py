from typing import Union

Iterables = Union[list | tuple | set]
Simple = Union[int | float | complex | str | bytes]
DataTypes = Union[Simple | Iterables | bool]