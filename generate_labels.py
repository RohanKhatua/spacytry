# use python 3.9
import spacy
import json


def spacy_extract_with_labels(text):
    # Load model
    nlp = spacy.load("en_core_web_md")

    # Get and print available entity types
    ner = nlp.get_pipe("ner")
    labels = set(ner.labels)
    print("SpaCy Recognizable Entity Types:")
    print("\n".join(f"- {label}" for label in sorted(labels)))
    print("\n" + "=" * 50 + "\n")

    # Process text
    doc = nlp(text)
    return [
        {
            "entity": ent.text,
            "label": ent.label_,
            "start_idx": ent.start_char,
            "end_idx": ent.end_char,
        }
        for ent in doc.ents
    ]


# Example usage
text = "Apple Inc. plans to invest $5M in Berlin by 2024."
print("SpaCy Results:")
print(json.dumps(spacy_extract_with_labels(text), indent=2))
