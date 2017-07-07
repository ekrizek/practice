import csv

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["siteId"]),
        print(line["studentId"]),
        print(line["date"])

if __name__ == "__main__":
    with open("ORF-CES-W.csv") as f_obj:
        csv_dict_reader(f_obj)

