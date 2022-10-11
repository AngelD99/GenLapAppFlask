
def Convert(string):
    caracteres_rechazados = """"()[]'"""

    for caracter in caracteres_rechazados:
        string = string.replace(caracter,"")
    
    tupla = tuple(string.split(","))
    return tupla

def eliminarEspacios(string):
    caracteres_rechazados = " ()''[]"

    for caracter in caracteres_rechazados:
        string = string.replace(caracter,"")
    
    tupla = tuple(string.split(","))
    return tupla

def eliminarCaracteres(string):
    caracteres_rechazados = " ,()''[]"

    for caracter in caracteres_rechazados:
        string = string.replace(caracter,"")
    
    return string

def eliminarVacios(tupla):

    tupla2 = tuple([elemento_lista for elemento_lista in list(tupla) if elemento_lista != ''])
    return tupla2