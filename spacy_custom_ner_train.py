
# Training additional entity types using spaCy
# https://gist.github.com/kaustumbh7/6dc0b909dbdfea4ae2428fb77e18273f#file-spacy_ner_custom_entities-py
from __future__ import unicode_literals, print_function
import pickle
# import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from joblib import Parallel, delayed
from functools import partial
from datetime import datetime
import en_core_web_lg

# spacy.require_gpu()
# New entity labels
# Specify the new entity labels which you want to add here
LABEL = ['I-geo', 'B-geo', 'I-art', 'B-art', 'B-tim', 'B-nat', 'B-eve', 'O', 'I-per', 'I-tim', 'I-nat', 'I-eve', 'B-per', 'I-org', 'B-gpe', 'B-org', 'I-gpe']

"""
geo = Geographical Entity
org = Organization
per = Person
gpe = Geopolitical Entity
tim = Time indicator
art = Artifact
eve = Event
nat = Natural Phenomenon
"""
# Loading training data 
with open ('ner_corpus_form.pickle', 'rb') as fp:
    TRAIN_DATA = pickle.load(fp)

# @plac.annotations(
#     model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
#     new_model_name=("New model name for model meta.", "option", "nm", str),
#     output_dir=("Optional output directory", "option", "o", Path),
#     n_iter=("Number of training iterations", "option", "n", int))

def main_train(model="en_core_web_lg", new_model_name='new_model', output_dir=None, n_iter=50):
    """Setting up the pipeline and entity recognizer, and training the new entity."""
    if model is not None:
        nlp = en_core_web_lg.load()  # load existing spacy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe('ner')

    for i in LABEL:
        ner.add_label(i)   # Add new entity labels to entity recognizer

    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.entity.create_optimizer()

    # Get names of other pipes to disable them during training to train only NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            starttime = datetime.now()
            print("Starting: " + str(starttime))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
                           losses=losses)
            print('Losses', losses)

#     with nlp.disable_pipes(*other_pipes):  # only train NER
#         batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
#         executor = Parallel(n_jobs=4, backend="multiprocessing", prefer="processes")
#         do = delayed(partial(update, nlp, optimizer))
#         tasks = (do(batch, {}) for batch in batches)
        
#         starttime = datetime.now()
#         print("Starting: " + str(starttime))
#         executor(tasks)

    print("Finished: " + str(datetime.now()))

    # Test the trained model
    test_text = 'Gianni Infantino is the president of FIFA.'
    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # Save model 
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # Test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)


def update_train(nlp, optimizer, batch, losses):
    texts, annotations = zip(*batch)
    nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
    print('Losses', losses)