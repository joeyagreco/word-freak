import json

from parser.TxtParser import TxtParser


class FrequencyService:

    @classmethod
    def extractWordFrequencies(cls, inputFilePath: str, outputFilePath: str) -> None:
        """
        Takes a file and save all word frequencies to a JSON file.
        """

        # TODO: check different file types here (.txt, .pdf, etc...)
        wordFrequencies = TxtParser.getWordFrequency(inputFilePath)

        # sort word frequencies by number of occurrences
        orderedWordFreq = dict(sorted(wordFrequencies.items(), reverse=True, key=lambda item: item[1]))

        # save to JSON file
        with open(outputFilePath, "w+") as file:
            json.dump(orderedWordFreq, file)
