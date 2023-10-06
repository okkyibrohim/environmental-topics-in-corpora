import numpy as np
from converter.jsonl2conll import jsonl2conll
from seqeval.metrics import classification_report

def get_tags(conll):
    list_tags = []
    for tagged_sentence in conll:
        sentence, tags = zip(*tagged_sentence)
        list_tags.append(list(np.array(tags)))
    return list_tags

def pairwise_classification_report(file_path_1,file_path_2,relation_mode,debug=False):
    # Preprocess ann_1
    conll_ann_1 = jsonl2conll(file_path_1,relation_mode,debug)
    tags_ann_1 = get_tags(conll_ann_1)
    # Preprocess ann_2
    conll_ann_2 = jsonl2conll(file_path_2,relation_mode,debug)
    tags_ann_2 = get_tags(conll_ann_2)
    return classification_report(tags_ann_1, tags_ann_2)