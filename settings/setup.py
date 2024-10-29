class Theme():

    BLACK =         "#2B2B2B"
    MID_GRAY =      "#BABABA"
    LIGHT_GRAY =    "#EAEAEA"
    WHITE =         "#FFFFFF"

class Layout():

    def _get_canvas_width(window_width, window_height, toolbar_height):
        canvas_scale = abs((toolbar_height / window_height) - 1)

        return int(round(window_width * canvas_scale))

    # Define private dimensions to be used for public class attributes.
    _WINDOW_WIDTH = 1200
    _WINDOW_HEIGHT = 650
    _TOOLBAR_HEIGHT = 100
    _FOOTER_HEIGHT = 20
    _CANVAS_HEIGHT = _WINDOW_HEIGHT - _TOOLBAR_HEIGHT - _FOOTER_HEIGHT
    _CANVAS_WIDTH = _get_canvas_width(_WINDOW_WIDTH, _WINDOW_HEIGHT, _TOOLBAR_HEIGHT)

    # Toolbar frames
    _LOAD_SAVE_WIDTH = 84
    _DRAW_WIDTH = 193
    _COLOR_WIDTH = 135
    _BRUSH_STYLE_WIDTH = 181
    _DRAW_SHAPE_WIDTH = 181
    _UNDO_REDO_WIDTH = 59
    

    
    

    # Define padding for frame components.
    _LARGE_PADDING = 6
    _MEDIUM_PADDING = 4
    _SMALL_PADDING = 2

    # Public attributes.
    DEFAULT_BUTTON_HEIGHT = 35
    DEFAULT_PADDING = 6
    MEDIUM_PADDING = 4
    DEFAULT_TOOL_HEIGHT = _TOOLBAR_HEIGHT - (DEFAULT_PADDING * 2)

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

    load_save = {
        "FRAME_WIDTH":_LOAD_SAVE_WIDTH,
        "FRAME_HEIGHT":_TOOLBAR_HEIGHT,
        "X":0,
        "Y":0,
        "BUTTON_WIDTH":66,
        "BUTTON_PADDING":11,
        "SECOND_ROW_Y":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "BG_WIDTH":_LOAD_SAVE_WIDTH - DEFAULT_PADDING,
        "BG_HEIGHT":DEFAULT_TOOL_HEIGHT
    }

    draw = {
        "FRAME_WIDTH":_DRAW_WIDTH,
        "FRAME_HEIGHT":_TOOLBAR_HEIGHT,
        "X":_LOAD_SAVE_WIDTH,
        "Y":0,
        "BUTTON_WIDTH":DEFAULT_BUTTON_HEIGHT,
        "BUTTON_PADDING":11,
        "SECOND_ROW_Y":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "BG_WIDTH":_DRAW_WIDTH - DEFAULT_PADDING,
        "BG_HEIGHT":DEFAULT_TOOL_HEIGHT,
        "ERASER_BUTTON_X":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "SLIDER_BG_X":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "SLIDER_BG_WIDTH":134,
        "SIZE_BG_X":(DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING) * 2 + 11,
        "SIZE_BG_WIDTH":93,
        "SIZE_SLIDER_X":11 + DEFAULT_BUTTON_HEIGHT + (DEFAULT_PADDING * 2),
        "SIZE_SLIDER_Y":11+ DEFAULT_PADDING,
        "SIZE_SLIDER_WIDTH":122,
        "SIZE_SLIDER_HEIGHT":25,
        "TEXT_BOX_X":(DEFAULT_BUTTON_HEIGHT * 3) + (DEFAULT_PADDING * 2) + MEDIUM_PADDING + 11,
        "TEXT_BOX_Y":11 + DEFAULT_BUTTON_HEIGHT + (DEFAULT_PADDING * 2),
        "TEXT_BOX_WIDTH":49,
        "TEXT_BOX_HEIGHT":23,
    }

    color = {
        "FRAME_WIDTH":_COLOR_WIDTH,
        "FRAME_HEIGHT":_TOOLBAR_HEIGHT,
        "X":_LOAD_SAVE_WIDTH + _DRAW_WIDTH,
        "Y":0,
        "BUTTON_WIDTH":DEFAULT_BUTTON_HEIGHT,
        "BUTTON_PADDING":11,
        "SECOND_ROW_Y":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "BG_WIDTH":_COLOR_WIDTH - DEFAULT_PADDING,
        "BG_HEIGHT":DEFAULT_TOOL_HEIGHT
    }

    brush_style = {
        "FRAME_WIDTH":_BRUSH_STYLE_WIDTH,
        "FRAME_HEIGHT":_TOOLBAR_HEIGHT,
        "X":_LOAD_SAVE_WIDTH + _DRAW_WIDTH + _COLOR_WIDTH,
        "Y":0,
        "BUTTON_WIDTH":DEFAULT_BUTTON_HEIGHT,
        "BUTTON_PADDING":11,
        "SECOND_ROW_Y":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "BG_WIDTH":_BRUSH_STYLE_WIDTH - DEFAULT_PADDING,
        "BG_HEIGHT":DEFAULT_TOOL_HEIGHT
    }

    draw_shape = {
        "FRAME_WIDTH":_DRAW_SHAPE_WIDTH,
        "FRAME_HEIGHT":_TOOLBAR_HEIGHT,
        "X":_LOAD_SAVE_WIDTH + _DRAW_WIDTH + _COLOR_WIDTH + _BRUSH_STYLE_WIDTH,
        "Y":0,
        "BUTTON_WIDTH":DEFAULT_BUTTON_HEIGHT,
        "BUTTON_PADDING":11,
        "SECOND_ROW_Y":11 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "BG_WIDTH":_DRAW_SHAPE_WIDTH - DEFAULT_PADDING,
        "BG_HEIGHT":DEFAULT_TOOL_HEIGHT
    }

    undo_redo = {
        "FRAME_WIDTH":_UNDO_REDO_WIDTH,
        "FRAME_HEIGHT":_TOOLBAR_HEIGHT,
        "X":_LOAD_SAVE_WIDTH + _DRAW_WIDTH + _COLOR_WIDTH + _BRUSH_STYLE_WIDTH + _DRAW_SHAPE_WIDTH,
        "Y":0,
        "BUTTON_WIDTH":DEFAULT_BUTTON_HEIGHT,
        "BUTTON_PADDING":12,
        "SECOND_ROW_Y":12 + DEFAULT_BUTTON_HEIGHT + DEFAULT_PADDING,
        "BG_WIDTH":_UNDO_REDO_WIDTH - (DEFAULT_PADDING * 2),
        "BG_HEIGHT":DEFAULT_TOOL_HEIGHT
        
    }

    canvas = {
        "WIDTH":_CANVAS_WIDTH,
        "HEIGHT":_CANVAS_HEIGHT,
        "X":(_WINDOW_WIDTH - _CANVAS_WIDTH) / 2,
        "Y":_TOOLBAR_HEIGHT
    }

    footer = {
        "WIDTH":_WINDOW_WIDTH,
        "HEIGHT":_FOOTER_HEIGHT,
        "X":0,
        "Y":_WINDOW_HEIGHT - _FOOTER_HEIGHT
    }

        

