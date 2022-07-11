import os

import wordfreak

if __name__ == "__main__":
    PATH_TO_FILES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "files"))

    # Extracts word frequencies from "inputFile.txt" and returns them as a Python dictionary.
    wordFrequencies = wordfreak.extractWordFrequencies(os.path.join(PATH_TO_FILES_DIR, "theRoadNotTaken.txt"))
    print(wordFrequencies)

    # Give an output file to save the results to JSON.
    wordFrequencies = wordfreak.extractWordFrequencies(os.path.join(PATH_TO_FILES_DIR, "theRoadNotTaken.txt"),
                                                       os.path.join(PATH_TO_FILES_DIR,
                                                                    "theRoadNotTaken_wordFrequencies.json"))
    print(wordFrequencies)

    # Loads word frequencies from "theRoadNotTaken_wordFrequencies.json" and returns them as a Python dictionary.
    wordFrequencies = wordfreak.pythonizeWordFrequencies(
        os.path.join(PATH_TO_FILES_DIR, "theRoadNotTaken_wordFrequencies.json"))
    print(wordFrequencies)
