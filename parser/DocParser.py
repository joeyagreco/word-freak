import docx2txt

from parser.Parser import Parser


class DocParser(Parser):
    """
    For use parsing .doc and .docx files.
    """

    @classmethod
    def getWordFrequency(cls, pathToPdfFile: str) -> dict[str, int]:
        # get all word frequencies from the given .doc or .docx file
        lines = docx2txt.process(pathToPdfFile).split()
        return cls._getWordFrequencyFromLines(lines)
