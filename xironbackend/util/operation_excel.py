import xlrd
from xlutils.copy import copy
from xironbackend.util.read_ini import ReadIni


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None, sheet_name=None, start_row=None):
        read_ini = ReadIni()
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = read_ini.get_value_by_node_and_key('ExcelPath', 'file_path')

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = int(read_ini.get_value_by_node_and_key('ExcelPath', 'default_sheet_id'))

        if start_row:
            self.start_row = start_row
        else:
            self.start_row = int(read_ini.get_value_by_node_and_key('ExcelPath', 'default_start_row'))

        self.valid_sheet_names = read_ini.get_value_by_node_and_key('ExcelPath', 'valid_sheet_name')
        self.valid_data = self.get_valid_sheets_data()
        if sheet_name:
            self.data = self.valid_data[sheet_name]
        else:
            self.data = self.get_data()

    def get_valid_sheets_data(self):
        if self.valid_sheet_names is None:
            return None
        else:
            valid_sheet_names = self.valid_sheet_names.split(',')
        data = xlrd.open_workbook(self.file_name)
        valid_sheets_data = dict()
        for sheet_name in valid_sheet_names:
            valid_sheets_data[sheet_name] = data.sheet_by_name(sheet_name)
        return valid_sheets_data

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseID找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseID 找到对应的行号
    def get_row_num(self, case_id):
        num = self.start_row
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_data().nrows)
    print(opers.get_cell_value(1, 2))
