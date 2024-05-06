import re
from collections import Counter
import csv
import argparse

LOG_REGEX = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
parser = argparse.ArgumentParser(description="Reading the log file")
parser.add_argument(
    "-L",
    "--logfile",
    dest="log_file",
    help="Input log file path",
    required=True,
    type=argparse.FileType('r')  # read file mode
)

parser.add_argument(
    "--O",
    "--output",
    help='Output CSV file name',
    dest="output_file",
    type=str,
    default="output.csv"
)
def read_file(log_file_path):
    return re.findall(LOG_REGEX, log_file_path.read())

def couting_data(ip_list):
    return Counter(ip_list).items()

def write_out(exported_file, data_counted):
    with open(exported_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["IP_Address", "Count"])
        writer.writeheader()
        for item, count in data_counted:
            writer.writerow({"IP_Address": item, "Count": count})

def main():
    args = parser.parse_args()
    ip_list=read_file(args.log_file)
    data_counted=couting_data(ip_list)
    write_out(args.output_file, data_counted)

if __name__ == '__main__':
    main()