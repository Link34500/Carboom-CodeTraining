def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    return tuple(int(hex[ih:ih + 2], 16) for ih in (0, 2, 4))