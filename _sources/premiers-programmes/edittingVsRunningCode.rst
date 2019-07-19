

Édition et exécution du code
============================

Il faut distinguer l'édition du code du programme et son exécution.
L'édition se fait sur l'ordinateur dans l'environnement TigerJython. Le
code est ensuite téléchargé sur l'Oxocard et exécuté sur la carte
elle-même par le firmware MicroPython. Lorsqu'une erreur se produit dans
la fenêtre de terminal, c'est que l'ordinateur est en communication en
temps réel par une liaison série avec l'Oxocard.

La commande ``makeSnake()`` engendre un objet de la classe ``Snake`` sur
lequel on peut agir à l'aide des commandes issues du module
``oxosnake``.