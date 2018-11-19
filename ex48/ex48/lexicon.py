numbers = range(1, 1999999999)

lexicon = {'north': 'direction', 'east': 'direction',
           'west': 'direction', 'south': 'direction',
           'bear': 'noun', 'princess': 'noun',
           numbers: 'number',
           'the': 'stop', 'in': 'stop', 'of': 'stop', 'with': 'stop',
           'go': 'verb', 'kill': 'verb', 'eat': 'verb', 'punch': 'verb',
           }


def convert_number(s):
    # print(">>>> Enter convert number")
    try:
        return int(s)
        # print(">>>> ", s, "as INT")
    except ValueError:
        # print(">>>> Value Error, returning original")
        return None


def scan(input):
    global lexicon
    # Scan takes an input and turns it into a list of words
    words = input.split()
    # print(words)
    sentence = []
    # Scan searches in lexicon for each of these words
    for word in words:
        # print("Debug word is >>>>", word)
        if word.lower() in lexicon:
            # print(">>>> ", word, "is in lexicon")
            # we set the word type as the value for the word key
            word_type = lexicon.get(word.lower())
            # we append a tuple using word_type and word as our values
            sentence.append((word_type, word.lower()))
        else:
            # Attempt to turn word into an Int
            number = convert_number(word)
            # If so, it must be a number
            if number is not None:

                word_type = 'number'
                sentence.append((word_type, number))

            else:
                word_type = 'error'
                sentence.append((word_type, word))

#    print(">>> Sentence is", sentence)

    return sentence


if __name__ == "__main__":
    print(">>>> Running as main.")
    scan('north')
    scan('north south east')
    scan(' north west')
    scan('1234 3 cow')
