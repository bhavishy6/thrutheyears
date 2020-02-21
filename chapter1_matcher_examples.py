import spacy

# Import the Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")


def matcher_examples():

    # Initialize the matcher with the shared vocab
    matcher = Matcher(nlp.vocab)

    # Add the pattern to the matcher
    pattern = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]
    matcher.add('IPHONE_PATTERN', None, pattern)
    pattern2 = [{'LEMMA': 'buy'}, {'POS': 'PRON'}]
    matcher.add('BUYING_PATTERN', None, pattern2)
    pattern3 = [
        {'IS_DIGIT': True},
        {'LOWER': 'fifa'},
        {'LOWER': 'world'},
        {'LOWER': 'cup'},
        {'IS_PUNCT': True}
    ]
    matcher.add('FIFA_PATTERN', None, pattern3)

    pattern4 = [
        {'LEMMA': 'love', 'POS': 'VERB'},
        {'POS': 'NOUN'}
    ]
    matcher.add('LOVED_VERB_PATTERN', None, pattern4)


    pattern4 = [
        {'LEMMA': 'love', 'POS': 'NOUN'},
        {'POS': 'ADP'},
        {'POS': 'NOUN'}
    ]
    matcher.add('LOVED_NOUN_PATTERN', None, pattern4)

    pattern5 = [
        {'LEMMA': 'buy'},
        {'POS': 'DET', 'OP': '?'},  # optional: match 0 or 1 times
        {'POS': 'NOUN'}
    ]
    matcher.add('OPERATOR_QUANTIFIERS', None, pattern5)

    # Process some text
    doc = nlp("New iPhone X release date leaked, I will be buying it... 2018 FIFA World Cup: France won!... I loved dogs but now I love cats more... I have love for cats... I bought a smartphone. Now I'm buying apps.")
    for token in doc:
        print(token.text, token.pos_)
    # Call the matcher on the doc
    matches = matcher(doc)

    # Iterate over the matches
    for match_id, start, end in matches:
        # Get the matched span
        matched_span = doc[start:end]
        print(str(match_id) +", "+ matched_span.text)
    
    
    print(nlp.vocab.strings[6336049367242486597])


def find_str_data(str):
    doc = nlp(str)

    for token in doc:
        print("{:<12}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("text", "lemma_", "pos_", "tag_", "dep_", "shape_" "is_alpha", "is_stop"))
        print("{:<12}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop))

str = 'This is a test sentence. I am a Man. He lied to You. I am weary. The man is a fool.'

find_str_data(str)

print(spacy.explain('det'))