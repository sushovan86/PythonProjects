import os
import sys

from pandas import read_excel

from process_split import *


def validate_column(df, column):
    if column not in df.columns:
        print("ERROR!!! Column {} is not available in the spreadsheet"
              .format(column))
        exit(-1)


def main():
    args = sys.argv
    if len(args) != 2:
        print("ERROR!!! Please provide file path as first argument")
        exit(-1)
    else:
        abspath = os.path.abspath(args[1])
        filename = os.path.splitext(abspath)[0]
        ext = os.path.splitext(abspath)[1]

        if ext.lower() not in ['.xls', '.xlsx']:
            print("ERROR!!! Not an excel file")
            exit(-1)

        column = input('Enter column to split: ')
        choice = input('Enter split choice (S = Sheet / F = File): ').upper()

        df = read_excel(abspath)
        validate_column(df, column)

        if choice == 'F':
            process_split_file(df, column, filename, ext)
        elif choice == 'S':
            process_split_sheet(df, column, filename, ext)
        else:
            print("ERROR!!! Invalid choice")


if __name__ == '__main__':
    main()
