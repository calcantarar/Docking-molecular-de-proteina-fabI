from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "C1=CC(=C(C=C1Cl)O)OC2=C(C=C(C=C2)Cl)Cl"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)  # Añadir hidrógenos

AllChem.EmbedMolecule(mol)  # Genera geometría 3D

# Guardar como SDF
w = Chem.SDWriter("Triclosan.sdf")
w.write(mol)
w.close()

# Leer SDF generado
sdf_file = "Triclosan.sdf"
mol_supplier = Chem.SDMolSupplier(sdf_file, removeHs=False)
mol = mol_supplier[0]

# Guardar como PDB
w = Chem.PDBWriter("Triclosan.pdb")
w.write(mol)
w.close()
