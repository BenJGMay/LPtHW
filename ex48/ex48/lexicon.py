
lexicon = [('verb', 'go'), ('direction', 'north'), ('direction', 'west')]


def scan(input):
    global lexicon
#    Scan takes an input and turns it into a list of words
    words = input.split()
    sentence = []
#    Scan searches in lexicon for each of these words
    for word in words:
        for pair in lexicon:
            if word in pair:
#                print(">>> Word is in", pair)
#               append tuple pair to sentence
                sentence.append(pair)
#                print(">>> Sentence is", sentence)

    return sentence


scan('north')
# scan(first_word)
# scan(' north west')
