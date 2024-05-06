import re
from collections import Counter
import csv
import argparse

my_parser = argparse.ArgumentParser(description="Reading the log file")
my_parser.add_argument(
    "log_file",
    help="enter the log path to parser, please!",
    type= argparse.FileType('r')  # read file mode
)
args = my_parser.parse_args()

# log_file = 'apache.log'
exported_file = 'count.csv'
log_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

with args.log_file as file:
    logs = file.read()
    ip_list = re.findall(log_regex, logs)
    # print("this is list ip: \n", ip_list)

    # grep -P "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" apache.log
    # grep -Po "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" apache.log
    # -P, --perl-regexp PATTERNS are Perl regular expressions
    # -o, only match

    # count number and uniq data:
    # grep -Po "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" apache.log | sort | uniq - c


    with open(exported_file, 'w') as f:
        fwritecsv = csv.writer(f)
        fwritecsv.writerow(["IP Address", "Count"])
        for k, v in Counter(ip_list).items():
            fwritecsv.writerow([k, v])
