# El if anidado se usa para colocar varias sentencias if dentro de otras if

# En la práctica no es muy recomendado anidar tantos if 
# se considera código innecesario y se vuelvo muy poco legible la estructura.

## Ejemplo 1 ##

if 20 >= 10:
    print("20 es mayor que 10.")
    if 10 < 20:
        print("10 es menor que 20")     
        
else:
    print(False)        
    
## Ejemplo 2 ##   
 
pet = "Dog"
pet_in_data_base = "Dog"   

name = "Mauldred"
name_in_data_base = "Mauldred"

if pet == pet_in_data_base:
    print(f"Esta es mi mascota.")
    if name == name_in_data_base:
        print(f"El nombre de mi mascota es {name}.")
        
    else:
        print(False)
            
else:
    print(False) 
    
## Ejemplo 3 ##

if 0 < 30 > 20:
    print(True)
    if 40 > 35 < 50:
        print(True)     
        
              
    else:
        print(False)      
        
                     
else:
    print(False)  
    
    
## Ejemplo 4 ##

x = 5.0
y = 7.5

resultado = x + y

if resultado == 12.5:
    print("El resultado de a suma es 12.5")    
    if x < y:
        print(True)
    
else:
    print("La suma es incorrecta.")         
