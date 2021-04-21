import os
import time
import sys
import tkinter.filedialog

from Gramatica import GLC

GRAMATICAS=[]
def MENU():	
    os.system('cls')
    print("___________________________________________________________________________________")
    print("                                                                                   ")
    print ("        \t              1 - Cargar Archivo           ")
    print ("        \t              2 - Mostrar Información          ")
    print ("        \t              3 - Generar Autómata de Pila          ")
    print ("        \t              4 - Reporte de Recorrido       ")
    print ("        \t              5 - Salir")
    print("___________________________________________________________________________________")

def Op1():
    global GRAMATICAS
    os.system('cls')

    root= tkinter.Tk()
    root.withdraw()
    ruta=tkinter.filedialog.askopenfilename(
        initialdir="C:", 
        filetypes=(
            ("Archivo glc", "*.glc"),
            ("Todos los ficheros","*.*")
        ), 
        title = "ABRIR ARCHIVO"
    )
    try:
        #lectura de archivo linea*linea
        with open(ruta, "r", encoding="utf-8") as f:
	        content=f.readlines()
        #print(content)
        print(ruta)
        temp=[]

        for i in content:
            temp.append(i.split("\n"))
        
        #separando por lineas
        lineas=[]

        for i in range(len(temp)):
            lineas.append(temp[i][0])
        cont=0
        line=0
        for i in range(len(lineas)):
            line+=1
            if line==1:
                transiciones=[]
                nombre=lineas[i]
                #print("nombre: " +lineas[i])
            elif line==2:
                no_terminales=""
                terminales=""

                s=lineas[i].split(";")
    
                no_terminales=s[0].split(",")   #no terminales
                terminales=s[1].split(",")  #terminales
                inicial=s[2]    #terminal inicial

                #print("terminales:"+ str(terminales))
                #print("no terminales:"+ str(no_terminales))
                #print("estado inicial "+ inicial)
            elif line==0:
                print("empieza gramática")
            elif line>2 and lineas[i]!="*":
                transiciones.append(lineas[i]) 
            
            if lineas[i]=="*":
                #termino de leer gramática
                line=0
                print("------")
                cont+=1
                #print("transiciones :"+ str(transiciones))
                GRAMATICAS.append(GLC(nombre,no_terminales,terminales,inicial,transiciones))
            #print(lineas[i] + " linea: " + str(line))

        print(" cantidad de gramáticas " + str(cont))
    finally:
        for i in GRAMATICAS:
            print(i.nombre)
            print(i.no_terminales)
            print(i.terminales)
            print(i.transiciones)
            print(i.inicial)
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")

def Op2():
    os.system('cls')

def Op3():
    os.system('cls')

def Op4():
    os.system('cls')

os.system('cls')
print("___________________________________________________________________________________")
print("")
print("                               PROYECTO 2 - LFP                            ")
print("")
print("     *********************************************************************")
print("     **         > Marlon Isaí Figueroa Farfán                           **")
print("     **         > 201904013                                             **")
print("     **         > Lenguajes Formales de Programación: \"B\"               **")
print("     **         > Ingeniería en Ciencias y Sistemas                     **")
print("     **         > 4to Semestre                                          **")
print("     *********************************************************************")
print("___________________________________________________________________________________")

#cuenta regresiva
"""for i in range(5, 0, -1):
    sys.stdout.write(" \r ")
    sys.stdout.write(" --->{:2d}  ".format(i))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\r  BIENVENIDO !            \n")

input("\nEnter para continuar...")
os.system('cls')
"""
while True:
    MENU()
    print("\n          -------------Seleccione una Opción-------------\n")
    op=input("              >>  ")
    if op=="1":
        print ("")
        Op1()
        input("\npulsa enter para volver...")
    elif op=="2":
        print ("")
        os.system('cls')
        Op2()
        input("\npulsa enter para volver...")
    elif op=="3":
        print ("")
        os.system('cls')
        Op3()
        input("\npulsa enter para volver...")
    elif op=="4":
        print ("")
        os.system('cls')
        Op4()
        input("\npulsa enter para volver...")
    elif op=="5":
        os.system('cls')
        break
    else:
        print ("***ERROR****")
        os.system('cls')
        input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")

