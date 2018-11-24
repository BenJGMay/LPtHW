from nose.tools import *
from ex49 import parser

def test_Sentence():
    s1 = parser.Sentence(('subject', 'Player'), ('verb', 'runs'),
                        ('direction', 'north'))
    assert s1.verb == 'runs'
    assert s1.subject == 'Player'
    assert s1.object == 'north'

def test_peek():
    assert_equal(parser.peek([]), None) # Empty List
    result = parser.peek([('verb', 'run'), ('direction', 'north')])
    assert_equal(result, 'verb')

def test_match():
    assert_equal(parser.match([], 'verb'), None) # Nothing expected
    result = parser.match([('verb', 'run'), ('direction', 'north')], 'verb')
    assert_equal(result, ('verb', 'run'))
    result = parser.match([('verb', 'run'), ('direction', 'north')], 'noun')
    assert result == None

def test_skip():
    word_list_eg = [('verb', 'run'),
                 ('direction', 'north'),
                 ('stop', 'with'),
                 ('stop', 'the'),
                 ('noun', 'bear')]

    assert_equal(parser.skip(word_list_eg, 'stop'), None)

def test_parse_verb():
    word_list_1 = [('verb', 'run'),
                 ('direction', 'north'),
                 ('stop', 'with'),
                 ('stop', 'the'),
                 ('noun', 'bear')]
    result = parser.parse_verb(word_list_1)
    assert_equal(result, ('verb', 'run')) # Next word is a verb

    word_list_2 = [('stop', 'the'),
                   ('verb', 'run'),
                   ('direction', 'north'),
                   ('stop', 'with'),
                   ('stop', 'the'),
                   ('noun', 'bear')]
    result = parser.parse_verb(word_list_2)
    assert_equal(result, ('verb', 'run')) # Next word is a verb, skip the 'stop'

    word_list_3 = [('noun', 'cats'),
                   ('verb', 'run'),
                   ('direction', 'north'),
                   ('stop', 'with'),
                   ('stop', 'the'),
                   ('noun', 'bears')]

    word_list_4 = [('verb', 'run'),
                 ('direction', 'south'),
                 ('stop', 'with'),
                 ('stop', 'the'),
                 ('noun', 'boss')]
    assert_raises(parser.ParserError, parser.parse_verb, word_list_3)
#   This below will work as the verb has been popped off of wl1 by this point
    assert_raises(parser.ParserError, parser.parse_verb, word_list_1)

def test_parse_object():
    word_list_1 = [('noun', 'dog'),
                 ('verb', 'go'),
                 ('direction', 'north'),
                 ('stop', 'with'),
                 ('noun', 'bear')]
    result = parser.parse_object(word_list_1)
    assert_equal(result, ('noun', 'dog')) # Next word is a noun

    word_list_2 = [('stop', 'the'),
                   ('noun', 'cows'),
                   ('verb', 'go'),
                   ('direction', 'north'),
                   ('stop', 'with'),
                   ('noun', 'bears')]
    result = parser.parse_object(word_list_2)
    assert_equal(result, ('noun', 'cows')) # Next word is a noun, skip the 'stop'

    word_list_3 = [('adverb', 'quickly'),
                   ('verb', 'run'),
                   ('direction', 'north'),
                   ('stop', 'with'),
                   ('stop', 'the'),
                   ('noun', 'bears')]

    assert_raises(parser.ParserError, parser.parse_object, word_list_3)

def test_parse_subject():
    word_list_1 = [('noun', 'dog'),
                 ('verb', 'go'),
                 ('direction', 'north'),
                 ('stop', 'with'),
                 ('noun', 'bear')]
    result = parser.parse_subject(word_list_1)
    assert_equal(result, ('noun', 'dog')) # Next word is a noun

    word_list_2 = [('stop', 'the'),
                   ('noun', 'cows'),
                   ('verb', 'go'),
                   ('direction', 'north'),
                   ('stop', 'with'),
                   ('noun', 'bears')]
    result = parser.parse_subject(word_list_2)
    assert_equal(result, ('noun', 'cows')) # Next word is a noun, skip the 'stop'

    word_list_3 = [('adverb', 'quickly'),
                   ('verb', 'run'),
                   ('direction', 'north'),
                   ('stop', 'with'),
                   ('stop', 'the'),
                   ('noun', 'bears')]

    assert_raises(parser.ParserError, parser.parse_subject, word_list_3)

    word_list_4 = [('verb', 'run'),
                 ('direction', 'north'),
                 ('stop', 'with'),
                 ('stop', 'the'),
                 ('noun', 'bear')]
    result = parser.parse_subject(word_list_4)
    assert_equal(result, ('noun', 'player'))
#   Next word is a verb, so we return player

def test_parse_sentence():
    word_list_1 = [('verb', 'run'),
                 ('direction', 'north'),
                 ('stop', 'with'),
                 ('stop', 'the'),
                 ('noun', 'bear')]
    result = parser.parse_sentence(word_list_1)
    assert_equal(result.subject, ('player'))
    assert_equal(result.verb, ('run'))
    assert_equal(result.object, ('north'))
