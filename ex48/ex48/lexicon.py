
lexicon = [('direction', 'north'), ('direction', 'east'),
            ('direction', 'west'), ('direction', 'south'),
            ('noun', 'bear'),
            ('stop', 'the'), ('stop', 'in'), ('stop', 'of'),
            ('verb', 'go'), ('verb', 'kill'), ('verb', 'eat')
            ]


def scan(input):
    global lexicon
#    Scan takes an input and turns it into a list of words
    words = input.split()
#    print(words)
    sentence = []
#    Scan searches in lexicon for each of these words
    for word in words:
#        print("Debug word is >>>>", word)
        for pair in lexicon:
            if word in pair:
#                print(">>> Word is in", pair)
#               append tuple pair to sentence
                sentence.append(pair)

#    print(">>> Sentence is", sentence)

    return sentence


# scan('north')
# scan('north south east')
# scan(first_word)
# scan(' north west')
