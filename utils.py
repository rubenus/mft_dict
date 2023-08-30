#!/usr/bin/env python
# coding: utf-8

import os
import sys
import numpy as np
import pandas as pd

def get_MFT_dictionaries():
    file_name = 'mfd_ptbr_alpha.dic'
    file = open(os.path.join(os.path.dirname(__file__), file_name), 'r', encoding='utf-8-sig')
    data = file.read()
    str_lines = data.split('\n')[1:]
    start_words = False
    dict_foundations = dict()
    dict_words = dict()
    for line in str_lines:
        if not start_words and line[0] == '%':
            start_words = True
            continue
        if not start_words:
            pair = line.split('\t')
            foundation_index = int(pair[1])
            dict_foundations[pair[0]] = foundation_index
            dict_words[foundation_index] = []
        else: # Words
            line_splitted = line.split('\t')
            foundation_codes = [ int(x) for x in line_splitted[1:] if x != '' ]
            for i in foundation_codes:
                dict_words[i] = dict_words[i] + [line_splitted[0]]
    return dict_foundations, dict_words

def MFT_to_python_regex(dict_mft_words):
    create_myMFT_words = dict()
    for key, value in dict_mft_words.items():
        create_myMFT_words[key] = '|'.join([ (r'\b' + x.replace('*', r'\w*')) for x in value ])
    return create_myMFT_words

