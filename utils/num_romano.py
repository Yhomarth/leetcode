
def romanToInt( s: str) -> int:
    """
    Funcion que devuelve en enteros los numeros romanos
    """
    nums = {       
            "I" : 1,
            "V": 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000        
            }        
    
    lista = list(s)
    
    suma = 0
    for i,v in enumerate(lista):
    
        if i < (len(lista) - 1):
            if(nums[v] < nums[lista[i+1]]) : 
                suma -= nums[v]
            else:
                suma += nums[v]
        else : 
            suma += nums[v]    
    return suma

