def main():
    
    route = 0
    test = int(input('nb de route: '))
    
    while test > 0:
        tmp = 1
        debut = 0
        fin = 0
        add = 0
        rep = 0
        i = 2
        j = int(input('nombre d'arret de la route {}: '.format(test)))
        
        for i in range(j-1):
            x = int(input('note de la route: '))
            add += x
            
            if add < 0:
                add = 0
                tmp = i
                
            if add >= rep:
                if add > rep or (add == rep and (i - tmp > fin - debut)):
                    debut = tmp + 2
                    fin = i + 2
                    
            rep = add
            
        i += 1
        route += 1
        
        if rep > 0:
            print("The nicest part of route {} is between stops {} and {}".format(route, debut, fin))
        else:
            print("Route {} has no nice parts".format(route))
        test -= 1

main()