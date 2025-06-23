import os
import re
from collections import Counter

CORPUS_DIR = 'corpus'

# Regex para diferentes tipos de términos
REGEX_PATTERNS = [
    r'\b[a-z]{4,}\b',                 # Palabras técnicas (mín. 4 letras)
    r'\b[A-Z]{2,}\b',                 # Acrónimos en mayúsculas
    r'\b[a-z]+_[a-z_]+\b',            # snake_case
    r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b' # CamelCase
]

def extract_terms_from_text(text):
    terms = []
    for pattern in REGEX_PATTERNS:
        terms += re.findall(pattern, text)
    return terms

def extract_terms_from_corpus():
    term_counter = Counter()
    
    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith('.txt'):
            with open(os.path.join(CORPUS_DIR, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                terms = extract_terms_from_text(text)
                term_counter.update(map(str.lower, terms))  # normalizamos a minúsculas
    
    return term_counter

def save_terms(term_counter, output_file='terms.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for term, count in term_counter.most_common():
            f.write(f"{term}\t{count}\n")

if __name__ == '__main__':
    terms = extract_terms_from_corpus()
    save_terms(terms)
    print(f"{len(terms)} términos extraídos y guardados en 'terms.txt'")
