#Ponerle comillas a un texto
mi_texto ="Master"
mi_texto2 ="en \"Python\" "

texto_unido = mi_texto + " "+ mi_texto2 
print (texto_unido)

#Salto de linea
texto_unido = mi_texto + " \n "+ mi_texto2 
print (texto_unido)

#Tabulacion
texto_unido = mi_texto + " \t "+ mi_texto2 
print (texto_unido)

#Quitar el texto que esta antes de la r por lo que solo aparece "en Python"
texto_unido = mi_texto + " \r "+ mi_texto2 
print (texto_unido)