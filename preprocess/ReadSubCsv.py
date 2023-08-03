import pandas as pd
import ast


def get_sub_csv(from_file, rowNum, to_file, start_row, end_row):
    data = pd.read_csv(from_file, nrows=rowNum, header=None, index_col=None)
    selected_rows = data.iloc[start_row:end_row + 1]
    data.to_csv(to_file, header=None, index=None)

def count_level_one_parentheses(filename):
    with open(filename, 'r') as file:
        content = file.read()
    level = 0
    count = 0
    for char in content:
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1
            if level == 1:
                count += 1
    return count

# 每个一级括号的第一个二级括号里，如果第11项（从1开始数）为1则视为有效数据，统计有效数据数目


def print_level_one_parentheses(filename):
    with open(filename, 'r') as file:
        content = file.read()

    level = 0
    current_line_content = ""

    for char in content:
        if char == '(':
            level += 1
            if level == 1:
                current_line_content = char
        elif char == ')':
            if level == 1:
                current_line_content += char
                print("一级括号内容：", current_line_content)
            level -= 1
        else:
            current_line_content += char


if __name__ == '__main__':
    rowNum = 11520
    start_row = 1619
    end_row = start_row + rowNum
    # get_sub_csv("../data/Quartet_data_tpch.csv", rowNum, "./Quartet_data_tpch.csv", start_row, end_row)
    # get_sub_csv("../data/Quartet_label_tpch.csv", rowNum, "./Quartet_label_tpch.csv", start_row, end_row)
    filename = "../data/TBOH_data_tpch.txt"
    num_level_one_parentheses = count_level_one_parentheses(filename)
    print("一级括号个数：", num_level_one_parentheses)