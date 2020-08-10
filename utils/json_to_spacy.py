# Convert json file to spaCy format.
# https://gist.github.com/kaustumbh7/afbd9788cc6b5526f11e70be9e41935a#file-json_to_spacy-py

# import plac
import logging
import argparse
import sys
import os
import json
import pickle
import time
# @plac.annotations(input_file=("Input file", "option", "i", str), output_file=("Output file", "option", "o", str))

def main(input_file="ner_corpus_260.json", output_file="ner_corpus_form"):
    try:
        training_data = []
        lines=[]
        with open(input_file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            text = data['content']
            entities = []
            for annotation in data['annotation']:
                point = annotation['points'][0]
                labels = annotation['label']
                if not isinstance(labels, list):
                    labels = [labels]

                for label in labels:
                    entities.append((point['start'], point['end'] + 1 ,label))

            if(len(annotation) > 0 and text != ""):
                training_data.append((text, {"entities" : entities}))
            else:
                print("!@#!@#: none found {} => {}".format(text, annotation))

        print(training_data)

        with open(output_file, 'wb') as fp:
            pickle.dump(training_data, fp)

    except Exception as e:
        logging.exception("Unable to process " + input_file + "\n" + "error = " + str(e))
        return None
if __name__ == '__main__':
    # plac.call(main)
    main()