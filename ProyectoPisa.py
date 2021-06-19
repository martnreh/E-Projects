
#------------------------------------------------------------
#----------------------Librerías Importadas------------------
#------------------------------------------------------------
import random

#------------------------------------------------------------
#----------------------Crear archivo csv------------------
#------------------------------------------------------------

#Esta sección abre el archivo csv que recogerá y guardará todas las respuestas correctas correctas contestadas por el alumno 
calificaciones = open('calificaciones.csv' , 'w')
#lecturacalif = califinales.read_excel('calificaciones.xlsx')


#------------------------------------------------------------
#----------------------Funciones-----------------------------
#------------------------------------------------------------

#Estas variables se utilizan como counters para ir almacenando el numero de preguntas que contesta el alumno y a la vez cuales de esas estuvieron correctas
PreguntasCorrectas = 0
PreguntasTotales = 0

#La función muestra_incisos imprime en la pantalla de manera organizada por renglón las opciones de respuesta que tiene el alumno para elegir.
def muestra_incisos(mat):
    for ren in range(len(mat)):
        for col in range(len(mat[0])):
            print(f'{mat[ren][col]:3}', end='')
        print()
        
# Si la respuesta correcta a un problema es el inciso a, se manda llamar a esta función respuesta_a que compara la respuesta del alumno y la respuesta correcta.
# Evalúa si tiene el acierto o no, de tenerlo escribe en el archivo calificaciones.csv que tiene una respuesta correcta y una respuesta respondida.
# De no ser así, se muestra que ha sido incorrecta y en el archivo csv se escribe que tiene una respuesta incorrecta y una respuesta respondida.
def respuesta_a(x):
    if x == "a":
        print(" ")
        print("Correcto")
        print(" ")
        calificaciones.write(str(1) + ',' + str(1) + '\n')   
    
    else:
        print(" ")
        print("Incorrecto")
        print(" ")
        calificaciones.write(str(0) + ',' + str(1) + '\n')

# Si la respuesta correcta a un problema es el inciso b, se manda llamar a esta función respuesta_b que compara la respuesta del alumno y la respuesta correcta.
# Evalúa si tiene el acierto o no, de tenerlo escribe en el archivo calificaciones.csv que tiene una respuesta correcta y una respuesta respondida.
# De no ser así, se muestra que ha sido incorrecta y en el archivo csv se escribe que tiene una respuesta incorrecta y una respuesta respondida.
def respuesta_b(x):
    if x == "b":
        print(" ")
        print("Correcto")
        print(" ")
        calificaciones.write(str(1) + ',' + str(1) + '\n')
        
    
    else:
        print(" ")
        print("Incorrecto")
        print(" ")
        calificaciones.write(str(0) + ',' + str(1) + '\n')
        
        

# Si la respuesta correcta a un problema es el inciso c, se manda llamar a esta función respuesta_c que compara la respuesta del alumno y la respuesta correcta.
# Evalúa si tiene el acierto o no, de tenerlo escribe en el archivo calificaciones.csv que tiene una respuesta correcta y una respuesta respondida.
# De no ser así, se muestra que ha sido incorrecta y en el archivo csv se escribe que tiene una respuesta incorrecta y una respuesta respondida.       
def respuesta_c(x):

    if x == "c":
        print(" ")
        print("Correcto")
        print(" ")
        calificaciones.write(str(1) + ',' + str(1) + '\n')    
    
    else:
        print(" ")
        print("Incorrecto")
        print(" ")
        calificaciones.write(str(0) + ',' + str(1) + '\n')
        
        

# Si la respuesta correcta a un problema es el inciso d, se manda llamar a esta función respuesta_d que compara la respuesta del alumno y la respuesta correcta.
# Evalúa si tiene el acierto o no, de tenerlo escribe en el archivo calificaciones.csv que tiene una respuesta correcta y una respuesta respondida.
# De no ser así, se muestra que ha sido incorrecta y en el archivo csv se escribe que tiene una respuesta incorrecta y una respuesta respondida.
def respuesta_d(x):
    if x == "d":
        print(" ")
        print("Correcto")
        print(" ")
        calificaciones.write(str(1) + ',' + str(1) + '\n')
        
    
    else:
        print(" ")
        print("Incorrecto")
        print(" ")
        calificaciones.write(str(0) + ',' + str(1) + '\n')
        
        


# La función solución recibe en el parámetro de correcta la respuesta acertada que se genera a través del programa en los problemas matemáticos. En el parámetro de
# usuario la respuesta que ingresa el alumno. Dentro de la función se evalua si ambas variables son iguales,escribe en el archivo calificaciones.csv que tiene una respuesta correcta y una respuesta respondida.
# De no ser así, se muestra que ha sido incorrecta y en el archivo csv se escribe que tiene una respuesta incorrecta y una respuesta respondida.

def solucion(correcta,usuario):
    if usuario == correcta:
        print(" ")
        print("Correcto")
        print("\n \n")
        calificaciones.write(str(1) + ',' + str(1) + '\n')
        
    else:
        print(" ")
        print("Incorrecto")
        print(" ")
        calificaciones.write(str(0) + ',' + str(1) + '\n')


#La función pregunta_azar recibe como parámetro una lista de preguntas. Se mide la longitud de la lista para saber cuántas preguntas hay y se le resta uno para
#crear un rango que se guarda en la variable largo. Se crea un número random dentro de ese rango. Ahora ya se tiene elegida una pregunta dentro de la lista.
# Con la variable largointerno se mide cuantos incisos de la pregunta hay dentro de esa lista interna. Se utiliza un for para imprimir cada uno de los índices, es decir,
# mostrar los incisos al alumno. El if x == 1 es para asegurarse que haya un espacio entre la pregunta y los incisos. Al final del for, la variable correcta
# toma el valor dentro de la lista donde se encuentra la pregunta que fue elegida al azar y se guarda el último índice. Es decir, se guarda la respuesta correcta
# y finalmente se regresa esa respuesta al programa principal dónde fue llamada la función.

def pregunta_azar(lista):
    import random
    #estructura de lista admitida = [["Pregunta1","a","b","c","d","letracorrecta"]]
    largo = len(lista) - 1
    random = random.randint(0,largo)
    
    largointerno = len(lista[random]) - 1
    x = 0
    for azar in range (0,largointerno):
        print(lista[random][azar])
        x += 1
        if x == 1:
            print("\n")
            x += 1
        
    correcta = lista[random][largointerno]
    
    return correcta
    
    
    

#----------------------------------------------------------------------
#---------------------Programa Principal-------------------------------
#----------------------------------------------------------------------
print('¡Bienvenido! Este es programa computacional que busca apoyarte para mejorar tus habilidades y conocimientos en una de las pruebas que que evalúa la prueba PISA de la OCDE')
print('Esta prueba de repaso contiene primeramente un parte de Física y es seguida por una de Química.')
print('Contesta las preguntas siguientes y mira tu resultado al final del examen. \n ')
print("-Ingresa el inciso que corresponda a tu respuesta (ingresa la letra correspondiente en minúscula). \n \n \n  ")
#--------------------------------------------------------------------------------
#--------------------Parte Teórica de Física-------------------------------------
#--------------------------------------------------------------------------------

print('\t\t\t\t\t\t\tParte de Física')

#Pregunta1
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_a().

print(" ")
print(" ")
print("¿Qué es la física?")
print(" ")
print(" ")
Pregunta1 = [["a) La ciencia que estudia las propiedades de la materia y la relación de los conceptos que forman el universo como: energía, espacio y tiempo; para la explicación de fenómenos."], ["b) La ciencia que estudia la composición, la estructura y el comportamiento molecular de la materia, incluyendo su cambio, para la explicación de fenómenos."], ["c) La ciencia que estudia a los seres vivos, las características físicas y comportamientos individuales o en conjunto."], ["d) Ciencia que tiene por objeto el estudio, la interpretación, integración y sistematización de un ordenamiento jurídico para su justa aplicación."]]
muestra_incisos(Pregunta1)
print(" ")
print(" ")
pregunta1 = str(input("Ingresa respuesta: ")).lower()
respuesta_a(pregunta1)
print(" ")
print(" ")
print(" ")

#Pregunta2
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_c().
print("¿Qué es desplazamiento?")
print(" ")
print(" ")
Pregunta2 = [["a) La distancia total recorrida por un objeto en un intervalo de tiempo."], ["b) El tiempo que tarda en llegar del punto de origen al punto final."], ["c) La distancia resultante que existe entre el punto de origen y el punto final de una trayectoria."], ["d) Es el cambio de posición de un objeto entre el tiempo empleado para lograr este cambio."]]
muestra_incisos(Pregunta2)
print(" ")
print(" ")
pregunta2 = str(input("Ingresa respuesta: ")).lower()
respuesta_c(pregunta2)
print(" ")
print(" ")
print(" ")


#Pregunta3
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_b().
print("¿Qué es velocidad?")
print(" ")
print(" ")
Pregunta3 = [["a) La distancia total recorrida entre el tiempo que toma recorrerla."], ["b) El desplazamiento de un punto a otro dividido entre el tiempo que toma llegar al punto final desde el punto inicial."], ["c) La distancia resultante que existe entre el punto de origen y el punto final de una trayectoria."], ["d) Se define como el tiempo que le toma a un objeto llegar a un punto final desde un punto inicial y dividirlo entre el desplazamiento del objeto."]]
muestra_incisos(Pregunta3)
print(" ")
print(" ")
pregunta3 = str(input("Ingresa respuesta: ")).lower()
respuesta_b(pregunta3)
print(" ")
print(" ")
print(" ")


#Pregunta4
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_d().
print("¿Cómo definirías la aceleración?")
print(" ")
print(" ")
Pregunta4 = [["a) Como el cambio de posición entre el tiempo."], ["b) Como el cambio de tiempo dividido entre el cambio de posición"], ["c) Como la distancia total recorrida entre el intervalo de tiempo total."], ["d) Como el cambio de velocidad en un intervalo de tiempo."]]
muestra_incisos(Pregunta4)
print(" ")
print(" ")
pregunta4 = str(input("Ingresa respuesta: ")).lower()
respuesta_d(pregunta4)
print(" ")
print(" ")
print(" ")



#Pregunta5
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_b().
print("¿Qué es la fuerza?")
print(" ")
print(" ")
Pregunta5 = [["a) Un campo de energía metafísico y omnipresente creado por las cosas que existen que impregna el universo y todo lo que hay en él manteniéndolo unido."], ["b) Es la interacción entre dos objetos que provoca que uno de estos cambie su estado de movimiento o forma."], ["c) Es una representación con flechas que debe tener una magnitud y una dirección."], ["d) Es una constante universal que no depende de la masa ni la aceleración."]]
muestra_incisos(Pregunta5)
print(" ")
print(" ")
pregunta5 = str(input("Ingresa respuesta: ")).lower()
respuesta_b(pregunta5)
print(" ")
print(" ")
print(" ")


#Pregunta6
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_a().
print("¿Qué establece la Primer Ley de Newton?")
print(" ")
print(" ")
Pregunta6 = [["a) Que todos los cuerpos permanecen en movimiento constante o reposo hasta que una fuerza se aplique sobre ellos."], ["b) Que todos los cuerpos en reposo se pueden mover sin que una fuerza sea aplicada."], ["c) Que la trayectoria órbital que recorren todos los planetas alrededor del Sol tiene forma de elipse."], ["d) Es una constante universal que no depende de la masa ni la aceleración."]]
muestra_incisos(Pregunta6)
print(" ")
print(" ")
pregunta6 = str(input("Ingresa respuesta: ")).lower()
respuesta_a(pregunta6)
print(" ")
print(" ")
print(" ")


#Pregunta7
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_d().
print("¿Qué es la fuerza neta?")
print(" ")
print(" ")
Pregunta7 = [["a) Es la fuerza reactiva de igual magnitud pero de sentido opuesto que ejerce un objeto B sobre el objeto A que se produce cuando el objeto A ejerce una fuerza sobre un objeto B."], ["b) Es la fuerza presente en la superficie que contrarrestra la fuerza que produce el movimiento de un objeto."], ["c) La fuerza neta siempre es igual a cero."], ["d) Es el resultante de la suma vectorial de todas las fuerzas que actúan sobre un objeto."]]
muestra_incisos(Pregunta7)
print(" ")
print(" ")
pregunta7 = str(input("Ingresa respuesta: ")).lower()
respuesta_d(pregunta7)
print(" ")
print(" ")
print(" ")


#Pregunta8
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_c().
print('¿Cómo se define la "Energía"?')
print(" ")
print(" ")
Pregunta8 = [["a) Se relaciona únicamente con el movimiento de los cuerpos."], ["b) Es la fuerza que se encarga de mover los objetos."], ["c) Es la capacidad de un sistema para llevar a cabo un trabajo determinado, cambiar su situación o estado."], ["d) Aquella que se obtiene por distintos métodos para abastecer de electricidad a una ciudad."]]
muestra_incisos(Pregunta8)
print(" ")
print(" ")
pregunta8 = str(input("Ingresa respuesta: ")).lower()
respuesta_c(pregunta8)
print(" ")
print(" ")
print(" ")


#Pregunta9
#Se despliega la pregunta. La lista contiene varios incisos de respuestas para dicha pregunta. Esa lista se manda a la función muestra_incisos() para desplegarlas al alumno.
# Se pide al alumno que ingrese su respuesta y se guarda en variable. El alumno puede ingresar la letra en mayuscula y el programa la transforma a minúscula. Una vez guardada
#se envía dicha respuesta para ser evaluada en la función respuesta_b().
print('"La energía no se crea ni se destruye, solo se transforma", ¿Qué Ley es esta?')
print(" ")
print(" ")
Pregunta9 = [["a) No existe."], ["b) La Segunda Ley de la Termodinámica."], ["c) La Segunda Ley de Newton."], ["d) No lo sé."]]
muestra_incisos(Pregunta9)
print(" ")
print(" ")
pregunta9 = str(input("Ingresa respuesta: ")).lower()
respuesta_b(pregunta9)
print(" ")
print(" ")
print(" ")

#-------------------------------------------------------------------------------------------------------------
#------------------------------------------Verdadero o Falso parte Fisica-------------------------------------
#-------------------------------------------------------------------------------------------------------------


#Verdad o Falso 1
#Pregunta10
#Esta es otra forma que se desarrolló para mostrar preguntas. Se tiene una lista de incluyendo una pregunta y la letra de la respuesta correcta. Se tiene otra lista
#con las opciones Verdadero y falso. Se imprime la pregunta y se imprime las opciones de respuesta en una sola línea. Después se pide a alumno que ingrese su propia respuesta.
# Gracias a un for se lee la segunda posición de la lista que incluye la respuesta correcta. Dentro del if se evalúa si la respuesta del alumno es igual al de la pregunta.
# Si lo es imprime Correcto y se agrega al rchivo csv el resultado, si no lo es se imprime incorrecto y también se agrega el resultado al mismo archivo.
V_F1 = [['Calor y temperatura son lo mismo.'],['b']]
V_F1_2 = ['a) Verdadero', 'b) Falso']
for i in (V_F1[0]):
    print(i)
    print(" ")
    print(V_F1_2)
    print(" ")
    print(" ")
    respuesta = str(input("Ingresa tu respuesta: ")).lower()
    for x in V_F1[1]:
        if respuesta == x:
            print(" ")
            print("Correcto")
            print(" ")
            print(" ")
            print(" ")
            calificaciones.write(str(1) + ',' + str(1) + '\n')
    
        else:
            print(" ")
            print("Incorrecto")
            print(" ")
            print(" ")
            print(" ")
            calificaciones.write(str(0) + ',' + str(1) + '\n')
        break

#Verdad o Falso 2
#Pregunta11
#Esta es otra forma que se desarrolló para mostrar preguntas. Se tiene una lista de incluyendo una pregunta y la letra de la respuesta correcta. Se tiene otra lista
#con las opciones Verdadero y falso. Se imprime la pregunta y se imprime las opciones de respuesta en una sola línea. Después se pide a alumno que ingrese su propia respuesta.
# Gracias a un for se lee la segunda posición de la lista que incluye la respuesta correcta. Dentro del if se evalúa si la respuesta del alumno es igual al de la pregunta.
# Si lo es imprime Correcto y se agrega al rchivo csv el resultado, si no lo es se imprime incorrecto y también se agrega el resultado al mismo archivo.
V_F2 = [['La energía mecánica se divide en dos partes: cinética y potencial.'],['a']]
V_F2_2 = ['a) Verdadero', 'b) Falso']
for i in (V_F2[0]):
    print(i)
    print(" ")
    print(V_F2_2)
    print(" ")
    print(" ")
    respuesta = str(input("Ingresa tu respuesta: ")).lower()
    for x in V_F2[1]:
        if respuesta == x:
            print(" ")
            print("Correcto")
            print(" ")
            calificaciones.write(str(1) + ',' + str(1) + '\n')
    
        else:
            print(" ")
            print("Incorrecto")
            print(" ")
            calificaciones.write(str(0) + ',' + str(1) + '\n')
        break

#--------------------------------------------------------------------------------
#--------------------Parte Práctica de Física------------------------------------
#--------------------------------------------------------------------------------
print(" ")   
print('Intrucciones: Escribe las respuestas de tus resulatados solamente en números. Lee bien si te pide número entero o con decimal redondeado.')   
print(' De no tener una respuesta y querer continuar, pon como resultado 0')
#Pregunta12
# Se genera un numero random entre -5 y 20 incluyéndolos. Se tienen valores para las variables vi, a y t. Estos representan velocidad inicial, aceleración y tiempo.
# El valor random se suma a cada uno de ellos para tener un problema con numero más reales y que no todos sean negativos. Además el tiempo se asegura que su valor sea
# positivo dandole a la suma su valor absoluto. El programa calcula la solución del problema y lo guarda en la variable respuesta.
#Se imprime la pregunta con dentro de ella los valores de las varables que fueron modificadas. Finalmente se envían dos parametros a la función solucion().
# Se envían la respuesta correcta y la respuesta del alumno.
print(" ")
print(" ")
random = random.randint(-5,20)
vi = 10 + random
a = 2 + random
t = abs(3 + random)
respuesta = vi + a*t
    

Problema12 = int(input("Resuelve para velocidad final cuando el objeto inicia con velocidad " + str(vi) +  " m/s a una aceleración de " + str(a)+ " m/s^2 en un tiempo de " + str(t) + " segundos. Ecuación: vf = vi + at \n \n Respuesta en numero entero:  "))   
solucion(respuesta, Problema12)

#Pregunta13
# La variable de tiempo t recibe el valor de un número random generado transformandolo en float y sumandole 6. El problema se divide en dos partes por lo que primero se soluciona
#para obtener la velocidad inicial y el resultado se le asigna a la variable respuesta1. La variable respuesta utiliza la velocidad inicial con demás calculos para obtener
# la distancia en el eje y del movimiento parabólico de la pelota de golf. Se transforma esa respuesta en un formato de dos decimales redondeados. Finalmente se imprime
#la pregunta al alumno. Se recibe su respuesta como float, pero se transforma en string para llevarlo a la función solución además con la respuesta correcta.
print(" ")
print(" ")
t = float(random) + 6.0
respuesta1 = 9.81 * (t/2)
respuesta = (respuesta1 * (t/2)) - ( (9.81*((t/2)**2)) / 2) 
respuesta = "{:.2f}".format(respuesta)    
Problema13 = float(input("Una pelota de golf se lanza hacia arriba en un tiro vertical, su velocidad inicial es desconocida y se sabe que regresa al suelo después de " + str(t) + " segundos.  Ten en cuenta el valor de la gravedad como: -9.81 m/s^2 y calcula la altura máxima de la pelota. Redodea tu resultado a dos decimales.\n \n Respuesta: "))
Problema13 = str(Problema13)
solucion(respuesta, Problema13)
print('\n')



#--------------------------------------------------------------------------------
#--------------------Parte teórica Química --------------------------------------
#--------------------------------------------------------------------------------

print('\t\t\t\t\t\t\tParte de Química')
print('\n\n')
    
#Pregunta14
#Se tiene una lista compleja donde hay varias preguntas dentro de ella. Se envía la lista a la función pregunta azar dónde se elige una pregunta totalmente random de esa lista
# y se regresa el valor de la respuesta correcta al programa principal, se asigna a la variable correcta y además despliega la pregunta y los incisos a el alumno.
#Se pide al alumno que ingrese su respuesta. La variable possibles con globals().copy y possibles.update(locals()) permite usar el string en la variable correcta y que al sumarlo con el string
# de 'respuesta_' se cree el nombre de la función donde se evaluará. Se hace esto ya que si solo se suman los strings, se crea un string por ejemplo 'respuesta_a'pero este no puede llamar una función.
# No debe de tener comillas por lo que se buscó otra manera de transformarlo, se regresa la palabra con possibles.get() de nuevo a tipo texto para que python pueda leerlo y se llama función para evaluar la respuesta.
lista18 = [["Un gas no tiene una figura fija pero sí tiene un volumen fijo y no puede ser comprimido.","a) Verdadero","b) Falso","b"],["La materia es un conjunto de partículas, átomos, moléculas, sus partículas se mueven constantemente.","a) Verdadero","b) Falso","a"]]
correcta = pregunta_azar(lista18)
print('\n')
pregunta18 = str(input("Ingresa respuesta: ")).lower()
possibles = globals().copy()
possibles.update(locals())
stringf = ("respuesta_" + correcta)
funcion = possibles.get(stringf)
funcion(pregunta18)
print('\n')

#Pregunta15
#Se tiene una lista compleja donde hay varias preguntas dentro de ella. Se envía la lista a la función pregunta azar dónde se elige una pregunta totalmente random de esa lista
# y se regresa el valor de la respuesta correcta al programa principal, se asigna a la variable correcta y además despliega la pregunta y los incisos a el alumno.
#Se pide al alumno que ingrese su respuesta. La variable possibles con globals().copy y possibles.update(locals()) permite usar el string en la variable correcta y que al sumarlo con el string
# de 'respuesta_' se cree el nombre de la función donde se evaluará. Se hace esto ya que si solo se suman los strings, se crea un string por ejemplo 'respuesta_a'pero este no puede llamar una función.
# No debe de tener comillas por lo que se buscó otra manera de transformarlo, se regresa la palabra con possibles.get() de nuevo a tipo texto para que python pueda leerlo y se llama función para evaluar la respuesta.
lista19 = [["Sublimación es el cambio de estado de materia de sólido a gas.","a) Verdadero","b) Falso","a"],["Condensación es el cambio de estado de materia de líquido a gas.","a) Verdadero","b) Falso","b"]]
correcta = pregunta_azar(lista19)
print('\n')
pregunta19 = str(input("Ingresa respuesta: ")).lower()
possibles = globals().copy()
possibles.update(locals())
stringf = ("respuesta_" + correcta)
funcion = possibles.get(stringf)
funcion(pregunta19)
print('\n')


#Pregunta16
#Se tiene una lista compleja donde hay varias preguntas dentro de ella. Se envía la lista a la función pregunta azar dónde se elige una pregunta totalmente random de esa lista
# y se regresa el valor de la respuesta correcta al programa principal, se asigna a la variable correcta y además despliega la pregunta y los incisos a el alumno.
#Se pide al alumno que ingrese su respuesta. La variable possibles con globals().copy y possibles.update(locals()) permite usar el string en la variable correcta y que al sumarlo con el string
# de 'respuesta_' se cree el nombre de la función donde se evaluará. Se hace esto ya que si solo se suman los strings, se crea un string por ejemplo 'respuesta_a'pero este no puede llamar una función.
# No debe de tener comillas por lo que se buscó otra manera de transformarlo, se regresa la palabra con possibles.get() de nuevo a tipo texto para que python pueda leerlo y se llama función para evaluar la respuesta.
lista20 = [["Método utilizado para separar un líquido  de un sólido que es insoluble o dos líquidos que no pueden disolverse entre sí y por la gravedad se separan.","a) Decantación","b) Destilación","c) Evaporación","d) Sublimación","a"],["Método utilizado para la separación de sustancias aplicando altas temperaturas a las mezclas como agua y alcohol. La sustancia con un punto de ebullición menor se evaporará primero y se separará de la otra sustancia.","a) Sublimación","b) Filtración","c) Destilación","d) Cristalización","c"]]
correcta = pregunta_azar(lista20)
print('\n')
pregunta20 = str(input("Ingresa respuesta: ")).lower()
possibles = globals().copy()
possibles.update(locals())
stringf = ("respuesta_" + correcta)
funcion = possibles.get(stringf)
funcion(pregunta20)
print('\n')


#Pregunta17
#Se tiene una lista compleja donde hay varias preguntas dentro de ella. Se envía la lista a la función pregunta azar dónde se elige una pregunta totalmente random de esa lista
# y se regresa el valor de la respuesta correcta al programa principal, se asigna a la variable correcta y además despliega la pregunta y los incisos a el alumno.
#Se pide al alumno que ingrese su respuesta. La variable possibles con globals().copy y possibles.update(locals()) permite usar el string en la variable correcta y que al sumarlo con el string
# de 'respuesta_' se cree el nombre de la función donde se evaluará. Se hace esto ya que si solo se suman los strings, se crea un string por ejemplo 'respuesta_a'pero este no puede llamar una función.
# No debe de tener comillas por lo que se buscó otra manera de transformarlo, se regresa la palabra con possibles.get() de nuevo a tipo texto para que python pueda leerlo y se llama función para evaluar la respuesta.
lista21 = [["Una mezcla heterogénea tiene una composición y propiedades uniformes como el agua salada.","a)Verdadero","b) Falso","b"],["Una mezcla homogénea no tiene una composición uniforme y sus propiedades varían. Similar a una ensalada o la tierra de jardín.","a)Verdadero","b)Falso","b"]]
correcta = pregunta_azar(lista21)
print('\n')
pregunta21 = str(input("Ingresa respuesta: ")).lower()
possibles = globals().copy()
possibles.update(locals())
stringf = ("respuesta_" + correcta)
funcion = possibles.get(stringf)
funcion(pregunta21)
print('\n')


#--------------------------------------------------------------------------------
#------------------Preguntas agregadas por usuario desde archivo excel ----------
#--------------------------------------------------------------------------------

# Se importa la librería xlrd la cual permite poder accesar y y leer archivos .xlsx de excel. La variable path recibe el archivo que contiene preguntas pregrabadas pero pueden
# ser modificadas por el alumno. En inputWorkbook se pide abrir el archivo y leerlo. En inputWorksheet se pide leer solo la columa 1. Con inputWorksheet.nrows se le asigna
# a la variable rows la cantidad de renglones que tiene el archivo y se asigna a veces el numero de preguntas que hay en el archivo diviendo entre 6 la cantidad de renglones.
# Esto ya que deben de estar las preguntas en el archivo excel escritas solo en la primera columna hacia abajo y deben de ser pregunta,4 incisos y letra correcta seguida de la siguiente pregunta.
# Por lo que son 6 renglones por pregunta. Gracias a un for se leen 5 renglones y se imprimen para el alumno. Se pide que ingrese su respuesta y se guarda. La variable correcta
# recibe el valor de la ultima posición del for + 1. Es decir se queda en el 5 renglón al imrpimir y guarda la letra del sexto. Otra vez utilizandoglobals.copy() y .update(locals()) se
# manda a llamar la función respuesta_ y su letra correcta para evaluar la pregunta y despliega el resultado al alumno. Todo este proceso se repite el numero de veces, es decir
# el numero de preguntas que haya. Para esto en el count de rango x y rango y van aumentando de 6 en 6 cada vez que termina una pregunta para que el programa sepa desde dónde empezar a leer.
#El resultado de estas preguntas también se agregan al rchivo csv de calificaciones.
import xlrd

path = 'PreguntasdeUsuario.xlsx'
print('\t\t\t\t\t\t\tPreguntas añadidas por el usuario')
print('\n\n')
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)
#print(inputWorksheet.nrows)
#print(inputWorksheet.ncols)
rows = inputWorksheet.nrows
veces = int(rows/6)

rangox = 0
rangoy = 5
if rows <=0:
    print('No hay preguntas añadidas en el archivo excel')
for x in range (0,veces):
    p = 0
    for x in range (rangox,rangoy):
        print(inputWorksheet.cell_value(x,0))
        p += 1
        if p == 1:
            print("\n")
            p+= 1
    print("\n")
    pregunta30 = str(input("Ingresa respuesta: ")).lower()
    possibles = globals().copy()
    possibles.update(locals())
    correcta = str(inputWorksheet.cell_value(x+1,0))
    stringf = ("respuesta_" + correcta)
    funcion = possibles.get(stringf)
    funcion(pregunta30)
    print('\n\n')
    rangox = rangox + 6
    rangoy = rangoy + 6

    
    

#--------------------------------------------------------------------------------
#------------------Cálculo de calificación final leyendo los resultados----------
#-------------------------------desde un archivo csv----------------------------- 
#--------------------------------------------------------------------------------   

#Aquí se cierra el archivo abierto de modo escritura de calificaciones.csv donde se escribieron todas las preguntas contestdas y correctas del alumno.  
calificaciones.close()

#Ahora se pide leer el archivo calificaciones.csv creado, escrito y cerrado anteriormente para poder leer las líneas. Si la longitud de la línea es 0, quiere decir que ya no hay datos y termina el programa.
# Si el programa lee que por linea si hay una longitud entra a un while que identificará todas las lineas con datos. Si la línea dice '1,1' quiere decir que el alumno contestó
# una pregunta y la obtuvo correcta y se actualizan las variables iniciales. De lo contrario, es decir, se lee la línea como '0,1', el alumno conestó la pregunta pero la obtuvo mal y solo se actualiza
# la variable de preguntas totales. Se imprime al alumno cuántas preguntas contestó, incuyendo las agregadas en el archivo excel, y cuántas de todas ellas las contestó bien.

print('\n\n')
lectura = open('calificaciones.csv', 'r')
linea = lectura.readline()
while len(linea) != 0:
    linea = lectura.readline()
    if linea == '1,1\n':
        PreguntasCorrectas += 1
        PreguntasTotales += 1
    else:
        PreguntasTotales += 1

print('Número de preguntas contestadas: ' + str(PreguntasTotales) + '\n')
print('Número de preguntas correctas: ' + str(PreguntasCorrectas) + '\n')

#Finalmente se calcula su calificación dividiendo entre 100 las preguntas totales y multiplicandolo por las correctas.
# Finalmente se imprime su calificación en porcentaje y además se imprime un mensaje al alumno y se cierra el archivo calificaciones.csv.

calif = 100/int(PreguntasTotales) * int(PreguntasCorrectas)

print("Calificación final: " +"{:.2f}".format(calif) + '%')

print('\n\n')
print('(Puedes ingresar tus propias preguntas con incisos dentro del archivo de excel PreguntasdeUsuario.xlsx)')
lectura.close()


#Termina el programa

