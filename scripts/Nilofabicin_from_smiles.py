from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "CC1=C(C=CC=C1N)CN2C=CC(=CC2=O)OCCC3=CC=CS3"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)  # Añadir hidrógenos

AllChem.EmbedMolecule(mol)  # Genera geometría 3D

# Guardar como SDF
w = Chem.SDWriter("Nilofabicin.sdf")
w.write(mol)
w.close()

# Leer SDF generado
sdf_file = "Nilofabicin.sdf"
mol_supplier = Chem.SDMolSupplier(sdf_file, removeHs=False)
mol = mol_supplier[0]

# Guardar como PDB
w = Chem.PDBWriter("Nilofabicin.pdb")
w.write(mol)
w.close()
