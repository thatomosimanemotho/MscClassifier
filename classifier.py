def classify_noun(noun):
    noun = noun.lower().strip()

    # Simple rule-based classification using noun prefixes and keyword matching
    if noun.startswith("mo") or noun.startswith("mme") or noun in ["monna", "mosadi"]:
        return "Person"
    elif noun.startswith("di") or noun.startswith("ma") or noun.startswith("se"):
        return "Object or Plural Entity"
    elif noun in ["kgomo", "phologolo", "ntša", "katse"]:
        return "Animal"
    elif noun in ["motse", "toropo", "lefelo", "ntlo"]:
        return "Place"
    elif noun in ["bojalwa", "metsi", "lona"]:
        return "Substance or Material"
    else:
        return "Unknown or Not Classified"

# Example usage
if __name__ == "__main__":
    print("Setswana Noun Semantic Classifier\n")
    noun = input("Enter a Setswana noun: ")
    classification = classify_noun(noun)
    print(f"\nPredicted Semantic Class: {classification}")
