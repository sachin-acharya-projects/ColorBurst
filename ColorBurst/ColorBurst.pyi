from typing import Any, Callable
from .classes import *

__all__ = ['ColorBurst', 'Colors', 'Decorations', 'TextProperty']

class ColorBurst:
    def __init__(self, default_property: TextProperty | None = TextProperty(), autoreset: bool = False) -> None:
        """Display styled text onto your console

        Args:
            default_property (TextProperty | None, optional): Unless updated, all of the outout will have this property. Defaults to TextProperty().
            autoreset (bool, optional): When set to True, after every output, style of buffer will be reset. Defaults to False.
        """
        ...
    def update(self, property_: TextProperty = TextProperty(), autoreset: bool = False):
        """Uodate the default property for all of the output

        Args:
            property_ (TextProperty, optional): This is the default property. Defaults to TextProperty().
            autoreset (bool, optional): Set to True to reset color buffer after every output. Defaults to False.
        """
        ...
    @property
    def RESET(self):
        """Reset persisting style
        """
        ...
    def input_burst(self, prompt: str = '', prompt_property: TextPropertyDict | TextProperty = TextProperty(), text_property: TextPropertyDict |  TextProperty = TextProperty(), type_: Callable = None) -> Any:
        """You can now have stylish input from users. You can set color, decoration and background for prompt as well as the user-input area

        Args:
            prompt (str, optional): This is the prompt for the input. Defaults to ''.
            prompt_property (TextPropertyDict | TextProperty, optional): Property for prompt. Defaults to TextProperty().
            text_property (TextPropertyDict | TextProperty, optional): Property for user-input area. Defaults to TextProperty().
            type_ (Callable, optional): The data-type in which you want your input to be casted into. Defaults to None.

        Returns:
            Any: return string if type_ parameter is None otherwise the type provided by type_ param.
        """
        ...
    def print_burst(self, *args, properties: TextPropertyDict | TextProperty = None, separator = None, end = None):
        """Printout the stylish text onto the console

        Args:
            properties (TextPropertyDict | TextProperty, optional): Properties for the output text (use default property if None provided). Defaults to None.
            separator (_type_, optional): A separator that is used to separate multiple strings (use blank space as default value if None provided). Defaults to None.
            end (_type_, optional): Value to be provided after each printing statement (use \\n for default value). Defaults to None.
        """
        ...
    def get_property(self, color: str = '', background: str = '', decoration: str = '0') -> TextProperty:
        ...