def text_to_braille(text):
    """
    Converts plain text to Braille Unicode symbols.

    Args:
        text (str): The input text to convert to Braille.

    Returns:
        str: The converted Braille text.
    """
    braille_dict = {
        "a": "⠁",
        "b": "⠃",
        "c": "⠉",
        "d": "⠙",
        "e": "⠑",
        "f": "⠋",
        "g": "⠛",
        "h": "⠓",
        "i": "⠊",
        "j": "⠚",
        "k": "⠅",
        "l": "⠇",
        "m": "⠍",
        "n": "⠝",
        "o": "⠕",
        "p": "⠏",
        "q": "⠟",
        "r": "⠗",
        "s": "⠎",
        "t": "⠞",
        "u": "⠥",
        "v": "⠧",
        "w": "⠺",
        "x": "⠭",
        "y": "⠽",
        "z": "⠵",
        "1": "⠼⠁",
        "2": "⠼⠃",
        "3": "⠼⠉",
        "4": "⠼⠙",
        "5": "⠼⠑",
        "6": "⠼⠋",
        "7": "⠼⠛",
        "8": "⠼⠓",
        "9": "⠼⠊",
        "0": "⠼⠚",
        " ": " ",
        ".": "⠲",
        ",": "⠂",
        "?": "⠦",
        "!": "⠖",
        "-": "⠤",
        ":": "⠒",
        ";": "⠆",
        "(": "⠶",
        ")": "⠶",
        "'": "⠄",
        '"': "⠐⠦",
        "/": "⠌",
    }

    braille_text = "".join(braille_dict.get(char.lower(), "") for char in text)
    return braille_text
