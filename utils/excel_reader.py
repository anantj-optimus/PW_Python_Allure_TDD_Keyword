# utils/excel_reader.py

import openpyxl
from collections import defaultdict

def get_test_steps_by_testcase(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    steps_by_testcase = defaultdict(list)

    # Read header row
    headers = [cell.value for cell in sheet[1]]

    # Read rows starting from row 2
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = dict(zip(headers, row))
        testcase_id = row_data.get("TestCaseID")
        if testcase_id:
            steps_by_testcase[testcase_id].append(row_data)

    return [(tc_id, steps) for tc_id, steps in steps_by_testcase.items()]
