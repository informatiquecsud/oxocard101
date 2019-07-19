Exercices
=========

Exercice 1
----------

Effectuez un copier-coller du code suivant dans l'éditeur TigerJython et
exécutez-le en mode simulation dans TigerJython. **Exceptionnellement,
vous ne devez pas chercher à comprendre ce code qui implique beaucoup de
notions que nous allons aborder très gentiment dans ce cours.**

..  admonition:: Remarque
    :class: tip

    Il est normal que l'exécution de ce code directement dans le navigateur
    produise une erreur car le module ``oxocard`` qui est importé n'est pas
    disponible dans le navigateur pour le moment.


..  activecode:: ac-mise-en-route-ex-1
    :language: python
    :caption: Code Python à copier/coller dans TigerJython et exécuter sur l'Oxocard
    :enabledownload:
    :nocodelens:

    from oxocard import *
    from random import randint

    enableRepaint(False)
    while True:
        for i in range(8):
            for k in range(8):
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                dot(i, k, (r, g, b))

        repaint()
        sleep(0.001 * randint(10, 100))


..  mchoice:: mc-mise-en-route-ex-1

    Cocher ce qui convient

    ..

    -   J'ai réussi à exécuter le code avec succès en mode Simulation dans TigerJython

        +   Super! Essayez de l'exécuter sur votre Oxocard dans l'exercice
            suivant !

    -   Je n'ai pas réussi à exécuter le code en mode simulation 

        -   Il ne faut pas abandonner. L'enseignant va voir dans son tableau de
            contrôle que vous n'avez pas réussi à exécuter le code. Essayez d'abord
            de relire la section :ref:`programming-oxocard-in-python`. Si vous
            n'arrivez toujours pas à exécuter votre programme, commencez par trouver
            quelqu'un qui a réussi à le faire et, en dernier recours, demandez à
            votre enseignant de venir vous dépanner.

            Assurez-vous que vous avez bien effectué le copier/coller dans
            l'éditeur TigerJython sans faire de faute. Il faut notamment que les
            indentations du code soient conservées (décalage par rapport à la
            marge de gauche).


Exercice 2
----------

Exécutez le code de l'exercice précédent sur l'Oxocard et, si vous êtes
en classe, levez la main en montrant votre Oxocard.

..  admonition:: Avertissement
    :class: warning

    Attention à ne pas regarder trop longtemps l'écran car les LEDs sont
    vraiment très brillantes si l'Oxocard n'est pas emballée dans son
    carton protecteur.

    Il est possible de recouvrir les LEDS avc une feuille de papier pour
    que l'intensité convienne mieux. 

..  mchoice:: mc-mise-en-route-ex-2

    Cocher ce qui convient

    ..

    -   J'ai réussi à exécuter le code avec succès sur l'Oxocard

        +   Super! Levez-vous dans la classe et montrez l'écran de votre Oxocard.

    -   Je n'ai pas réussi à exécuter le code sur l'Oxocard

        -   Il ne faut pas abandonner. L'enseignant va voir dans son tableau de
            contrôle que vous n'avez pas réussi à exécuter le code. Essayez d'abord
            de relire la section :ref:`programming-oxocard-in-python`. Si vous
            n'arrivez toujours pas à exécuter votre programme, commencez par trouver
            quelqu'un qui a réussi à le faire et, en dernier recours, demandez à
            votre enseignant de venir vous dépanner.