def aCadena(n, base):
    cadenaConversion = "0123456789ABCDEF"
    
    if n < base:
        return cadenaConversion[int(n)]
        
    else:
        return aCadena(int(n)/int(base), int(base)) + cadenaConversion[int(n)%int(base)]


print(aCadena(9, 2))