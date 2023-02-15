# ColorBurst - Stylish Output
ColorBurst is a python module that provide method to print stylish text onto console without any setups. For example, you can print colored text or text with colored background or different styled text like bold, underlined, etc or with all these property with specified color and style for each

## Table of Contents
- [Methods](#Methods "Methods")
 - [Colors](#Colors "Colors")
 - [Decorations](#Decorations "Decorations")
 - [ColorBurst](#ColorBurst "ColorBurst")
- [Code](#Code "Code")

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
#### ColorBurst
  This is the main class that can be used to print styled text onto console(Terminals). This class provides following three methods
1. **init(color: Colors = None, background: Colors = None, decoration: Decorations = None, autoreset = False)**
      This method is used to set or unset different parameter which are color, background and/or decoration as well as autoreset. This method can be used to preserve value for above parameter so they can be used later without having to pass paramter to colorize method explicitly
*Example*
```python
ColorBurst().init(
	color = Colors.RED,
	background = Colors.CYAN,
	decoration = Decorations.DOUBLY_UNDERLINE,
	autoreset = True
)
```
After calling init method like so, you can now simply call `ColorBurst().colorize("Hello", "World")` and it will print RED text with CYAN background with double underline. You can override these property for only one line by passing parameter explicitly or you can change these property for any next uses by re-using `init` method.  
   ```python
"""
	The code below will print YELLOW text with CYAN as background and DOUBLE UNDERLINE as Text Style
	CYAN as background and DOUBLE UNDERLINE as Text Style was stored in previous init method calls
"""
ColorBurst.colorize("Hello", "World", color=Colors.YELLOW)
```
Last parameter for this method, autoreset, if set to True, the color sequence will be terminated after line-break otherwise it will remains as is unless overriden or closing of terminal
```python
c = ColorBurst()
"""
The line below will print text with RED color but the foreground color will be kept RED even after the program is terminated. This can be override by using another color (New color will persist instead of RED) or closing the terminal.
"""
c.colorize("Hello", "World", color = 'RED') # color = Colors.RED
c.init(autoreset = True)
"""
The line below will print text will CYAN color and terminated the coloring sequence. That means this CYAN color will only be available for current line/row (outputted row).
"""
c.colorize("Hello", "There", color = 'CYAN') # Colors.CYAN
```
**Parameters**
 - color
 This parameter, type `Colors` represent foreground color. (Default: `None`)
 - background
 This parameter, type `Colors` represent background color. (Default: `None`)
 - decoration
 This parameter, type `Decorations` represent text style/decoration. (Default: `None`)
 - autoreset
 This parameter, type `Boolean` represent condition to autoreset after line break or not. (Default: `False`)
2. **colorize(*args, color: Colors = None, background: Colors = None, decoration: Decorations = None, separator = None, end = None)**  
	This method can be used to print stylish text onto screen.
````python
ColorBurst().colorize(
	"Hello", "World",
	color = Colors.RED,
	background = Colors.CYAN,
	decoration = Decorations.BOLD,
	separator = '-',
	end = '\n'
)
```
Above code will print bold 'Hello-World\n' onto screen with color RED and background CYAN.
__Parameters__
 - args (Type: `Tuple`)
 These are the positional arguments which will be printed out onto screen. (Default: `''`)
 - color (Type: `Colors`)
 Same as color parameter for `init` method. (Default: Terminals' default)
 - background (Type: `Colors`)
 Same as background for `init` method. (Default: Terminals' default)
 - decoration (Type: `Decorations`)
 Same as decoration parameter for `init` method. (Default: `Decorations.NORMAL`)
 - separator (Type: `String`)
 This parameter represent separating character for each data in args parameter. (similar to `sep` parameter of `print` statement). (Default:  `' '`)
 - end (Type: `String`)
 This parameter represent what to append at the end of the line. (Default: `\n`)
3. **RESET**
	This method is used to reset any text formatting done. This is used when `autoreset` is set to `False` and need to terminate coloring sequence.
*Example*
The code below will print text will RED color and this foreground color will be persistent as autoreset is set to False
```python
c = ColorBurst()
c.colorize('Text', color = 'RED')
```
Now if we use RESET method right after printing text, color sequence will be terminated and foreground color will be reverted to default
```python
c = ColorBurst()
c.colorize('Text', color = 'RED')
c.RESET # Omit parenthesis
```
This method is used to revert any formatting done to defaults.
## Code
```python
from ColorBurst import ColorBurst, Colors, Decorations
if __name__ == '__main__':
    color_print = ColorBurst()
	
    color_print.colorize("Hello", "World", color=Colors.RED, background=Colors.GREEN, decoration=Decorations.ITALIC)
    color_print.RESET
	
    color_print.init(autoreset=True)
    color_print.colorize("Hello", "World", color=Colors.YELLOW, decoration=Decorations.RAPID_BLINK)
```

[Go Up](#h1-colorburst-stylish-output "Go Up")