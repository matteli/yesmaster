Yes Master
==========

Incipit
-------

```Je lui donnai les explications les plus claires possibles sur les nombreuses combinaisons, quatre couleurs différentes, une couleur doublée ou triplée, les pions blancs et rouges. 
Elle écoutait attentivement, questionnait sans cesse et se pénétrait de mes réponses.
— Et est-il possible de trouver la bonne combinaison du premier coup ? Rose a crié tout à l’heure :« En un coup », et a levé les bras. Qu’est-ce que ça signifie ?
— En un coup, Margaux, c'est exceptionnel; Cela n'arrive presque jamais.
— En combien de coups alors ?
— En général, si on joue bien, on y arrive en 6 coups.
— Et cela arrive souvent ? Pourquoi y-a-t'il 9 lignes ? C'est pour les imbéciles ?
— Parce que l'on peut manquer de chance et mettre un peu plus de coups pour réussir.
— Quelle bêtise ! Là, est-ce que j'ai réussi du premier coup ?
— Margaux, le un coup vient d'être fait; c’est un mauvais moment pour penser réussir en un coup. Un blanc.
— Qu’est-ce que tu racontes! Et là ?
— Au deuxième coup, c'est rare aussi. Un blanc, un rouge.
— Des bêtises! Quand on craint le loup on ne va pas au bois. C’est perdu ? 
Margaux ne tenait pas en place. Elle semblait vouloir fasciner les petits pions. Le troisième coup donna deux blancs, un rouge. Margaux était hors d'elle. Elle donna un coup de poing sur la table quand j'indiquai encore deux blancs et un rouge.
— Canaille! s’écria-t-elle. Ce maudit 4 rouges ne veut donc pas sortir ? Je veux rester jusqu’à ce qu’il sorte! C’est toi scélérat qui l'empêche de sortir!... Et là ?
— 4 rouges !
— Tu vois! Tu vois! dit vivement Margaux toute rayonnante. C’est Dieu lui-même qui m’a donné l’idée de mettre cette combinaison...
```

Intuition
---------
Ces derniers jours, j'ai recommencé à jouer à Mastermind avec mes filles.
Pour rappel ou pour ceux qui ne connaîtrait pas ce classique, il faut découvrir un code de 4 couleurs parmi 8 (on peut mettre plusieurs fois une couleur). A chaque tentative, il est indiqué le nombre de pions de la bonne couleur bien placé (avec un indicateur rouge ou noir suivant les versions) et le nombre de pions de la bonne couleur mal placé (avec un indicateur blanc).
Dans nos parties, on trouve le code en 6 coups. Parfois 5 quand on a de la chance, parfois 7 quand on en manque.
Au début, après un premier coup au hasard avec 4 couleurs différentes, on ne faisait que des coups compatibles avec les indications. Ensuite, intuitivement, on s'est mis à faire un deuxième coup avec les 4 couleurs que l'on avait pas encore mis au premier coup quite à ce que ce coup ne soit pas compatible avec le premier. Je me suis demandé quelle était la meilleure stratégie et surtout si nos 6 coups étaient dans la moyenne.

Code
-------
J'ai donc sorti mon éditeur de code favori et utilisé le langage le plus élégant au monde pour écrire un petit programme qui me permettrait de vérifier tout ça. Tout d'abord les bases, un petit [programme](https://github.com/matteli/yesmaster/blob/master/yesmaster/yesmaster.py) qui me permettait de jouer seul. Programme trivial, il a fallu juste que je trouve un moyen de vérifier la combinaison et de déterminer les blancs et rouges.
Pour les rouges, c'est trivial, pour les blancs un petit peu moins. La méthode qui m'est venu a été de compter dans les deux codes (celui à trouver et celui de la tentative) le nombre de fois que chaque couleur était jouée. Pour chaque couleur, je prends la valeur minimale. J'additionne toutes ces valeurs minimales, ce qui me donne le nombre total de bonnes couleurs (bien ou mal placé). Je n'ai plus qu'à soustraire à ce total, le nombre de rouges et j'obtiens le nombre de blancs. [Voir def verify](https://github.com/matteli/yesmaster/blob/master/yesmaster/utils.py)

Bien mais ce n'était pas l'objectif. J'ai mis en place la partie auto avec un premier algo qui tire au hasard des combinaisons jusqu'à ce qu'il trouve la bonne solution (il est tellement crétin qu'il peut tirer plusieurs fois la même combinaison). Résultat après quelques milliers de parties, le nombre de coups moyens converge gentiment vers 4000-4100 coups (ce qui correspond bien à 8^4 = 4096, arrangement de 4 couleurs parmi 8 avec remise). Ça permet de vérifier la loi des grands nombres qui est bien souvent faussement invoqué pour jouer à Mme Irma.

[Deuxième algo](https://github.com/matteli/yesmaster/blob/master/yesmaster/algo/random_no_repeat.py), le même mais cette fois-ci il ne tire plus deux fois la même combinaison. Résultat : on semble converger cette fois-ci vers 2048 coups. Je suis bien incapable de le prouver. Afin d'améliorer les performances, j'ai dû stocker les combinaisons déjà faites sous forme d'arbre. [Voir def make_tree](https://github.com/matteli/yesmaster/blob/master/yesmaster/utils.py)

Bon, on passe maintenant à des algos un peu plus intéressant. Le [troisième algo](https://github.com/matteli/yesmaster/blob/master/yesmaster/algo/compatible.py) joue un coup au hasard en premier puis des coups compatibles (coups qui ne sont pas incompatibles au vu des résultats des tentatives précédentes).

Puis, un [quatrième algo](https://github.com/matteli/yesmaster/blob/master/yesmaster/algo/compatible_8in2.py) implémente notre intuition : sur les deux premiers coups, on joue les 8 couleurs puis des coups compatibles.

Enfin, un [cinquième algo](https://github.com/matteli/yesmaster/blob/master/yesmaster/algo/compatible_4in1.py) ressemble beaucoup au troisième en obligeant le premier coup à jouer avec 4 couleurs différentes puis des coups compatibles.

Résultats
-------------
Je ne reviens pas sur les deux premiers algo.

Le 3ème donne, après 10000 parties:
- 5,42 coups en moyenne
- 9 coups maximum

Le 4ème donne, après 10000 parties:
- 5,52 coups en moyenne
- 9 coups maximum

Le 5ème donne, après 10000 parties:
- 5,40 coups en moyenne
- 9 coups maximum

Avec nos 6 coups, on est dans la moyenne. De façon étonnante, on a jamais été au-delà de 7 coups alors que l'algo "compatible" monte à 9. Enfin notre intuition n'est pas bonne même si elle permet d'avoir des infos faciles à intégrer au début du jeu. Enfin, il vaut mieux jouer 4 couleurs différentes en premier.

Je me pose quand même la question de savoir si 10000 parties suffisent pour bien converger sur la deuxième décimale. D'après mes tests, c'est un peu juste.

Épilogue
--------
Chères lectrices, chers lecteurs, pour aller plus loin je te propose deux défis :
- Sauras-tu retrouver l'oeuvre originale, tombée dans le domaine public, dont est très largement inspiré l'incipit ?
- Sauras-tu trouver un algorithme qui permettra de descendre sous les 5,4 coups de moyenne (avec 10000 parties) tout en maintenant les parties à 9 coups maximum ? Voir le [README.md](https://github.com/matteli/yesmaster/blob/master/README.md) pour qu'il s'intègre harmonieusement avec le reste du code.