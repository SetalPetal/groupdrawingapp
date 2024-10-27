class Theme():

    BLACK =         "#2B2B2B"
    MID_GRAY =      "#BABABA"
    LIGHT_GRAY =    "#EAEAEA"
    WHITE =         "#FFFFFF"

class Layout():
    # Define private dimensions to be used for public class attributes.
    _TOOLBAR_HEIGHT = 76
    _CANVAS_HEIGHT = 700
    _FOOTER_HEIGHT = 20
    _WINDOW_WIDTH = 1200
    _WINDOW_HEIGHT = _TOOLBAR_HEIGHT + _CANVAS_HEIGHT + _FOOTER_HEIGHT

    # Define padding for frame components.
    _LARGE_PADDING = 6
    _MEDIUM_PADDING = 4
    _SMALL_PADDING = 2

    # Frame component dimensions.
    _SAVE_LOAD_WIDTH = 55
    _SAVE_LOAD_HEIGHT = 62

    # Default widget dimensions
    _DEFAULT_WIDGET_HEIGHT = 25

    root = {
        "SIZE":f"{_WINDOW_WIDTH}x{_WINDOW_HEIGHT}",
        "WIDTH":_WINDOW_WIDTH,
        "HEIGHT":_WINDOW_HEIGHT
    }

    toolbar = {
        "WIDTH":_WINDOW_WIDTH,
        "HEIGHT":_TOOLBAR_HEIGHT,
        "X":0,
        "Y":0
    }

    save_load = {
        "WIDTH":_SAVE_LOAD_WIDTH,
        "HEIGHT":_TOOLBAR_HEIGHT - (_MEDIUM_PADDING * 2),
        "X":_LARGE_PADDING,
        "Y":_LARGE_PADDING,
        "BUTTON_WIDTH":_SAVE_LOAD_WIDTH - (_MEDIUM_PADDING * 2),
        "BUTTON_HEIGHT":_DEFAULT_WIDGET_HEIGHT
    }

    canvas = {
        "WIDTH":_WINDOW_WIDTH,
        "HEIGHT":_CANVAS_HEIGHT,
        "X":0,
        "Y":toolbar["HEIGHT"]
    }

        


