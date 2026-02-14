from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "C1=CC=C(C=C1)OC2=CC=CC=C2O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)  # Añadir hidrógenos

AllChem.EmbedMolecule(mol)  # Genera geometría 3D

# Guardar como SDF
w = Chem.SDWriter("2HDE.sdf")
w.write(mol)
w.close()

# Leer SDF generado
sdf_file = "2HDE.sdf"
mol_supplier = Chem.SDMolSupplier(sdf_file, removeHs=False)
mol = mol_supplier[0]

# Guardar como PDB
w = Chem.PDBWriter("2HDE.pdb")
w.write(mol)
w.close()
