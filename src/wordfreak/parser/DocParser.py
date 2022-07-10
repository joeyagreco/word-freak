import textract

from src.wordfreak.parser.Parser import Parser


class DocParser(Parser):
    """
    For use parsing .doc files.
    """

    @classmethod
    def getWordFrequency(cls, pathToPdfFile: str) -> dict[str, int]:
        # get all word frequencies from the given .docx file
        byteLines = textract.process(pathToPdfFile).split()
        # convert bytes to strings
        lines = [byteLine.decode("utf-8") for byteLine in byteLines]
        return cls._getWordFrequencyFromLines(lines)
