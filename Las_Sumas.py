'''
* Crea una función que encuentre todas las combinaciones de los números
* de una lista que suman el valor objetivo.
* - La función recibirá una lista de números enteros positivos
*   y un valor objetivo.
* - Para obtener las combinaciones sólo se puede usar
*   una vez cada elemento de la lista (pero pueden existir
*   elementos repetidos en ella).
* - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
*   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
*   (Si no existen combinaciones, retornar una lista vacía)
'''
 
def find_sums (numbers: list, target: int) -> list:
     
     def find_sum(start: int,target: int, combination: list):
         
        if target == 0:
            print(combination)
            result.append(combination)
            return
     
        if target < 0 or start == len(numbers):
            return
        
        
        for i in range(start, len(numbers)):
            
            if numbers[i] == numbers[i - 1]:
                continue
            
            combination.append(numbers[i])
            find_sum(i + 1, target - numbers[i], combination)
            combination.pop()
     numbers.sort()
     result = []
     find_sum(0, target, [])
     return result
 
 
print(find_sums([1, 5, 3, 2],6))