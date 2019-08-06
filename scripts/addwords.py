import json

input_file = 'words.json'
output_file = 'words2.json'


with open(input_file, 'r') as f:
    scrabble_words = json.load(f)

words = {k: v['definition'] for (k,v) in scrabble_words.items()}

with open(output_file, 'w+') as f:
            json.dump(words, f, indent=4)