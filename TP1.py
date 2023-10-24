#Escribir una función que reciba el mensaje a cifrar (cadena de caracteres) y la clave de
#cifrado, y devuelva el mensaje cifrado, mediante el cifrado césar. Probarla utilizando doctest,
#con al menos 10 casos diferentes.

#*************************************************************

def crearRelacion():
    caracter_a_pos = {}
    pos_a_caracter = {}
    
    # Creamos una tabla con los caracteres que pueden desplazarse;
    # en nuestro caso  son sólo los alfanuméricos. La tabla asigna
    # al caracter "a" la posición 0, al "b" la posición 1 y así su-
    # cesivamente hasta llegar a la posición 63, que está asignada
    # al caracter "9". Esta tabla se opera con dos diccionarios, uno
    # que dado un caracter devuelve su posición, y otro que dada una
    # posición devuelve un caracter
    
    digitos    = "0123456789"
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    caracteres = minusculas + mayusculas + digitos
    
    i = 0
    while(i < len(caracteres)):
        caracter_a_pos[caracteres[i]] = i
        pos_a_caracter[i] = caracteres[i]
        i += 1
        
    return (caracter_a_pos, pos_a_caracter)
    
# Diccionarios de caracter a posición y viceversa. Se crea una sola
# vez para evitar construirlos reiteradas veces en cada llamada a las
# funciones de cifrado.

relacion = crearRelacion()
caracter_a_pos = relacion[0]
pos_a_caracter = relacion[1]
del relacion

def desplazar(caracter, clave):

    # Desplaza un solo caracter hacia la derecha 'clave' veces, usando
    # la tabla de caracteres y posiciones definida por los diccionarios
    # caracter_a_pos y pos_a_caracter

    # cantidad : Tamaño del grupo según tipo de caracter. Hay 27 minúsculas, 27 mayúsculas y 10 dígitos
    # offset   : distancia del primer caracter del grupo al inicio de la tabla. La "a" dista 0 posiciones, 
    #            la "A" 27 y el "0" 54
    # alnum    : Indicador de caracter alfanumérico. Si es falso el caracter hallado no se altera.

    cantidad = 0
    offset   = 0
    alnum = True
    
    if(caracter.islower()):
        cantidad = 27
        offset   = 0
    elif(caracter.isupper()):
        cantidad = 27
        offset   = 27
    elif(caracter.isdigit()):
        cantidad = 10
        offset   = 54
    else:
        alnum = False
        
    if(alnum):
        valor = ((caracter_a_pos[caracter] - offset) + clave) % cantidad
        caracter = pos_a_caracter[valor + offset]
        
    return caracter
    
    
def cifrar_c(cadena, clave):

    """
    
    >>> cifrar_c("A", 4)
    'E'
    
    Se desplaza último caracter del abecedario:
    >>> cifrar_c("Z", 3)
    'C'
    
    Los caracteres que no son alfanuméricos no se desplazan:
    >>> cifrar_c("$#---/ABC", 5)
    '$#---/FGH'
    
    >>> cifrar_c("PERRO", 1)
    'QFSSP'
    
    >>> cifrar_c("     ", 10)
    '     '
    
    >>> cifrar_c("PERRO", 1) == cifrar_c("PERRO", 1 + 27)
    True
    
    >>> cifrar_c("HOLA MUNDO%%%&%/...;", 7) == cifrar_c("HOLA MUNDO%%%&%/...;", 7 + 27 * 8000)
    True
    
    >>> cifrar_c("6000-3288", 1)
    '7111-4399'
    
    >>> cifrar_c("9999-9999-caño", 1)
    '0000-0000-dbop'
    
    >>> cifrar_c("Illuminatis", 0) == "Illuminatis"
    True
    
    """

    codigo = ""
    
    for c in cadena:
        codigo += desplazar(c, clave)
        
    return codigo
    
    
def descifrar_c(codigo, clave):
    return cifrar_c(codigo, -clave)
    
    
if __name__ == "__main__":
    import doctest  
    doctest.testmod()
    

    