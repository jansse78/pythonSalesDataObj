import multiprocessing
import CsvReader
import DataContainer
from datetime import datetime

class CreateContainer():

    def __init__(self):
        self.container = []
       
    def createContainer(self):

        processes = []
        self.container = DataContainer.DataContainer() #csv_reader.readFile())
        csv_reader = CsvReader.CsvReader(r'C:\Users\xxx\opiskelut\Python\finalCapstoneProj\100000 Sales Records.csv', self.container)
        print(f'objects inside from the csv file: {datetime.now().time()}')
        print(f"lines: {csv_reader.readFile()}")
        print(f'begin sorting: {datetime.now().time()}')
        self.container.sort_container()
        print(f'containerReady {datetime.now().time()}')
        return self.container