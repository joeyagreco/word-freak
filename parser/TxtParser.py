import json
import re
import string


class TxtParser:
    """
    For use parsing .txt files.
    """
    SPECIAL_CHARACTERS = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

    @classmethod
    def parseWordFrequencyToJson(cls, pathToTxtFile: str, pathToSaveTo: str) -> None:
        # get all word frequencies from .txt file
        wordFrequency: dict[str, int] = dict()
        with open(pathToTxtFile) as file:
            for line in file:
                line = line.strip()
                words = line.split()
                for word in words:
                    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                    if word in wordFrequency:
                        wordFrequency[word] += 1
                    else:
                        wordFrequency[word] = 1

        # save all word frequencies to .json file
        with open(pathToSaveTo, "w+") as file:
            json.dump(wordFrequency, file)
