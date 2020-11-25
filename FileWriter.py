import DataModel
from DataModel import DataEncoder
from datetime import datetime

class FileWriter():

    def __init__(self, container):
        self.container = container

    def write_to_binary(self):
        import pickle
        print(f'binarywriting start {datetime.now().time()}')
        try:
            with open('objects.bin', 'wb') as outputfileBin:
                pickle.dump(self.container.returnContainer(), outputfileBin, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print(f'Tuli herja: {e.__class__}, {e.args[0]}')

        return f'binarywriting completed {datetime.now().time()}'

    def write_to_json(self):
        import json
        print(f'json writing start {datetime.now().time()}')

        try:
            jsonData = ''
            with open('objects.json', 'w') as outputfileJson:
                dEncoder = DataModel.DataEncoder
                json.dump(self.container.returnContainer(), outputfileJson ,cls=dEncoder)
        except Exception as e:
            print(f'Tuli herja: {e.__class__}, {e.args[0]}')
        finally:
            print (f'json writing completed {datetime.now().time()}')

    def generate_XmlFile(self):

        i = 0
        import xml.etree.ElementTree as xml
        print(f'xml writing start {datetime.now().time()}')
        root = xml.Element("Data")

        while i < self.container.containerSize():
            dataRow = self.container.returnContainerValue(i)
            dataNode = xml.Element("Row")
            root.append(dataNode)
            orderId = xml.SubElement(dataNode, "OrderId")
            orderId.text = str(dataRow.orderID)
            orderDate = xml.SubElement(dataNode, "OrderDate")
            orderDate.text = dataRow.orderDate
            fina = xml.SubElement(dataNode,"Financial")
            totalRevenue = xml.SubElement(fina, "TotalRevenue")
            totalRevenue.text = dataRow.financial.totalRevenue
            totalCost = xml.SubElement(fina, "TotalCost")
            totalCost.text = dataRow.financial.totalCost
            totalProfit = xml.SubElement(fina, "TotalProfit")
            totalProfit.text = dataRow.financial.totalProfit
            i += 1

        tree = xml.ElementTree(root)
        tree = tree.getroot()

        from ElementTree_create_pretty import prettify
        tree = prettify(tree)

        with open('objects.xml', 'w') as files:
            files.write(tree)
        print(f'xml writing completed {datetime.now().time()}')
    
    def prettify(self, elem):
        from xml.etree import ElementTree
        from xml.dom import minidom
        rough_str = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_str)
        return reparsed.toprettyxml(indent='  ')


