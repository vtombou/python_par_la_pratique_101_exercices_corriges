def join(*args):
    separateur = args[0]
    ret = args[1]
    if len(args) >= 2 :
        for i in range(2, len(args)):
            ret += separateur + args[i]
    
    return ret
        
    

j = join(":", "Bonjour", "tout", "le", "monde")
print(j)