import csv
import json
import pprint

# word
# part of speech
# origin
# root
# 1st meaning/ 2nd meaning


class ScrabbleDictionary():
    
    def __init__(self, target_csv):
        """builds the scrabble dictionary from a tab delimited text file containing word and definition pairings"""

        self.words = {}

        # read in words and defintions from a tab delimited text file
        with open(target_csv) as current_file:
            csvReaderObj = csv.reader(current_file, delimiter='\t', quotechar='"')

            # create word in the scrabble dictionary
            for row in csvReaderObj:
                word = row[0]
                word_defintion = row[1]

                words_sub_dict = {
                    'definition': word_defintion,
                    'points': self.calculate_points(word),
                    'length': len(word)
                }

                self.words[word] = words_sub_dict
                

    def calculate_points(self, word):
        """returns the points scored by playing a word"""

        letter_points = {
            'a': 1,
            'b': 3,
            'c': 3,
            'd': 2,
            'e': 1,
            'f': 4,
            'g': 2,
            'h': 4,
            'i': 1,
            'j': 8,
            'k': 5,
            'l': 1,
            'm': 3,
            'n': 1,
            'o': 1,
            'p': 3,
            'q': 10,
            'r': 1,
            's': 1,
            't': 1,
            'u': 1,
            'v': 4,
            'w': 4,
            'x': 8,
            'y': 4,
            'z': 10
        }

        word_points = 0

        for letter in word:
            word_points += letter_points[letter.lower()]

        return word_points

    def outputJSON(self, output_filename):
        with open(output_filename, 'w+') as json_file:
            json.dump(self.words, json_file, indent=4)

if __name__ == '__main__':
    target_csv = 'words_all.txt'
    s = ScrabbleDictionary(target_csv)
    s.outputJSON('words.json')
