import sys

sys.setrecursionlimit(10000)


def compare_char(reg_char, word_char):
    return reg_char == word_char or bool(reg_char == '.' and word_char) or not reg_char


def compare(reg, word):
    if not reg:
        return True
    if not word:
        return reg == '$'
    elif reg[0] == '\\':
        return compare(reg[1:], word)
    elif len(reg) > 1 and reg[1] == '?':
        return question_mark(reg, word)
    elif len(reg) > 1 and reg[1] == '*':
        return asterisk(reg, word)
    elif len(reg) > 1 and reg[1] == '+':
        return plus(reg, word)
    elif compare_char(reg[0], word[0]):
        return compare(reg[1:], word[1:])
    else:
        return False


def asterisk(reg, word):
    if reg[0] == word[0] or reg[0] == '.' and word[0] != word[1]:
        return compare(reg, word[1:])
    else:
        return compare(reg[2:], word)


def question_mark(reg, word):
    if reg[0] == word[0] or reg[0] == '.':
        return compare(reg[2:], word[1:])
    else:
        return compare(reg[2:], word)


def plus(reg, word):
    if (reg[0] == word[0] or reg[0] == '.') and (len(word) == 1 or word[0] != word[1]):
        return compare(reg[2:], word[1:])
    else:
        return compare(reg, word[1:])


def regex_compare(reg, word):
    if not reg:
        return True
    elif not word:
        return False
    elif reg[0] == '^':  # check for begin-pattern '^'
        return compare(reg[1:], word)
    elif compare(reg, word):
        return True
    else:
        return regex_compare(reg, word[1:])


if __name__ == "__main__":
    regex, text = (input().split('|'))
    print(regex_compare(regex, text))
