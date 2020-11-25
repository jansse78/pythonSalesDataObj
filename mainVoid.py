import multiprocessing
import CsvReader
import DataContainer
import FileWriter
from datetime import datetime
import ExcelHandler
import CreateContainer

if __name__ == '__main__':

    creator = CreateContainer.CreateContainer()
    container = creator.createContainer()

    processes = []
    print(f'multiprocessingStart {datetime.now().time()}')
    fWriter = FileWriter.FileWriter(container)
    p1 = multiprocessing.Process(target=fWriter.write_to_binary)
    processes.append(p1)
    p2 = multiprocessing.Process(target=fWriter.write_to_json)
    processes.append(p2)
    p3 = multiprocessing.Process(target=fWriter.generate_XmlFile)
    processes.append(p3)
    xlHandler = ExcelHandler.ExcelHandler(container)
    p4 = multiprocessing.Process(target=xlHandler.rollExcels)
    processes.append(p4)

    for p in processes:
        p.start()

    for p in processes:
        p.join()