import json
from collections import defaultdict
from Levenshtein import distance
from bpe_utils import get_bpe_merges, apply_bpe

def load_terms(file_path='terms.txt'):
    terms = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            term, count = line.strip().split('\t')
            terms.append((term, int(count)))
    return sorted(terms, key=lambda x: -x[1])  # ordenado por frecuencia

def cluster_terms(terms, max_distance=3):
    clusters = []
    visited = set()

    for i, (term_i, _) in enumerate(terms):
        if term_i in visited:
            continue

        cluster = [term_i]
        visited.add(term_i)

        for j in range(i + 1, len(terms)):
            term_j, _ = terms[j]
            if term_j in visited:
                continue
            if distance(term_i, term_j) <= max_distance:
                cluster.append(term_j)
                visited.add(term_j)
        
        clusters.append(cluster)
    
    return clusters

def build_glossary(terms, clusters):
    glossary = []
    for cluster in clusters:
        canonical = max(cluster, key=lambda t: dict(terms)[t])  # el más frecuente
        glossary.append({
            "term": canonical,
            "variants": [v for v in cluster if v != canonical],
            "tokens": [],        # vacío por ahora
            "definition": "",
            "example": ""
        })
    return glossary

if __name__ == '__main__':
    terms = load_terms()
    clusters = cluster_terms(terms)
    glossary = build_glossary(terms, clusters)

    # BPE
    canonical_terms = [entry["term"] for entry in glossary]
    merges = get_bpe_merges(canonical_terms)
    for entry in glossary:
        entry["tokens"] = apply_bpe(entry["term"], merges)

    with open('glossary.json', 'w', encoding='utf-8') as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)

    print(f"Glosario generado con {len(glossary)} términos canónicos en 'glossary.json'")
