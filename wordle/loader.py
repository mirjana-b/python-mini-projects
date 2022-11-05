def is_good_word(word):
    if len(word) != 5:
        return False

    if not word.isalpha():
        return False

    if not word.islower():
        return False

    return True

def load_words(file_name):
    words = []

    with open(file_name, "rt") as f:
        words = (word.strip() for word in f)
        words = [word for word in words if is_good_word(word)]

    return words