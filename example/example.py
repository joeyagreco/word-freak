import os

import wordfreak

if __name__ == "__main__":
    PATH_TO_FILES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "files"))

    # Extracts word frequencies from "inputFile.txt" and returns them as a Python dictionary.
    wordFrequencyDict = wordfreak.extractWordFrequencies(os.path.join(PATH_TO_FILES_DIR, "theRoadNotTaken.txt"))
    print(wordFrequencyDict)

    # Give an output file to save the results to JSON.
    wordFrequencyDict = wordfreak.extractWordFrequencies(os.path.join(PATH_TO_FILES_DIR, "theRoadNotTaken.txt"),
                                                         os.path.join(PATH_TO_FILES_DIR,
                                                                      "theRoadNotTaken_wordFrequencies.json"))
    print(wordFrequencyDict)

    # Loads word frequencies from "theRoadNotTaken_wordFrequencies.json" and saves them to the variable wordFrequencyDict.
    wordFrequencyDict = wordfreak.pythonizeWordFrequencies(
        os.path.join(PATH_TO_FILES_DIR, "theRoadNotTaken_wordFrequencies.json"))
    print(wordFrequencyDict)
