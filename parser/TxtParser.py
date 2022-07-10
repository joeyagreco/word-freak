import string

from parser.Parser import Parser


class TxtParser(Parser):
    """
    For use parsing .txt files.
    """

    @classmethod
    def getWordFrequency(cls, pathToTxtFile: str) -> dict[str, int]:
        # get all word frequencies from the given .txt file
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
        return wordFrequency
