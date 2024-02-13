import pandas as pd
import os
import numpy as np

pdb_path = "C:/Users/User/Downloads/test_input_dir/4c7n.pdb"
colspecs = [(0, 6), (6, 11), (12, 16), (16, 17), (17, 20), (21, 22), (22, 26),
            (26, 27), (30, 38), (38, 46), (46, 54), (54, 60), (60, 66), (76, 78),
            (78, 80)]

names = ['ATOM', 'serial', 'name', 'altloc', 'resname', 'chainid', 'resseq',
         'icode', 'x', 'y', 'z', 'occupancy', 'tempfactor', 'element', 'charge']

# Read PDB file into a DataFrame
pdb = pd.read_fwf(pdb_path, names=names, colspecs=colspecs)

# Extract lines starting with "ATOM" from the DataFrame
pdb_atom_df = pdb[pdb['ATOM'] == 'ATOM']

# Write the filtered DataFrame to a new CSV file
pdb_atom_df.to_csv("pdb_atom.csv", sep=' ', index=False, na_rep='NaN')

# Print the DataFrame containing lines starting with "ATOM"
print(pdb_atom_df)


#checking if there are multiple chains in the sequence
chains = pdb_atom_df.chainid.unique()
if len(chains) ==2:
    chain_1=chains[0]
    chain_2=chains[1]
#remove alternate locations
alt_loc = pdb_atom_df.altloc.unique()
if len(alt_loc) > 1:
    # Filter rows where Alt_Loc is not NaN
    pdb_atom_df = pdb_atom_df[pdb_atom_df['altloc'].isna()]

seq_num = pdb_atom_df.resseq.values.astype(int)
print(seq_num)
seq_diff = np.abs(np.diff(seq_num))
print(seq_diff)
if np.any(seq_diff > 1):
    gap_id = np.where(seq_diff > 1)[0]
    print(gap_id)
else:
    print("no")

