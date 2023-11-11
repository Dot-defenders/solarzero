from powerModel import Model
from scipy.optimize import minimize
import csv


def parseCSV(inputFilePath: str):
    """
    Parses CSV file into a dict with its 
    keys as the CSV headers and 
    values as a list representing the columns 
    """

    print("Loading input data...")

    data: dict[str, list[float]] = {}
    with open(inputFilePath) as f:
        reader = csv.reader(f)
        headers = next(reader)
        for header in headers:
            data[header] = []

        for row in reader:
            for i, item in enumerate(row):
                data[headers[i]].append(item)

    print("Loaded.")

    return data

data = parseCSV("./data/input.csv")