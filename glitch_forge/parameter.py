from typing import Generic, TypeVar

T = TypeVar("T", int, float, str, bool)


class Param(Generic[T]):
    """
    A generic parameter class that encapsulates a value, its type, and additional metadata.
    Attributes:
        val (T | None): The current value of the parameter. Can be None.
        tooltip (str | None): An optional tooltip providing additional information about the parameter.
        placeholder (str | None): An optional placeholder text for the parameter.
        label (str): A label describing the parameter.
        var_type (type[T]): The type of the parameter's value.
        min_val (T | None): The minimum allowable value for the parameter. Can be None.
        max_val (T | None): The maximum allowable value for the parameter. Can be None.
    Args:
        val (T | None): The initial value of the parameter. Can be None.
        var_type (type[T]): The type of the parameter's value.
        label (str | None): A label describing the parameter. If None, no label is assigned.
        min_val (T | None, optional): The minimum allowable value for the parameter. Defaults to None.
        max_val (T | None, optional): The maximum allowable value for the parameter. Defaults to None.
        tooltip (str | None, optional): An optional tooltip providing additional information about the parameter. Defaults to None.
        placeholder (str | None, optional): An optional placeholder text for the parameter. Defaults to None.
    """

    val: T | None
    """The current value of the parameter"""
    tooltip: str | None
    """An optional tooltip providing additional information about the parameter on hover"""
    placeholder: str | None
    """An optional placeholder text for the parameter"""
    label: str
    """A label describing the parameter"""
    var_type: type[T]
    """The type of the parameter's value"""
    min_val: T | None
    """The minimum allowable value for the parameter"""
    max_val: T | None
    """The maximum allowable value for the parameter"""

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
