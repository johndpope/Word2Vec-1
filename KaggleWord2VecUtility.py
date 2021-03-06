#!/usr/bin/env python

import re
import nltk

import pandas as pd
import numpy as np
import codecs
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


class KaggleWord2VecUtility(object):
    """KaggleWord2VecUtility is a utility class for processing raw HTML text into segments for further learning"""

    @staticmethod
    def sku_to_wordlist( sku, remove_stopwords=False ):
        # Function to convert a document to a sequence of words,
        # optionally removing stop words.  Returns a list of words.
        #
        # 1. Remove HTML
	sku_text = BeautifulSoup(sku).get_text()
        #
        # 2. Remove non-letters
        sku_text = re.sub("[^a-zA-Z]"," ", sku_text)
        #
        # 3. Convert words to lower case and split them
        words = sku_text.lower().split()
        #
        # 4. Optionally remove stop words (false by default)
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]
        #
        # 5. Return a list of words
        return(words)

    # Define a function to split a sku into parsed sentences
    @staticmethod
    def sku_to_sentences( sku, tokenizer, remove_stopwords=False ):
        # Function to split a sku into parsed sentences. Returns a
        # list of sentences, where each sentence is a list of words
        #
        # 1. Use the NLTK tokenizer to split the paragraph into sentences
        raw_sentences = []
	try:
		sku = sku.encode('utf-8')
		raw_sentences = tokenizer.tokenize(sku.decode('utf8').strip())
	except:
		print "exception"
		pass
	#raw_sentences = tokenizer.tokenize(codecs.utf_8_encode(sku.decode('utf8').strip()))
	#
        # 2. Loop over each sentence
        sentences = []
        for raw_sentence in raw_sentences:
            # If a sentence is empty, skip it
            if len(raw_sentence) > 0:
                # Otherwise, call sku_to_wordlist to get a list of words
                sentences.append( KaggleWord2VecUtility.sku_to_wordlist( raw_sentence, \
                  remove_stopwords ))
        #
        # Return the list of sentences (each sentence is a list of words,
        # so this returns a list of lists
        return sentences
