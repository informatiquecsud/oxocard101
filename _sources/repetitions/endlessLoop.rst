

Boucles infinies
================

On aimerait programmer le serpent pour qu'il parte de la ligne tout en
bas de l'écran et se déplace de manière répétée de bas en haut et
vice-versa. On peut utiliser la commande ``setPos(x, y)`` pour placer le
serpent à la position ``(x, y)`` sans qu'il ne dessine. Avec la commande
``setSpeed(90)``, on peut augmenter la vitesse du serpent (vitesse
maximale = 100).

..  admonition:: Remarque
    :warning:

    Remarquez que le système de coordonnées est tourné vers le bas :
    l'origine se trouve en haut à gauche avec l'axe des x à orienté vers la
    droite et l'axe des y vers le bas.

    .. figure:: Untitled-a10b3324-3612-4113-b358-ab20f5a63d4a.png
    :alt: 

Puisque l'on n'indique pas le nombre de fois que la boucle doit être
répétée, Python va répéter le corps de la boucle à l'infini. On parle
dans ce cas de **boucle infinie**.

::

    from oxosnake import * 

    makeSnake()
    setPos(3, 7)
    setSpeed(90)

    repeat:
        forward(8)
        right(180)

Pour interrompre l'exécution du programme, il faut faire la combinaison
de touches Ctrl+C dans la fenêtre de terminal si le programme s'exécute
en mode réel sur l'Oxocard.

Alternative
~~~~~~~~~~~

Au lieu d'invoquer les commandes ``setPos(3, 7)`` et ``getSpeed(90)``,
il est également possible de fixer ces paramètres lors de l'appel de la
commande ``makeSnake()`` avec des paramètres particuliers :

::

    from oxosnake import * 

    makeSnake(speed=90, pos=(3, 7))

    repeat:
        forward(8)
        right(180)
