# Docking-molecular-de-proteina-fabI
Proyecto de curso de Bioinformática de UNMSM. Se modeló el complejo enzimático de fabI y evaluó la afinidad de 3 ligandos en un sitio activo representativo para ver la efectividad como potencial fármaco.

### Procedimiento
1) Obtención de la secuencia de la proteina fabI en el bioproyecto NZ_LQXX01000001.1
2) Modelado de la proteina como tetrámero por homología unitaria usando SWISS-MODEL (https://swissmodel.expasy.org/), considerando los mejores scores, plots de Ramachadran y observaciones adicionales.
3) Descarga del archivo .pbd del molde y modelo
4) Ejercución complejo_enzimatico.py (tener instalado pymol-opensource en terminal)
5) Preparación de los ligandos
6) Docking de cada ligando con el complejo enzimático
7) Evaluación de las interacciones atómicas en Discovery Studio y VMD
