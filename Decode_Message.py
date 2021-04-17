# Decode Message with Uppercase Letters
# author @Yichen

def onlyUpper(text):
    if len(text) == 0:
        return ""
    elif len(text) == 1 and text[0].isupper():
        return text[0]
    elif len(text) == 1 and text[0].isupper()!=True:
        return ""
    else:
        result = onlyUpper(text[0]) + onlyUpper(text[1:len(text)])
    return result





if __name__ == '__main__':
    print(onlyUpper('respect'))

