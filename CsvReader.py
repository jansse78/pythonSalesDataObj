class CsvReader():

    def __init__(self,filePath, container):
        self.filePath = filePath
        self.container = container

    def readFile(self):
        import csv
        import DataModel
        with open(self.filePath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                location = DataModel.dataLocation(line[0], line[1])
                unit = DataModel.unitData(line[2], line[9],line[10],line[8])
                financial = DataModel.financialTotal(line[11],line[12],line[13])
                row = DataModel.DataRow(line[3],line[4],line[5],line[6],line[7],location,unit,financial)
                self.container.addToContainer(row)
            return csv_reader.line_num