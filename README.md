
# SpacyTry

SpacyTry is a project that demonstrates the use of [SpaCy](https://spacy.io/) for Named Entity Recognition (NER). SpaCy is a popular library for advanced natural language processing in Python.

## Features

- Named Entity Recognition (NER) using SpaCy.
- Pre-trained models for extracting entities such as persons, organizations, locations, dates, and more.
- Easy-to-understand implementation for beginners and advanced users alike.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/RohanKhatua/spacytry.git
   cd spacytry
   ```

2. Create and activate a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install SpaCy and the required language model:

   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Run the script to perform Named Entity Recognition:

   ```bash
   python main.py
   ```

2. Modify the `main.py` file to process your own texts.

## Project Structure

```
spacytry/
├── main.py             # Main script for running NER
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Examples

Here’s an example of how the Named Entity Recognition works:

Input:
```
"Apple is looking at buying U.K. startup for $1 billion."
```

Output:
```
Entities:
- Apple (ORG)
- U.K. (GPE)
- $1 billion (MONEY)
```
