# Las condicionales son estructuras de control que se utilizan para comprobar
# si los datos son (True or False) y asi ejecutar uno de los dos bloques de 
# instrucciones. 

# La estructura se inicia llamando a la palabra clave if condición: sentencia

x = 20 
y = 10

if x > y:
    print("x es mayor que y.")          

## Se puede retornar un string o un booleano. ##
    
else:
    print(False)                 

# Caso inverso- 
    
x = 10
y = 20 

if x < y:
    print("x es menor que y.")        
    
else:
    print(False) 
    
    
# Creando otra condicional. 

name_one = "Luque"
name_two = "Carlo" 

if name_one == name_two:
    print(f"\nHola, {name_two}.")
    print("¿Como estas?")    

else:
    print("\nEse nombre no es correcto.")                                        
    
    
# Se pueden colocalar varias condiciones en la misma linea.
# No obstante se evalúa una sola vez    
   
if 10 > 5 < 15:
    print(True)
    
else:
    print(False)
    
    
## ... ##            

if 5.0 >= 4.0 < 7.5:
    print(True)
    
    
else:
    print(False)    
