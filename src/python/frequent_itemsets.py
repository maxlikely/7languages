'''
Implementation of the Apriori algorithm for
finding frequent itemsets from a list of transactions

http://en.wikipedia.org/wiki/Apriori_algorithm
http://stats.stackexchange.com/questions/16456/apriori-algorithm-in-plain-english
http://aimotion.blogspot.co.uk/2013/01/machine-learning-and-data-mining.html

'''

from collections import Counter

def union(s):
    '''
    Returns the union of itemsets in s.

    >>> T = frozenset([frozenset([1,2,3]), frozenset([1,2,4])])
    >>> union(T)
    frozenset([1, 2, 3, 4])
    '''

    return reduce(frozenset.union, s)

def apriori(T, epsilon=3):
    '''
    Generate all frequent itemsets from T transactions with at least
    epsilon support.

    >>> T = [{1,2,5}, {2,4}, {2,3}, {1,2,4}, {1,3}, {2,3}, {1,3}, {1,2,3,5}, {1,2,3}]
    >>> apriori(T, epsilon=2)
    frozenset([frozenset([2, 4]), frozenset([5]), frozenset([3]), frozenset([1, 2]), frozenset([1, 5]), frozenset([1, 2, 5]), frozenset([4]), frozenset([2, 3]), frozenset([2, 5]), frozenset([1]), frozenset([1, 3]), frozenset([1, 2, 3]), frozenset([2])])

    >>> T = [{1,2,3,4}, {1,2}, {2,3,4}, {2,3}, {1,2,4}, {3,4}, {2,4}]
    >>> apriori(T, epsilon=3)
    frozenset([frozenset([2, 4]), frozenset([3]), frozenset([1, 2]), frozenset([3, 4]), frozenset([4]), frozenset([2, 3]), frozenset([1]), frozenset([2])])
    '''

    # generate frequent itemsets of size-1 (1-itemsets)
    counts = Counter(item for trans in T for item in trans)
    L = [frozenset(frozenset([cand]) for cand,count in counts.iteritems() if count >= epsilon)]

    # generate frequent (k+1)-itemsets
    k = 1
    while L[k-1]:
        candidates = {a | {b} for a in L[k-1] for b in union(L[k-1]) if not b in a}
        counts = Counter(c for trans in T for c in candidates if c <= trans)
        L.append({cand for cand, count in counts.iteritems() if count >= epsilon})
        k += 1

    return union(filter(None,L))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
