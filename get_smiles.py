from pubchempy import get_compounds
import csv

num = 1
with open('phytochemicals.tsv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        smiles = []
        for row in csvreader:
            compound = get_compounds(row[0], 'name')
            if compound:
                smiles.append((row[0], compound[0].canonical_smiles))
            else:
                smiles.append((row[0], ''))
            print(num)
            if len(smiles) == 10:
                file = open('phytochemicals_smiles.csv', 'a')
                for i in smiles:
                    file.write(i[0]+ "|" + i[1] + '\n')
                file.close()
                smiles = []
            num += 1
