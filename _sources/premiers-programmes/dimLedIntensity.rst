Diminuer la luminosité des LEDs
===============================

Peut-être que les LEDs brillent trop fort. On peut dans ce cas atténuer
leur intensité en fournissant un paramètre ``dim`` lors de l'appel de la
commande ``makeSnake``. Essayez de modifier le programme en remplaçant
la ligne appropriée par

::

    makeSnake(dim=20)

Cela a pour effet de diminuer d'un facteur 20 l'intensité lumineuse des
LEDs.

..  reveal:: reveal-dim-led-intensity-solution
    :showtitle: Afficher la solution
    :hidetitle: Cacher la solution

    ..  code-block:: python
        :emphasize-lines: 3

        from oxosnake import * 

        makeSnake(dim=20)

        forward()
        forward()
        right(90)
        forward(2)
