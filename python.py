import csv

input_file = 'lichess_db_puzzle_uncleaned.csv'
output_file = 'lichess_db_puzzle_uncleaned_sample.csv'

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for i, row in enumerate(reader):
        if i >= 1000:
            break
        writer.writerow(row)
print(f"Sample de 1000 lignes écrites dans {output_file}")

