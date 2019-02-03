#dbbase connect
#
import argparse
import os

def main(database: str, urlListFile: str):
    print("we are going to work with" +database)
    print("we are going to scan" +urlListFile)


if  __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File Containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, urlListFile=input_file)

