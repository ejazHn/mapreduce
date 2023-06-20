#!/usr/bin/env python
import sys
from math import log

def tfidf_col(doc_list, value_list, word_list):
    n = len(doc_list)

    for i in range(n):
        # extract the elements
        doc = doc_list[i]
        val = value_list[i]
        word = word_list[i]

        # calculate tf-idf
        tf = log(val + 1)
        idf = log(n / (1 + sum(value_list)))
        tfidf = tf * idf

        print("{}\t{}\t{}".format(doc, word, tfidf))

def main():
    current_word = None
    doc_list = []
    value_list = []
    word_list = []

    for line in sys.stdin:
        line = line.strip()
        word, doc_eq_count = line.split('\t')
        doc, count = doc_eq_count.split('=')
        count = int(count)

        if word == current_word:
            doc_list.append(doc)
            value_list.append(count)
            word_list.append(word)
        else:
            if current_word is not None:
                tfidf_col(doc_list, value_list, word_list)
            current_word = word
            doc_list = [doc]
            value_list = [count]
            word_list = [word]

    tfidf_col(doc_list, value_list, word_list)

if __name__ == "__main__":
    main()