# MscClassifier
# Setswana Noun Semantic Classifier

This project is a prototype implementation of a rule-based classifier that assigns semantic categories to Setswana nouns. It is based on my MSc research project titled **"A Model for Automatic Semantic Classification of Setswana Nouns"**, which was part of a larger initiative to develop a Setswana language translator.

The current version uses simple prefix cues and direct keyword matching to predict a noun's semantic class. While this version is rule-based, it lays the foundation for future implementations using decision trees or other machine learning techniques.

## 🧠 What it Does

Given a Setswana noun, the program predicts one of the following semantic classes:
- **Person**
- **Animal**
- **Object or Plural Entity**
- **Place**
- **Substance or Material**
- **Unknown**

## 💡 Example
Input: monna
Predicted Semantic Class: Person

Input: kgomo
Predicted Semantic Class: Animal

## 🛠 Requirements

- Python 3.x

## 🚀 How to Run

1. Clone this repository or download the `classifier.py` file.
2. Run it from a terminal or command line:

```bash
python classifier.py
