from os import getcwd,listdir,rename,chdir,path
from random import randint

directorioActual=getcwd()
llave=randint(100000,999999)

class contador:
    def __init__(self): self.contador=0
    def aumentar(self): self.contador+=1
    def devolver(self): return(str(self.contador))

contadorNombres=contador()

def NuevoNombre(NombreViejo):
    NuevoNombre=""
    for letra in NombreViejo:
        if    letra=="#":NuevoNombre+="N"
        elif  letra==" ":NuevoNombre+="_"
        else:            NuevoNombre+=letra          
    return(NuevoNombre)

def RenombrarTodosLosArchivos():
    print("\n>>>"+getcwd())
    for archivo in listdir():
        rename(archivo ,NuevoNombre(archivo))
        if archivo!=NuevoNombre(archivo):
            print("   rn->"+str(archivo)+"->"+str(NuevoNombre(archivo)))
            contadorNombres.aumentar()
    for carpeta in listdir():
        if path.isdir(carpeta):
            chdir(carpeta) 
            RenombrarTodosLosArchivos()
            chdir("..")
        
#-----------------------------------------------
print("""
          +
         / \       WARNING:
        / █ \        this script rename ALL files and directories 
       /  █  \       in the current working directory
      /   █   \    ALERTA:  
     /         \     este script cambia TODOS los nombres de los archivos
    /     █     \    y directorios en el directorio actual 
   +-------------+       
"""  )
print(" pwd: "+directorioActual+"\n")
print("  Repeat the KEY for continue... \n  Repite la LLAVE para continuar...\n ")
Entrada=input(" Key/Llave "+str(llave)+" : ")
#------------------------------------------------
if str(llave)==Entrada:
    try: RenombrarTodosLosArchivos()
    except:print("\n  Un error ha ocurrido :( ");exit()
    print("\n  Done! "+contadorNombres.devolver()+" names changed")
    print("  Listo! "+contadorNombres.devolver()+" nombres cambiados")
else:
    print("\n  no changes \n  sin cambios  \n ");exit()


