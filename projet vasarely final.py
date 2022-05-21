def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """trace un pavage d'hexagones déformé par une sphére"""
    import turtle
    from math import pi, sin, cos, sqrt, acos, asin, atan2
    turtle.speed("fastest")
    
    def hexagone (point, longueur, col, centre, rayon):
        """renvoie au point de coordonnés point = (x, y, z) avant deformation un hexagone de cote de longueur avant déformation déformé par une sphére de centre (X0, Y0, Z0) et de rayon"""
        turtle.up()
        x, y, z = point[0], point[1], point[2]

        def deformation(p, centre, rayon):
            """ Calcul des coordonnées d'un point suite à  la déformation engendrée par la sphére émergeante\
            \Entrées :p : coordonnées (x, y, z) du point du dalage à  tracer (z = 0) AVANT déformation\
            \centre : coordonnées (X0, Y0, Z0) du centre de la sphére\
            \rayon : rayon de la sphére\
            \Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à  tracer APRES déformation"""
            x, y, z = p
            xprim, yprim, zprim = x, y, z
            xc, yc, zc = centre
            if rayon**2 > zc**2:
                if zc <= 0:
                    zc = zc
                else:
                    zc = -zc
            r = sqrt((x - xc) ** 2 + (y - yc) ** 2)# distance horizontale depuis le point à  dessiner jusqu'à  l'axe de la sphére
            rayon_emerge = sqrt(rayon ** 2 - zc ** 2)# rayon de la partie émergée de la sphére
            rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
            if 0 < r <= rayon_emerge:# calcul de la déformation dans les autres cas
                xprim = xc + (x - xc) * rprim / r # les nouvelles coordonnées sont proportionnelles aux anciennes
                yprim = yc + (y - yc) * rprim / r
            if r <= rayon_emerge:
                beta = asin(rprim / rayon)
                zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
            return (xprim, yprim, zprim)
    

        x2, y2, z2 = deformation ((x, y, z), centre, rayon)#aller au centre 'déformé'
        turtle.goto(x2, y2)
        turtle.down()
        turtle.color (col[0])
        turtle.begin_fill()
        x += longueur
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)#aller au premier point du losange rouge
        turtle.goto(x2, y2)
        x = x - (cos(pi / 3) * longueur)
        y = y + (sin (pi / 3) * longueur)
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)#aller au deuxiéme point du losange déformé rouge
        x = x - longueur
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)# aller au dernier point rouge, commencer le losange noir
        turtle.end_fill() # fin du losange rouge
        turtle.color (col[1])
        turtle.begin_fill()
        x = x - (cos(pi / 3) * longueur)
        y = y - (sin (pi / 3) * longueur)
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)#aller au deuxiéme point du losange noir
        x = x + (cos(pi / 3) * longueur)
        y = y - (sin (pi / 3) * longueur)
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)#aller au troisiéme point du losange noir
        x2, y2, z2 = deformation ((point[0], point[1], point[2]), centre, rayon)#aller au centre 'déformé'
        turtle.goto(x2, y2)#retourner au centre, commencer le losange bleu
        turtle.end_fill()# fin du losange noir
        turtle.color (col[2])
        turtle.begin_fill()
        x = x + (cos(pi / 3) * longueur) + longueur
        y = y + (sin (pi / 3) * longueur)
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)#aller au deuxiéme point du losange bleu
        x = x - (cos(pi / 3) * longueur)
        y = y - (sin (pi / 3) * longueur)
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)#aller au troisiéme point du losange bleu
        x = x - longueur
        x2, y2, z2 = deformation ((x, y, z), centre, rayon)
        turtle.goto(x2, y2)# aller au dernier point du losange bleu
        x2, y2, z2 = deformation ((point[0], point[1], point[2]), centre, rayon)#aller au centre 'déformé'
        turtle.goto(x2, y2)#dernier retour au centre
        turtle.end_fill()# fin du losange bleu
        return

    absc = inf_gauche
    ordo = sup_droit
    arete = longueur
    i = 0
    while ordo >= inf_gauche:
        if int (i / 2) != i / 2:
            absc = inf_gauche - longueur - (cos (pi / 3) * longueur)
        else:
            absc = inf_gauche
        while absc <= sup_droit:
            hexagone ((absc, ordo, 0), arete, col, centre, rayon)
            absc += (3 * longueur)
        ordo += -(sin (pi / 3) * longueur)
        i += 1
    turtle.hideturtle()
    return


pavage(-200, 200, 15, ("yellow", "black", "grey"), (0, 0, 0), 150)
