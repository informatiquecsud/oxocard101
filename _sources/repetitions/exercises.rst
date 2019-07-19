

Exercices
=========


..  toctree::
    :caption: Exercices du chapitre
    :maxdepth: 1
    :glob:

    exercice-*/index

::

    # regexp to replace : `(Exercice \d+)\s+<\./((Exercice-\d+)-.+\.md).+
    # replace by : pandoc -t rst mdfiles/$2 | python3 scripts/copy_assets.py $3

