import json
from Levenshtein import distance

GLOSSARY_PATH = 'glossary.json'

def load_glossary(path=GLOSSARY_PATH):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def list_terms(glossary):
    print("\n Lista de términos:")
    for entry in sorted(glossary, key=lambda e: e['term']):
        print(f"{entry['term']:20} ({len(entry['variants'])} variantes)")
    print()

def find_term(glossary, query):
    query = query.lower()
    closest = None
    min_dist = float('inf')
    for entry in glossary:
        d = distance(entry['term'], query)
        if d < min_dist:
            min_dist = d
            closest = entry
    return closest, min_dist

def show_definition(entry):
    print(f"\n Término canónico: {entry['term']}")
    print(f" Definición: {entry['definition']}")
    print(f" Ejemplo: {entry['example']}")
    print()

def main():
    glossary = load_glossary()

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Listar términos")
        print("2. Definir término")
        print("3. Buscar término")
        print("4. Salir")

        choice = input(">> ").strip()

        if choice == "1":
            list_terms(glossary)

        elif choice == "2":
            term = input("define > ").strip().lower()
            entry = next((e for e in glossary if e["term"] == term), None)
            if entry:
                show_definition(entry)
            else:
                print(f" Término '{term}' no encontrado en el glosario.")

        elif choice == "3":
            query = input("search > ").strip().lower()
            match, dist = find_term(glossary, query)
            if match:
                print(f"\n Coincidencia más cercana: {match['term']} (distancia {dist})")
            else:
                print(" No se encontró ninguna coincidencia.")

        elif choice == "4":
            print(" Adiós.")
            break

        else:
            print(" Opción no válida. Intente con 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
