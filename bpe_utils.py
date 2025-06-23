from collections import Counter

def get_bpe_merges(terms, num_merges=50):
    pairs = Counter()

    for word in terms:
        chars = list(word)
        for i in range(len(chars) - 1):
            pair = (chars[i], chars[i + 1])
            pairs[pair] += 1
    
    merges = [pair for pair, _ in pairs.most_common(num_merges)]
    return merges


def apply_bpe(term, merges):
    tokens = list(term)
    i = 0
    while i < len(tokens) - 1:
        pair = (tokens[i], tokens[i + 1])
        if pair in merges:
            tokens[i:i+2] = [''.join(pair)]
            i = max(i - 1, 0)
        else:
            i += 1
    return tokens
