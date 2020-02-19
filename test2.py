import csv
import os
import psutil
process = psutil.Process(os.getpid())

with open('./title.principals.tsv', 'rt') as f:
    lines = csv.DictReader(f, delimiter='\t')
    line_number = 0
    for line in lines:
        line_number += 1
        if line_number % 10000 == 0:
            print(process.memory_info().rss)
            print(line_number)
        # print(
        # f"{line['tconst']}: {line['category']}")
