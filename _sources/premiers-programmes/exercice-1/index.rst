..  _first-programs-exercice-1:

Exercice 1
----------

..  tabbed:: first-programs-exercise-1a

    ..  tab:: Donnée

        Écrire un programme qui commande au serpent de se déplacer sur un
        carré de côté 4.

        ..  figure:: Untitled-8351dc62-f890-44e7-843b-2d514184c166.png
            :alt:

        ..  activecode:: ac-first-programs-exercise-1a
            :language: python
            :enabledownload:
            :nocodelens:

            Coller votre code solution ici lorsqu'il tourne dans TigerJython et
            cliquer sur le bouton "Run" pour que votre code. Remarque : pour le
            moment, cela donne une erreur dont il ne faut pas tenir compte.
            
            ~~~~
            from oxosnake import *

            makeSnake()

            # compléter votre code ci-desous

    ..  tab:: Solution

        ..  code-block:: python
            :linenos:

            from oxosnake import * 

            makeSnake()

            forward(3)
            right(90)

            forward(3)
            right(90)

            forward(3)
            right(90)

            forward(3)
            right(90)


        ..  admonition:: Attention
            :class: attention

            Vous noterez que pour dessiner un carré de côté 4, il faut indiquer
            ``3`` en paramètre à la commande ``forward()``


        ..  admonition:: Remarque
            :class: note

            On remarque que ce code est assez répétitif et que l'on va utiliser
            4 fois de suie la séquence de code 

            ::

                forward(3)
                right(90)


            On verra dans un prochain chapitre comment 
            
..  tabbed:: first-programs-exercise-1b

    ..  tab:: Donnée

        Écrire un programme qui commande au serpent de se déplacer sur un
        carré de côté 5.

        ..  activecode:: ac-first-programs-exercise-1b
            :language: python
            :enabledownload:
            :nocodelens:

            Coller votre code solution ici lorsqu'il tourne dans TigerJython et
            cliquer sur le bouton "Run" pour que votre code. Remarque : pour le
            moment, cela donne une erreur dont il ne faut pas tenir compte.
            
            ~~~~


    ..  tab:: Solution

        ..  code-block:: python
            :linenos:

            from oxosnake import * 

            makeSnake()

            forward(4)
            right(90)
            forward(4)
            right(90)
            forward(4)
            right(90)
            forward(4)
            right(90)

        ..  admonition:: Remarque
            :class: note

            On constate que ce code est pratiquement le même que dans la partie
            précédente. On modifie juste la distance sur laquelle le serpent
            avance tout droit de ``4`` à ``5``. 

            ::

                forward(3) => forward(4)
                

            On verra dans un prochain chapitre comment utiliser les commandes
            avec paramètres pour éviter de devoir recopier ainsi du code qui est
            pratiquement identique à quelques grandeur près.

..  tabbed:: first-programs-exercise-1c

    ..  tab:: Donnée

        Écrire un programme qui commande au serpent de se déplacer sur un
        carré de côté 6.


        ..  activecode:: ac-first-programs-exercise-1c
            :language: python
            :nocodelens:

            Coller votre code solution ici lorsqu'il tourne dans TigerJython et
            cliquer sur le bouton "Run" pour que votre code. Remarque : pour le
            moment, cela donne une erreur dont il ne faut pas tenir compte.

            ~~~~


    ..  tab:: Solution

        ..  code-block:: python
            :linenos:

            from oxosnake import * 

            makeSnake()

            forward(5)
            right(90)
            forward(5)
            right(90)
            forward(5)
            right(90)
            forward(5)
            right(90)

        ..  admonition:: Remarque
            :class: note

            Décidémment, cet exercice n'était pas compliqué mais surtout
            rébarbatif. Nous allons voir dans la suite des outils qu'offrent
            les langages de programmation pour éviter de duppliquer ainsi du
            inutilement. 
                
