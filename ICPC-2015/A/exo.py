# importing "math" for mathematical operations  
import math  

def calcul(p, a, b, c, d, n):
    
    def price(k):
        return p * ( math.sin(a*k+b) + math.cos(c*k+d) + 2 )

    # declaration variables
    uppest_decline = 0.00
    current_decline = 0.00
    prev_uppest = price(0)
    prev_lowest = price(0)

    # parcours de la courbe des prix
    for k in range(1,n):
        # si le prix est plus bas que le plus bas obtenu sur cette descente
        if( price(k) <= prev_lowest):
            prev_lowest = price(k)
            current_decline = prev_uppest - prev_lowest
        # si le prix remonte au dessus du prix le plus haut
        elif( price(k) >= prev_uppest):
            if(current_decline > uppest_decline):
                uppest_decline = current_decline
            prev_uppest = price(k)
            prev_lowest = price(k)

    if(current_decline > uppest_decline):
                uppest_decline = current_decline
    return uppest_decline


# main()
line = input('Enter your values (p, a, b, c, d, n):')
tab = line.split(' ')

if(len(tab) < 6):
    print("Manque des valeurs")
else :
    print( calcul(int(tab[0]),int(tab[1]),int(tab[2]),int(tab[3]),int(tab[4]),int(tab[5])) )
