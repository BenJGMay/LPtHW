# We need

# A way to handle errors

class ParserError(Exception):
    pass

# A Sentence object to put things in.

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

# A way to loop through a list of scanned words



# A way to "peek" at a potential tuple so as to make desicions

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# A way to "match" different types of tuples we expect in our Subject,
# Verb, Object setup

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# A way to skip things we don't care about like stop words

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

# Parsers

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

if __name__ == "__main__":
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    print("Sentence is 'run north'")
    print('Verb is', x.verb)
    print("Object is", x.object)
