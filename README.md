# ColorBurst - Stylish Output
  ColorBurst is a python module that provide method to print stylish text onto console without any setups. For example, you can print colored text or text with colored background or different styled text like bold, underlined, etc or with all these property with specified color and style for each

## Table of Contents
- [Installation](#installation "Installation")
- [Methods](#Methods "Methods")
  - [Colors](#Colors "Colors")
  - [Decorations](#Decorations "Decorations")
  - [TextProperty](#TextProperty "TextProperty")
  - [ColorBurst](#ColorBurst "ColorBurst")
- [Code](#Code "Code")
## Installation
  You can install this package using `pip` or directly from the github

  **Installing with `pip`**
  ```powershell
  pip install ChromaticColorBurst
  ```

  **Installing Directly from GitHub**
  ```powershell
  pip install git+https://github.com/sachin-acharya-projects/ColorBurst.git@master
  ```

  Or you can even download wheel file from [dist](/dist) folder and install it using
  ```powershell
  pip install wheel-file-name.whl
  ```
## Methods
  This package provide three classes which are Colors, Decorations and ColorBurst
#### Colors
  This is a namespace class that contains valid values for color and background parameter for ColorBurst.colorize method
  ````python
    Colors.RED # This equivalent to string 'RED'
  ````
#### Decorations
  This class contains valid values for decoration parameter for ColorBurst.colorize method
  ```python
  Decorations.BOLD # This equivalent to string 'BOLD'
  ```
#### TextProperty
  This is a dataclass that can contain values for different property for text like color, background and decoration
  *Usages*
  ```python
  # To access value
  TextProperty.color # returns default color value i.e. None if none assigned before

  # To change value
  TextPropery(color = 'RED').color # returns 'RED'
  ```
  There are three data kind it holds
  color of type `Colors`
  background of type `Colors`
  and decoration of type `Decorations`
#### ColorBurst
  This is the main class that can be used to print styled text onto console(Terminals). This class provides following three methods

```python
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
```
## Code
  ```python
    # Importing required modules
    from ColorBurst import ColorBurst, Colors, Decorations, TextProperty

    # Initializing ColorBurst
    cb = ColorBurst(autoreset=True)

    # Printing Text with color RED and Background YELLOW
    cb.print_burst('Hello', 'World', properties=TextProperty(Colors.RED, Colors.YELLOW))

    # Resetting
    cb.RESET

    # Updating autoreset property
    cb.update(autoreset=True)

    # Printing Text with color GREEN
    cb.print_burst('Hello', 'World', properties=TextProperty(Colors.GREEN))

    # Printing Text with color YELLOW
    cb.print_burst('Hi', properties={
        'color': "YELLOW"
    })

    # Taking styled input
    cb.input_burst("What is your name? ", TextProperty(background='GREEN', color='BLUE'), TextProperty(decoration=Decorations.ITALIC, color='RED'))
  ```

[Go Up](#table-of-contents "Go Up")
