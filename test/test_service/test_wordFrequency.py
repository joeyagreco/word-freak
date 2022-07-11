import json
import os
import tempfile
import unittest

from wordfreak.service.wordFrequency import extractWordFrequencies, pythonizeWordFrequencies


class TestWordFrequency(unittest.TestCase):
    PATH_TO_TEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files", "parser"))

    def test_extractWordFrequencies_outputFilePathGiven_savesToFile(self):
        txtFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.txt")
        with tempfile.TemporaryDirectory() as tempDir:
            fullJsonPath = os.path.join(tempDir, "tmp.json")
            response = extractWordFrequencies(txtFilePath, fullJsonPath)
            # check that JSON file is saved as we expect
            with open(fullJsonPath) as f:
                wordFrequencies = json.load(f)

            for responseDict in (response, wordFrequencies):
                self.assertIsInstance(responseDict, dict)
                self.assertEqual(6, len(responseDict.keys()))
                self.assertEqual(2, responseDict["hello"])
                self.assertEqual(2, responseDict["world"])
                self.assertEqual(1, responseDict["this"])
                self.assertEqual(1, responseDict["is"])
                self.assertEqual(1, responseDict["a"])
                self.assertEqual(1, responseDict["test"])

    def test_extractWordFrequencies_outputFilePathNotGivenGiven_happyPath(self):
        txtFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.txt")
        response = extractWordFrequencies(txtFilePath)

        self.assertIsInstance(response, dict)
        self.assertEqual(6, len(response.keys()))
        self.assertEqual(2, response["hello"])
        self.assertEqual(2, response["world"])
        self.assertEqual(1, response["this"])
        self.assertEqual(1, response["is"])
        self.assertEqual(1, response["a"])
        self.assertEqual(1, response["test"])

    def test_extractWordFrequencies_frequenciesAreSortedBiggestToSmallest(self):
        txtFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.txt")
        response = extractWordFrequencies(txtFilePath)

        self.assertEqual(str(sorted(response.values(), reverse=True)), str(list(response.values())))

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

    def test_pythonizeWordFrequencies_preFormattedJsonFile_happyPath(self):
        jsonFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.json")
        wordFrequencies = pythonizeWordFrequencies(jsonFilePath)
        self.assertIsInstance(wordFrequencies, dict)
        self.assertEqual(6, len(wordFrequencies.keys()))
        self.assertTrue(isinstance(count, int) for count in wordFrequencies.values())
        self.assertEqual(2, wordFrequencies["hello"])
        self.assertEqual(2, wordFrequencies["world"])
        self.assertEqual(1, wordFrequencies["this"])
        self.assertEqual(1, wordFrequencies["is"])
        self.assertEqual(1, wordFrequencies["a"])
        self.assertEqual(1, wordFrequencies["test"])

    def test_pythonizeWordFrequencies_freshlyFormattedJsonFile_happyPath(self):
        txtFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.txt")
        with tempfile.TemporaryDirectory() as tempDir:
            fullJsonPath = os.path.join(tempDir, "tmp.json")
            extractWordFrequencies(txtFilePath, fullJsonPath)
            wordFrequencies = pythonizeWordFrequencies(fullJsonPath)
            self.assertIsInstance(wordFrequencies, dict)
            self.assertEqual(6, len(wordFrequencies.keys()))
            self.assertTrue(isinstance(count, int) for count in wordFrequencies.values())
            self.assertEqual(2, wordFrequencies["hello"])
            self.assertEqual(2, wordFrequencies["world"])
            self.assertEqual(1, wordFrequencies["this"])
            self.assertEqual(1, wordFrequencies["is"])
            self.assertEqual(1, wordFrequencies["a"])
            self.assertEqual(1, wordFrequencies["test"])

    def test_pythonizeWordFrequencies_valuesNotAllInt_raisesException(self):
        jsonFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test2.json")
        with tempfile.TemporaryDirectory() as tempDir:
            with self.assertRaises(ValueError) as context:
                pythonizeWordFrequencies(jsonFilePath)
            self.assertEqual("Word Frequencies not formatted correctly, values must by type 'int'.",
                             str(context.exception))
