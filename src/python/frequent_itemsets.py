'''
Implementation of the Apriori algorithm for
finding frequent itemsets from a list of transactions

http://en.wikipedia.org/wiki/Apriori_algorithm
http://stats.stackexchange.com/questions/16456/apriori-algorithm-in-plain-english

'''

# coding: utf-8

from collections import Counter

def union(s):
    '''
    returns the union of itemsets in s
    '''
    united = set()
    for subset in s:
        united |= subset

    return united

def apriori(T, epsilon=3):
    '''
    generate all frequent itemsets from T transactions with at least
    epsilon support
    '''

    # generate frequent itemsets of size-1 (1-itemsets)
    counts = Counter(item for trans in T for item in trans)
    L = [{frozenset([cand]) for cand,count in counts.iteritems() if count >= epsilon}]

    # generate frequent (k+1)-itemsets
    k = 1
    while L[k-1]:
        candidates = {a | {b} for a in L[k-1] for b in union(L[k-1]) if not b in a}
        counts = Counter(c for trans in T for c in candidates if c <= trans)
        L.append({cand for cand, count in counts.iteritems() if count >= epsilon})
        k += 1

    return union(filter(None,L))

def demo():

    ## EXPECTED RESULTS:
    # {1}, {2}, {3}, {4}, {5}, {1, 2}, {1, 3}, {1, 5}, {2, 3}, {2, 4}, {2, 5},
    # {1, 2, 3}, {1, 2, 5}

    T = [{1,2,5}, {2,4}, {2,3}, {1,2,4}, {1,3}, {2,3}, {1,3}, {1,2,3,5}, {1,2,3}]
    results = apriori(T, 2)

    for r in results:
        print '*', r
    print '-' * 50

    ## EXPECTED RESULTS:
    # {{4}, {2}, {3}, {1}}, {{2, 4}, {1, 2}, {2, 3}, {3, 4}}}

    T = [{1,2,3,4}, {1,2}, {2,3,4}, {2,3}, {1,2,4}, {3,4}, {2,4}]
    results = apriori(T, 3)

    for r in results:
        print '*', r

if __name__ == '__main__':
    demo()
