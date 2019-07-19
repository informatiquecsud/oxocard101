Commenter son code
==================

Python, comme tous les langages de programmation, permet de rajouter des
commentaires dans le code, à savoir du texte qui sera complètement
ignoré par Python mais que l'on écrit uniquement pour nous-mêmes et les
personnes qui liront nos programmes. Il y a essentiellement deux types
de commentaires : ceux qui se limitent à une seule ligne et ceux qui
s'étendent sur plusieurs lignes.

::

    # ceci est un commentaire d'une seule ligne
    display.show("blabla")   # la fin de cette ligne après le '#' sera également ignorée

    '''

    Ceci est un commentaire qui 
    s'étend sur plusieurs lignes. On utilise généralement
    ce genre de commentaires pour écrire beaucoup de texte et documenter
    une grande partie du programme

    '''

-  Sur une ligne donnée, tout ce qui vient après un ``#`` est ignoré par
   Python
-  Le début et la fin des commentaires sur plusieurs lignes est marqué
   par trois guillemets simples ``'''``. Tout ce qui se trouve entre
   deux (en vert dans le code ci-dessus) est ignoré par Python, ce qui
   vous permet d'ajouter du texte qui vous permettra de mieux comprendre
   votre programme lorsque vous l'aurez laissé de côté pendant
   longtemps.

..  admonition:: Remarque
    :class: info

    Dans ce tutoriel, nous utiliserons parfois les commentaires dans le code
    pour donner des explications directement dans le code. Il faut donc bien
    lire les commentaires présents dans les programmes exemples.