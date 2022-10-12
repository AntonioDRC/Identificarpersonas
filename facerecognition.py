# Importat biblioteca
from deepface import DeepFace

#Buscar rostro
print ("Buscar rostro")

#df = Deep.find(img_path = "img1", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/antoniodrc/Downloads/img1.jpg", db_path = "/home/antoniodrc/GitHub/Identificarpersonas/IdentificarPersonas/Persona3/my_db", enforce_detection = "false")
print("Resultado")
print (df)
