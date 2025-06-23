import json
import requests
import time

OLLAMA_URL = 'http://localhost:11434/api/generate'
MODEL = 'mistral'  # o el que estés usando

def load_glossary(path='glossary.json'):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_glossary(glossary, path='glossary.json'):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)

def build_prompt(term, variants):
    return f"""
Eres un asistente de glosario experto. Define brevemente el término "{term}" relacionado con deportes, preferiblemente fútbol. Da un ejemplo corto de uso en una oración. Responde SOLO en español y SOLO en JSON con este formato:

{{"definition": "<máximo 25 palabras>", "example": "<máximo 25 palabras>"}}
"""


def query_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        raw = response.json()
        print("Respuesta bruta del modelo:\n", raw.get("response", ""))
        return raw["response"]

    except Exception as e:
        print(f"Error: {e}")
        return None

def fill_definitions(glossary):
    for entry in glossary:
        if entry["definition"] and entry["example"]:
            continue  # ya está definido

        prompt = build_prompt(entry["term"], entry["variants"])
        print(f"Definiendo: {entry['term']}...")

        response = query_ollama(prompt)
        if response:
            try:
                result = json.loads(response)
                entry["definition"] = result.get("definition", "")
                entry["example"] = result.get("example", "")
            except json.JSONDecodeError:
                print(f"Error al parsear JSON para {entry['term']}")
        else:
            print(f"No se pudo obtener respuesta para {entry['term']}")
        
        time.sleep(1)  # para no saturar Ollama

    return glossary

if __name__ == '__main__':
    glossary = load_glossary()
    glossary = fill_definitions(glossary)
    save_glossary(glossary)
    print("✅ Definiciones generadas y guardadas en 'glossary.json'")
