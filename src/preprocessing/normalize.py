import re
import ftfy

from .emoji_dict import EMOJI_DICT
from .teencode_dict import TEENCODE_DICT

# Unicode
def normalize_unicode(text):
    if not isinstance(text, str):
        text = str(text)

    text = ftfy.fix_text(text)
    text = text.strip()

    return text

# Emoji
def normalize_emoji(text):
    # Thay emoji bằng nhãn có khoảng trắng xung quanh
    for emoji_char, meaning in EMOJI_DICT.items():
        text = text.replace(emoji_char, f" {meaning} ")

    # Chuẩn hóa khoảng trắng
    text = re.sub(r"\s+", " ", text).strip()

    # Gộp các nhãn emoji giống nhau đứng liên tiếp
    words = text.split()

    result = []
    for word in words:
        if not result or result[-1] != word:
            result.append(word)

    return " ".join(result)

# Teencode
def normalize_teencode(text):
    words = re.findall(r"\w+|[^\w\s]", text)

    words = [
        TEENCODE_DICT.get(word.lower(), word)
        for word in words
    ]

    return " ".join(words)

# Repeated Character
def normalize_repeated_characters(text):
    # chữ cái lặp
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    # dấu câu lặp
    text = re.sub(r"([!?.,])\1+", r"\1", text)

    return text

# Punctuation
def normalize_punctuation(text):
    import re

    text = re.sub(r"!{2,}", "!", text)
    text = re.sub(r"\?{2,}", "?", text)
    text = re.sub(r"\.{2,}", ".", text)

    # xoá dấu rác
    text = re.sub(r"[:;,@]", " ", text)

    # chuẩn hóa khoảng trắng
    text = re.sub(r"\s+", " ", text).strip()

    return text