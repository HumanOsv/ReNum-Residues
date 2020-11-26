from Bio import PDB

pdb_io = PDB.PDBIO()
pdb_parser = PDB.PDBParser()
pdbfile = 'rep.c0.pdb'
structure = pdb_parser.get_structure(" ", pdbfile)

new_resnums = [i + 0 for i in range(609)]

for model in structure:
    for chain in model:
        for i, residue in enumerate(chain.get_residues()):
            res_id = list(residue.id)
            res_id[1] = new_resnums[i]
            residue.id = tuple(res_id)

pdb_io.set_structure(structure)
pdb_io.save(pdbfile + "-new.pdb")
