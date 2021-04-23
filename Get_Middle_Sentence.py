# Get Middle Sentence
# author @Yichen

def getMiddleSentence(s):
    s_original = s
    s = s.replace("!", ".")
    s = s.replace("?", ".")
    dot_count = s.count(".")
    if dot_count != 3:
        print("Improper structure")
    else:
        dot_1_index = s.find(".")
        first_sentence = s[0: dot_1_index+1]
        last_two_sentence = s[dot_1_index+1: len(s)]
        dot_2_index = last_two_sentence.find(".") + len(first_sentence)
        print(s_original[dot_1_index+1 : dot_2_index+1])

if __name__ == '__main__':
    getMiddleSentence('Hi.What!How do you do?')
