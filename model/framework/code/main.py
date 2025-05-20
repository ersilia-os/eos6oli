# imports
import os
import csv
import sys
import soltrannet as stn

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = list(stn.predict(smiles_list))
print(outputs)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

outputs_ = []
for o in outputs:
    sol = o[0]
    print(sol)
    outputs_.append(sol)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["solubility"])  # header
    for o in outputs_:
        writer.writerow([o])
