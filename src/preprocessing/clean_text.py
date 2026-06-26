import re

# Remove URL
def remove_url(text):
    return re.sub(r"http\S+|www\S+|https\S+", "", text)

# Remove HTML
def remove_html(text):
    return re.sub(r"<.*?>", "", text)

# Remove hashtag
def remove_hashtag(text):
    return re.sub(r"#\w+", "", text)

# Remove extra whitespace
def remove_extra_spaces(text):
    return re.sub(r"\s+", " ", text).strip()

# Lowercase
def lowercase(text):
    return text.lower()

def clean_after_preprocess(text):
    # xóa ký tự rác còn sót
    text = re.sub(r"[:;,@]", " ", text)

    # gộp space
    text = re.sub(r"\s+", " ", text).strip()

    return text