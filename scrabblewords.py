import csv

# word
# part of speech
# origin
# root
# 1st meaning/ 2nd meaning


class CSVParser():
    
    def __init__(self, target_csv):
        self.csvfile = []
        with open(target_csv) as current_file:
            csvReaderObj = csv.reader(current_file, delimiter='\t', quotechar='"')
            for row in csvReaderObj:
                self.csvfile.append(row)

    def printRows(self):
        for row in self.csvfile:
            print(row)


if __name__ == '__main__':
    target_csv = 'words.txt'
    c = CSVParser(target_csv)
    c.printRows()
