import json
import os
import tempfile
import unittest

from wordfreak.service.wordFrequency import extractWordFrequencies


class TestWordFrequency(unittest.TestCase):
    PATH_TO_TEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files", "parser"))

    def test_extractWordFrequencies_happyPath(self):
        txtFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.txt")
        with tempfile.TemporaryDirectory() as tempDir:
            fullJsonPath = os.path.join(tempDir, "tmp.json")
            extractWordFrequencies(txtFilePath, fullJsonPath)
            # check that JSON file is saved as we expect
            with open(fullJsonPath) as f:
                wordFrequencies = json.load(f)
            self.assertIsInstance(wordFrequencies, dict)
            self.assertEqual(6, len(wordFrequencies.keys()))
            self.assertEqual(2, wordFrequencies["hello"])
            self.assertEqual(2, wordFrequencies["world"])
            self.assertEqual(1, wordFrequencies["this"])
            self.assertEqual(1, wordFrequencies["is"])
            self.assertEqual(1, wordFrequencies["a"])
            self.assertEqual(1, wordFrequencies["test"])

    def test_extractWordFrequencies_outputFilePathNotJson_raisesException(self):
        txtFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.txt")
        with self.assertRaises(ValueError) as context:
            extractWordFrequencies(txtFilePath, "tmp.notjson")
        self.assertEqual("Output file must be a .json file.", str(context.exception))

    def test_extractWordFrequencies_inputFileIsNotSupportedFileType_raisesException(self):
        with self.assertRaises(ValueError) as context:
            extractWordFrequencies("bad.bad", "tmp.json")
        self.assertEqual("Filetype not supported for parsing (tried to parse file at 'bad.bad').",
                         str(context.exception))
