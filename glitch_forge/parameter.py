from typing import Generic, TypeVar

T = TypeVar("T", int, float, str, bool)


class Param(Generic[T]):
    val: T | None
    tooltip: str | None
    placeholder: str | None
    label: str
    var_type: type[T]
    min_val: T | None
    max_val: T | None

    def __init__(
        self,
        val: T | None,
        var_type: type[T],
        label: str | None,
        min_val: T | None = None,
        max_val: T | None = None,
        tooltip: str | None = None,
        placeholder: str | None = None,
    ):
        self.tooltip = tooltip
        self.placeholder = placeholder
        self.label = label
        self.val = val
        self.var_type = var_type
        self.min_val = min_val
        self.max_val = max_val
