Datos={
    "Alumnos": [
        {
            "nombre":"Mateo",
            "apellido":"Segura",
            "dni":1234,
            "fecha de nacimiento":"27/11/2005",
            "tutor":"Carlos Segura",
            "notas":[10,9,8,7,4,6],
            "faltas":2,
            "amonestaciones":1
        },
        {
            "nombre":"Nacho",
            "apellido":"Ramos",
            "dni":1233,
            "fecha de nacimiento":"12/2/2006",
            "tutor":"Jose Ramos",
            "notas":[1,2,0,5,7,2],
            "faltas":5,
            "amonestaciones":3
        },
        {
            "nombre":"Agustina",
            "apellido":"Martinez",
            "dni":1224,
            "fecha de nacimiento":"3/3/2006",
            "tutor":"La Pali",
            "notas":[10,10,10,9,10,9],
            "faltas":0,
            "amonestaciones":0
        }
    ]
}
print(f"El alumno 1 es {Datos["Alumnos"][0]}")
print(f"El alumno 2 es {Datos["Alumnos"][1]}")
print(f"El alumno 3 es {Datos["Alumnos"][2]}")
#Pregunta si quiere agregar a un nuevo alumno
pregunta=input("Quiere agregar un nuevo alumno?: ").lower()
j=3
while pregunta=="si":
    #Ingresa datos nuevos
    auxnotas=[]
    nom=input("Ingrese el nombre del nuevo alumno: ")
    ap=input("Ingrese el apellido del nuevo alumno: ")
    DNI=int(input("Ingrese el DNI del nuevo alumno: "))
    fecha_de_nac=input("Ingrese la fecha de nacimiento del nuevo alumno(dd/mm/aaaa): ")
    tutor=input("Ingrese el nombre y apellido del tutor del nuevo alumno: ")
    #Usa un for i para las notas q son 6
    for i in range (1,7):
        nota=int(input("Ingrese las notas del alumno: "))
        auxnotas.append(nota)
    faltas=int(input("Ingrese la cantidad de faltas: "))
    amonestaciones=int(input("Ingrese la cantidad de amonestaciones: "))
    nuevo_alumno={
        "nombre":nom,
        "apellido":ap,
        "dni":DNI,
        "fecha de nacimiento":fecha_de_nac,
        "tutor":tutor,
        "notas":auxnotas,
        "faltas":faltas,
        "amonestaciones":amonestaciones
    }
    #Agrega al alumno a la lista
    Datos["Alumnos"].append(nuevo_alumno)
    print(f"El alumno {j+1} es {Datos["Alumnos"][j]}")
    pregunta=input("Quiere agregar un nuevo alumno?: ").lower() #Usa la pregunta para ver si quiere agregar a otro alumno
    j=j+1

#Si pregunta si quiere editar algun dato
pregunta=input("Quieres cambiar el dato de algun alumno?: ").lower()
while pregunta=="si":
    auxpreg=int(input("De que alumno?: ")) #De que alumno quiere cambiar el dato
    auxpreg2=input("Que dato quieres cambiar?: ").lower() #Que dato quiere cambiar
    if auxpreg2=="notas": #Este if sirve para ver si son notas, para agregarlo en forma de lista
        auxnotas=[]
        for i in range (1,7):
            nota=int(input("Ingrese las notas del alumno: "))
            auxnotas.append(nota)
            Datos["Alumnos"][auxpreg-1][auxpreg2]=auxnotas
    else: #Si no son notas se cambia de forma normal
        Datos["Alumnos"][auxpreg-1][auxpreg2]=input("Ingresa el nuevo dato: ")
    print(Datos["Alumnos"][auxpreg-1])
    pregunta=input("Quieres cambiar el dato de algun alumno?: ").lower() #Se pregunta de vuelta si quiere cambiar otro dato
    
#Se pregunta si desea eliminar a algun alumno y a cual alumno quiere eliminar
pregunta=input("Desea eliminar a un alumno?: ").lower()
while pregunta=="si":
    auxpreg3=int(input("Que alumno desea aliminar?: "))
    del (Datos["Alumnos"][auxpreg3-1]) #Se lo elimina con la funcion del
    pregunta=input("Desea eliminar a un alumno?: ").lower()

aux=0
for c in (Datos["Alumnos"]):
    aux=aux+1
    print(f"El alumno {aux} es {c}") #Se muestran los resultados finales