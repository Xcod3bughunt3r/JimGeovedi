# -*- coding: utf-8 -*-

# http://stackoverflow.com/a/7595897
def gen_ngrams(tokens, MIN_N, MAX_N):
    n_tokens = len(tokens)
    for i in xrange(n_tokens):
        for j in xrange(i+MIN_N, min(n_tokens, i+MAX_N)+1):
            yield tokens[i:j]

from itertools import combinations
# find all possible ordered phrases - http://stackoverflow.com/a/18406982
def find_combo(tokens):
    ns = range(1, len(tokens))
    for n in ns:
        for ix in combinations(ns, n):
            yield [' '.join(tokens[i:j]) for i, j in zip((0,)+ix, ix+(None,))]


# http://stackoverflow.com/a/699892
def int2bin(i):
    return '{0:08b}'.format(i)


def bin2int(b):
    return int(b, 2)


# nltk.tag.util.str2tuple
def str2tuple(s, sep='/'):
    loc = s.rfind(sep)
    if loc >= 0:
        return (s[:loc], s[loc+len(sep):].upper())
    else:
        return (s, None)

# nltk.tag.util.tuple2str
def tuple2str(tagged_token, sep='/'):
    word, tag = tagged_token
    if tag is None:
        return word
    else:
        assert sep not in tag, 'tag may not contain sep!'
        return '%s%s%s' % (word, sep, tag)

# nltk.tag.util.untag
def untag(tagged_sentence):
    return [w for (w, t) in tagged_sentence]
