import os
import time
import sys
import tkinter.filedialog
import webbrowser
from Gramatica import GLC
from Gramatica import GRAMA


GRAMATICAS=[]
REPORTE=[]
nombre=""

def REPORTE_AP():
    f = open('AUTOMATA_PILA.html','w', encoding="utf-8")
    f.write("""
             <!DOCTYPE html>
        <html lang="en">

        <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>PROYECTO2_LF2</title>

        <link href="assets/img/icon.png" rel="icon">
        <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
        <!-- Bootstrap core CSS -->
        <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

        <link href="img/icon.png" rel="icon">
        <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

        <!-- Custom fonts for this template -->
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

        <!-- Custom styles for this template -->
        <link href="css/clean-blog.min.css" rel="stylesheet">

        </head>

        <body>

        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
        <div class="container">
        <a class="navbar-brand" href="AUTOMATA_PILA.html">FACULTAD DE INGENERÍA</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            AUTOMATA
            <i class="fas fa-bars">DE PILA EQUIVALENTE</i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="AUTOMATA_PILA.html">AUTÓMATA</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="RECORRIDO.html">RECORRIDO</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="RESUMEN.html">RESUMEN</a>
            </li>
            
            </ul>
        </div>
        </div>
        </nav>

        <!-- Page Header -->
        <header class="masthead" style="background-image: url('img/R.jpg')">
        <div class="overlay"></div>
        <div class="container">
        <div class="row">
            <div class="col-lg-8 col-md-10 mx-auto">
            <div class="site-heading">
                <h1>AUTÓMATA</h1>
                <span class="subheading">DE PILA EQUIVALENTE</span>
            </div>
            </div>
        </div>
        </div>
        </header>

        <!-- Main Content -->
        <div class="container">
        <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-preview">
            
            <a >
                <h2 class="post-title">""")
    f.write("Nombre: AP_"+nombre)
    cadena=""
    alfa=""
    for i in GRAMATICAS:
        if i.nombre==nombre:
            print("______________________________________________________")
            print("Nombre de la gramática tipo 2: "+ str(i.nombre))
            for j in range(len(i.terminales)):
                if j==(len(i.terminales)-1):
                    cadena+=i.terminales[j]
                    alfa+=i.terminales[j]+","
                else:
                    cadena+=i.terminales[j] +","
                    alfa+=i.terminales[j] +","
            for y in range(len(i.no_terminales)):
                if j==(len(i.no_terminales)-1):
                    alfa+=i.no_terminales[y]
                else:
                    alfa+=i.no_terminales[y] +","
            alfa+="#"
    f.write("""  
                </h2>
                <h3 class="post-subtitle">""")
    f.write("Terminales={"+cadena+"}")            
    f.write("""  
                </h3>
                <h3 class="post-subtitle">""")
    f.write("Alfabeto de pila={"+alfa+"}")
    f.write("""
                </h3>
                <h3 class="post-subtitle">
                Estados={i,p,q,f}
                </h3>
                <h3 class="post-subtitle">
                Estado inicial={i}
                </h3>
                <h3 class="post-subtitle">
                Estado de aceptacion={f}
                </h3>
            </a>
            </div>
            <br>
            <center><img src="apq.png"></center>
            <br>
            <br>
            <br>
            <br>
        
        """)
        #aqui va el contenido
    f.write("""
            </div>
            </div>
            </div>
            <hr>

            <!-- Footer -->
            <footer>
                <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                    </div>
                </div>
                </div>
            </footer>

            <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Custom scripts for this template -->
            <script src="js/clean-blog.min.js"></script>

            </body>

            </html>
        """)
    f.close()  

def RECORRIDO_AP():
    f = open('RECORRIDO.html','w', encoding="utf-8")
    f.write("""
    <!DOCTYPE html>
            <html lang="en">

            <head>

            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>PROYECTO2_LF2</title>

            <link href="assets/img/icon.png" rel="icon">
            <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
            <!-- Bootstrap core CSS -->
            <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

            <link href="img/icon.png" rel="icon">
            <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

            <!-- Custom fonts for this template -->
            <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
            <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

            <!-- Custom styles for this template -->
            <link href="css/clean-blog.min.css" rel="stylesheet">

            </head>

            <body>

            <!-- Navigation -->
            <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
            <div class="container">
            <a class="navbar-brand" href="AUTOMATA_PILA.html">FACULTAD DE INGENERÍA</a>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                <a class="nav-link" href="AUTOMATA_PILA.html">AUTÓMATA</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="RECORRIDO.html">RECORRIDO</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="RESUMEN.html">RESUMEN</a>
            </li>
            
            </ul>
        </div>
        </div>
        </nav>

        <!-- Page Header -->
        <header class="masthead" style="background-image: url('img/r2.jpg')">
            <div class="overlay"></div>
            <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                <div class="site-heading">
                    <h1>RECORRIDO</h1>
                    <span class="subheading">Autómata pila</span>
                </div>
                </div>
            </div>
            </div>
        </header>

        <!-- Main Content -->
        <div class="container">
        <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
        
        
            <div class="post-preview">
            <a>
                <h2 class="post-title">
                Iteración 1
                </h2>
                <center><img src="apq.png"></center>
            <h3 class="post-subtitle">
                Pila=#
            </h3>
            <h3 class="post-subtitle">
                Entrada=a
                </h3>  
            </a>
            <p class="post-meta">
    """)
    #aqui va el contenido
    f.write("""

    </div>
                </div>
            </div>

            <hr>

            <!-- Footer -->
            <footer>
                <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                    </div>
                </div>
                </div>
            </footer>

            <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Custom scripts for this template -->
            <script src="js/clean-blog.min.js"></script>

            </body>

            </html>
        
    """)
    f.close()  

def RESUMEN_AP():
    f = open('RESUMEN.html','w', encoding="utf-8")
    f.write("""
        <!DOCTYPE html>
            <html lang="en">

            <head>

            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>PROYECTO2_LF2</title>

            <link href="assets/img/icon.png" rel="icon">
            <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
            <!-- Bootstrap core CSS -->
            <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

            <link href="img/icon.png" rel="icon">
            <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

            <!-- Custom fonts for this template -->
            <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
            <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

            <!-- Custom styles for this template -->
            <link href="css/clean-blog.min.css" rel="stylesheet">

            </head>

            <body>

            <!-- Navigation -->
            <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
            <div class="container">
            <a class="navbar-brand" href="AUTOMATA_PILA.html">FACULTAD DE INGENERÍA</a>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                <a class="nav-link" href="AUTOMATA_PILA.html">AUTÓMATA</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="RECORRIDO.html">RECORRIDO</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="RESUMEN.html">RESUMEN</a>
            </li>
            
            </ul>
        </div>
        </div>
        </nav>

        <!-- Page Header -->
        <header class="masthead" style="background-image: url('img/r2.jpg')">
            <div class="overlay"></div>
            <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                <div class="site-heading">
                    <h1>RESUMEN</h1>
                    <span class="subheading">TRANSICIONES</span>
                </div>
                </div>
            </div>
            </div>
        </header>

        <!-- Main Content -->
        <div class="container">
        <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
        
        
            <div class="post-preview">
            <a>
                <h2 class="post-title">
                TABLA DE TRANSICIONES
                </h2>
            </a>
            <p class="post-meta">
    
    """)
    #aqui va el contenido
    f.write("""
        <table class="table table-dark table-hover">
                <td><center><h4>Iteración</h4></center></td>
                <td><center><h4>Pila</h4></center></td>
                <td><center><h4>Entrada</h4></center></td>
                <td><center><h4>Transiciones</h4></center></td>
    </table> 
    """)
    f.write("""
        </div>
                <hr>

                </div>
                </div>
            </div>

            <hr>

            <!-- Footer -->
            <footer>
                <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                    </div>
                </div>
                </div>
            </footer>

            <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Custom scripts for this template -->
            <script src="js/clean-blog.min.js"></script>

            </body>

            </html>
        

    """)
    f.close()

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
    global GRAMATICAS,REPORTE
    os.system('cls')
    print("--------------------CARGAR ARCHIVO--------------------")
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
                #Analizando producciones
                produccion=[]

                for x in range(len(transiciones)):
                    produccion.append(transiciones[x].split("->"))
                cont+=1
                analisis=[]
                for i in range(len(produccion)):
                    analisis.append(produccion[i][1].split(" "))
                es_libre=False
                for i in analisis:
                    if len(i)==3 or len(i)>3:
                        es_libre=True
                #print("transiciones :"+ str(transiciones))
                if es_libre==True:
                    GRAMATICAS.append(GLC(nombre,no_terminales,terminales,inicial,transiciones))
                else:
                    REPORTE.append(GLC(nombre,no_terminales,terminales,inicial,transiciones))
            #print(lineas[i] + " linea: " + str(line))

        print(" cantidad de gramáticas leidas " + str(cont))
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
    global GRAMATICAS,nombre
    os.system('cls')
    print("------------------Mostrar información de gramáticas cargadas en sistema------------------")
    print("(0) para volver a menu")
    for i in GRAMATICAS:
        print("-"+str(i.nombre))
    print("\n        -------------Ingrese el nombre:-------------\n")
    name=input("              >>  ")
    if name==0:
        MENU()

    #Mostrando datos de la Gramática solicitada
    for i in GRAMATICAS:
        if i.nombre==name:
            nombre=name
            print("______________________________________________________")
            print("Nombre de la gramática tipo 2: "+ str(i.nombre))
            
            print("No terminales = {",end="")
            for j in range(len(i.no_terminales)):
                if j==(len(i.no_terminales)-1):
                    print(i.no_terminales[j],end="")
                else:
                    print(i.no_terminales[j] +",",end="")    
            print("}\n", end="")
            
            print("Terminales = {", end="")
            for j in range(len(i.terminales)):
                if j==(len(i.terminales)-1):
                    print(i.terminales[j],end="")
                else:
                    print(i.terminales[j] +",",end="")
            print("}\n", end="")
            
            print("No terminal Inicial = "+ str(i.inicial[0]))
            produccion=[]
            print("Producciones")
            for x in range(len(i.transiciones)):
                produccion.append(i.transiciones[x].split("->"))
            o=0
            armando=[] 

            while o<len(i.no_terminales):
                trans=[]
                for x in range(len(produccion)):
                    if produccion[x][0]==i.no_terminales[o]:
                       trans.append(produccion[x][1]) 
                armando.append(GRAMA(i.no_terminales[o],trans))
                o+=1

            #imprimiendo producción
            for i in armando:
                print(i.no_terminales+"->",end="")
                if len(i.transiciones)==1:
                    for j in i.transiciones:
                        print(j) 
                elif len(i.transiciones)>1:
                    for j in range(len(i.transiciones)):
                        if j==0:
                            print(i.transiciones[j])
                        else:
                            print("  | " + i.transiciones[j]) 
            input("\npulsa enter para volver...") 
            Op2()  
            #analizando producciones
            """x=0
            while x<len(produccion)-1:
                if produccion[x+1]!=None and produccion[x][0]==produccion[x+1][0]:
                    print(str(produccion[x][0])+"->"+str(produccion[x][1]))
                    print("  |"+str(produccion[x+1][1]))
                    x+=1
                elif produccion[x][0]==produccion[x-1][0]:
                    x+=1
                else:
                    print(str(produccion[x][0])+"->"+str(produccion[x][1]))
                    x+=1"""

def Op3():
    global GRAMATICAS,nombre
    os.system('cls')
    if nombre!="":
        REPORTE_AP()
        RECORRIDO_AP()
        RESUMEN_AP()
        
        print("--------------------Mostrar autómata de pila equivalente--------------------")
    
        #Mostrando datos de la Gramática solicitada
        for i in GRAMATICAS:
            if i.nombre==nombre:
                print("______________________________________________________")
                print("Nombre de la gramática tipo 2: "+ str(i.nombre))
                
                print("No terminales = {",end="")
                for j in range(len(i.no_terminales)):
                    if j==(len(i.no_terminales)-1):
                        print(i.no_terminales[j],end="")
                    else:
                        print(i.no_terminales[j] +",",end="")    
                print("}\n", end="")
                
                print("Terminales = {", end="")
                for j in range(len(i.terminales)):
                    if j==(len(i.terminales)-1):
                        print(i.terminales[j],end="")
                    else:
                        print(i.terminales[j] +",",end="")
                print("}\n", end="")
                
                print("No terminal Inicial = "+ str(i.inicial[0]))
                produccion=[]
                print("Producciones")
                for x in range(len(i.transiciones)):
                    produccion.append(i.transiciones[x].split("->"))
                #separando derecho
                print(produccion)
                m="λ,λ;#"
                s="λ,λ;"+i.inicial
                q="λ,#;λ"
                trans=[]
                for x in range(len(produccion)):
                    a=produccion[x][0]
                    b=produccion[x][1]
                    c=("λ,"+str(a.replace(" ",""))+";"+str(b.replace(" ","")))
                    trans.append(c)
                for t in range(len(i.terminales)):
                    a=i.terminales[t]
                    y=a+","+a+";λ"
                    trans.append(y)
                cadena=""
                for p in trans:
                    cadena=cadena + str(p)+"\n"

                print("imprimiendo cadena")
                print(cadena)
        with open("apq.dot", mode="w",encoding="utf-8") as o:
            o.write("digraph automatadepila{ \n");
            o.write("rankdir=LR;\n");
            o.write("node[style=filled ,color=\"#28EE99\"];\n");
            o.write("nodo1[label=\"i\" ,shape=circle];\n");
            o.write("nodo2[label=\"p\" ,shape=circle];\n");
            o.write("nodo3[label=\"q\" ,shape=circle, width=0.8];\n");
            o.write("nodo4[label=\"f\" ,shape=doublecircle];\n");
            o.write("nodo1->nodo2[label=\""+m+"\"];")
            o.write("nodo2->nodo3[label=\""+s+"\"];")
            o.write("nodo3->nodo3[label=\""+cadena+"\"];")
            o.write("nodo3->nodo4[label=\""+q+"\"];")
            o.write("}\n");
        os.system('dot -Tpng apq.dot -o apq.png');
        webbrowser.open_new_tab('AUTOMATA_PILA.html')
    else:
        print("no se ha generado ninguna gramática")
    
def Op4():
    global REPORTE
    os.system('cls')
    print("--------------------Recorrido autómata de pila equivalente--------------------")
    
    print("GRAMÁTICAS REGULARES (NO SE CARGARON)")
    for i in REPORTE:
        
        print("______________________________________________________")
        print("Nombre de la gramática tipo 2: "+ str(i.nombre))
            
        print("No terminales = {",end="")
        for j in range(len(i.no_terminales)):
            if j==(len(i.no_terminales)-1):
                print(i.no_terminales[j],end="")
            else:
                print(i.no_terminales[j] +",",end="")    
        print("}\n", end="")
            
        print("Terminales = {", end="")
        for j in range(len(i.terminales)):
            if j==(len(i.terminales)-1):
                print(i.terminales[j],end="")
            else:
                print(i.terminales[j] +",",end="")
        print("}\n", end="")
            
        print("No terminal Inicial = "+ str(i.inicial[0]))
        produccion=[]
        print("Producciones")
        for x in range(len(i.transiciones)):
            produccion.append(i.transiciones[x].split("->"))
        o=0
        armando=[] 

        while o<len(i.no_terminales):
            trans=[]
            for x in range(len(produccion)):
                if produccion[x][0]==i.no_terminales[o]:
                    trans.append(produccion[x][1]) 
            armando.append(GRAMA(i.no_terminales[o],trans))
            o+=1

        #imprimiendo producción
        for i in armando:
            print(i.no_terminales+"->",end="")
            if len(i.transiciones)==1:
                for j in i.transiciones:
                    print(j) 
            elif len(i.transiciones)>1:
                for j in range(len(i.transiciones)):
                    if j==0:
                        print(i.transiciones[j])
                    else:
                        print("  | " + i.transiciones[j]) 
    """#Mostrando datos de la Gramática solicitada
    for i in GRAMATICAS:
        if i.nombre==nombre:
            print("______________________________________________________")
            print("Nombre de la gramática tipo 2: "+ str(i.nombre))
            
            print("No terminales = {",end="")
            for j in range(len(i.no_terminales)):
                if j==(len(i.no_terminales)-1):
                    print(i.no_terminales[j],end="")
                else:
                    print(i.no_terminales[j] +",",end="")    
            print("}\n", end="")
                
            print("Terminales = {", end="")
            for j in range(len(i.terminales)):
                if j==(len(i.terminales)-1):
                    print(i.terminales[j],end="")
                else:
                    print(i.terminales[j] +",",end="")
            print("}\n", end="")
                
            print("No terminal Inicial = "+ str(i.inicial[0]))
            produccion=[]
            print("Producciones")
            for x in range(len(i.transiciones)):
                produccion.append(i.transiciones[x].split("->"))
            #separando derecho
            print(produccion)
            m="(i,λ,λ;p,#)"
            s="(p,λ,λ;q,"+i.inicial+")"
            q="(q,λ,#;q,produccion)"
            trans=[]
            print("Transiciones")
            
            for x in range(len(produccion)):
                a=produccion[x][0]
                b=produccion[x][1]
                c=("(q,s,#;q,")
                c=("λ,"+str(a.replace(" ",""))+";"+str(b.replace(" ","")))
                trans.append(c)
            for t in range(len(i.terminales)):
                a=i.terminales[t]
                y=a+","+a+";λ"
                trans.append(y)
            cadena=""
            for p in trans:
                cadena=cadena + str(p)+"\n"

            print("imprimiendo cadena")
            print(cadena)"""
    webbrowser.open_new_tab('RECORRIDO.html')

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
for i in range(5, 0, -1):
    sys.stdout.write(" \r ")
    sys.stdout.write(" --->{:2d}  ".format(i))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\r  BIENVENIDO !            \n")

input("\nEnter para continuar...")
os.system('cls')

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

