import csv

class CsvLoader:
    def __init__(self, filepath):
        self.data = {}
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0].strip()
                quantity = row[1].strip()
                item_type = row[2].strip()
                self.data[name] = (quantity, item_type)
    
    def getQuant(self, name):
        if name in self.data:
            return self.data[name][0]
        else:
            return None
    
    def getType(self, name):
        if name in self.data:
            return self.data[name][1]
        else:
            return None


