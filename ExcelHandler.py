from datetime import datetime

class ExcelHandler():

    def __init__(self,  container):
        self.dataArray = []
        self.container = container

    def writeToExcel(self, fileNro):
        import xlsxwriter

        i = 0

        xlWb = xlsxwriter.Workbook(f"outExcel{fileNro}.xlsx")
        xlWs = xlWb.add_worksheet('data')
        print(f'excelfile generating:{fileNro}')
        for i  in range(len(self.dataArray)):
            try:
                xlWs.write(f'A{i+1}', '%s' %self.dataArray[i].orderID)
                xlWs.write(f'B{i+1}', self.dataArray[i].orderDate)
                xlWs.write(f'C{i+1}', self.dataArray[i].shipDate)
                xlWs.write(f'D{i+1}', self.dataArray[i].location.region)
                xlWs.write(f'E{i+1}', self.dataArray[i].financial.totalRevenue)
                xlWs.write(f'F{i+1}', self.dataArray[i].unit.itemType)
            except:
                print(f'haku datalle paikassa {i} ei onnistunut')

        xlWb.close()

    def rollExcels(self):
        print(f'Excel writing start {datetime.now().time()}')
        for i in range(10):
            self.dataArray = self.container.findDataRows(self.container.gatherRandom(1000))
            self.writeToExcel(i)
        print(f'Excel writing completed {datetime.now().time()}')
