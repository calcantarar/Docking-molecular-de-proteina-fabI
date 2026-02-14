from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "C1C=CN(C=C1C(=O)N)[C@H]2[C@@H]([C@@H]([C@H](O2)COP(=O)(O)OP(=O)(O)OC[C@@H]3[C@H]([C@H]([C@@H](O3)N4C=NC5=C(N=CN=C54)N)O)O)O)O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)  # Añadir hidrógenos

AllChem.EmbedMolecule(mol)  # Genera geometría 3D

# Guardar como SDF
w = Chem.SDWriter("NADH.sdf")
w.write(mol)
w.close()

# Leer SDF generado
sdf_file = "NADH.sdf"
mol_supplier = Chem.SDMolSupplier(sdf_file, removeHs=False)
mol = mol_supplier[0]

# Guardar como PDB
w = Chem.PDBWriter("NADH.pdb")
w.write(mol)
w.close()
