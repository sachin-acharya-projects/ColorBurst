from ColorBurst import ColorBurst, Colors, Decorations

if __name__ == '__main__':
    color_print = ColorBurst()
    
    color_print.colorize("Hello", "World", color=Colors.RED, background=Colors.GREEN, decoration=Decorations.ITALIC)
    color_print.RESET
    
    color_print.init(autoreset=True)
    color_print.colorize("Hello", "World", color=Colors.YELLOW, decoration=Decorations.RAPID_BLINK)