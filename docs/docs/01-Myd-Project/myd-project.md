# **Myd-project**

## Présentation du projet Myd

### But du projet

Le projet consiste à automatiser la contenairisation d'un site web crée à l'aide de [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank}.

!!! info
    [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} est un outil de documentation open-source permettant très simplement de documenter rapidement un projet. Il est basée sur le language [Python](https://www.python.org/){.internal-link target=_blank}.

### Mes outils

Durant le projet, j'ai utilisé plusieurs outils afin de mener à bien le projet, comme par exemple [Docker](https://www.docker.com/){.internal-link target=_blank} qui constitue le cœur de mon projet. J'ai utilisé notamment [Harbour](https://goharbor.io/){.internal-link target=_blank} qui est un service permettant de stocker dans le cloud des [images Docker](https://www.techtarget.com/searchitoperations/definition/Docker-image){.internal-link target=_blank}, à la manière du [Docker Hub](https://hub.docker.com/){.internal-link target=_blank}.

Pour ce qui est du site web, j'ai utilisé [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} qui est un générateur de [site web statique](https://fr.wikipedia.org/wiki/Page_web_statique) destiné à créer une plateforme de documentation. Le site une fois généré, a pu être déployé grâce à [Nginx](https://www.nginx.com/){.internal-link target=_blank} qui est un logiciel libre de serveur Web.

!!! check "Liste des outils"
    * [Docker](https://www.docker.com/){.internal-link target=_blank}
    * [Harbour](https://goharbor.io/){.internal-link target=_blank}
    * [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank}
    * [Nginx](https://www.nginx.com/){.internal-link target=_blank}

## Etapes du projet

### Image Python

Tout d'abord, j'ai dû créer mon tout premier fichier [Docker](https://www.docker.com/){.internal-link target=_blank} avec une image [Debian](https://www.debian.org/index.fr.html){.internal-link target=_blank} (j'ai utilisé l'image **debian-bulleye-slim** pour avoir un container léger). Par la suite, j'ai légèrement configuré ce dernier pour le rendre prêt pour la prochaine étape.

!!! note
    Inutile de préciser, mais chacun des container générer ont tous été publier sur [Harbour](https://goharbor.io/){.internal-link target=_blank} en privé pour avoir un accès facile et pour pouvoir les utiliser commes des images.

Ensuite, j'ai ajouté dans mon container [Debian](https://www.debian.org/index.fr.html){.internal-link target=_blank}, le langage obligatoire pour l'installation de [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} qui est [Python](https://www.python.org/){.internal-link target=_blank}. Toute cette étape m'a généré une image python prête à l'emploi pour la prochaine étape.

### Image Nginx

Enfin, j'ai dû utiliser cette fois ma propre image [Python](https://www.python.org/){.internal-link target=_blank}, j'ai par la suite récupéré depuis mon répertoire [Github](https://github.com/){.internal-link target=_blank}, mes fichiers [Markdown](https://fr.wikipedia.org/wiki/Markdown){.internal-link target=_blank} nécessaires à la génération de ma page web.

Après avoir installé [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} et toutes les dépendances nécessaires, j'ai ensuite généré les pages pour [Nginx](https://www.nginx.com/){.internal-link target=_blank} afin qu'il puisse me le traduire en page web et non en [Markdown](https://fr.wikipedia.org/wiki/Markdown){.internal-link target=_blank} ([MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} génère des pages [HTML](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language){.internal-link target=_blank} à partir de fichier [Markdown](https://fr.wikipedia.org/wiki/Markdown){.internal-link target=_blank}).

Grâce aux connaissances que j'ai acquises sur [Docker](https://www.docker.com/){.internal-link target=_blank}, j'ai réussi dans le même fichier de configuration à récupérer cette fois-ci l'image [Nginx](https://www.nginx.com/){.internal-link target=_blank} (**nginx:1.23.0-alpine**, image très légère également) ce qui m'a permis par la suite à simplement avoir dans ma dernière image seulement [Nginx](https://www.nginx.com/){.internal-link target=_blank} et [Alpine](https://fr.wikipedia.org/wiki/Alpine_Linux){.internal-link target=_blank} ([Python](https://www.python.org/){.internal-link target=_blank} étais nécessaire uniquement pour la génération des pages web et non le fonctionnement).

### Bilan

Toutes ces étapes ont été éffectué par ce qu'on appelle des **Docker files** (des fichiers de configurations de container [Docker](https://www.docker.com/){.internal-link target=_blank}) et des scripts [Shell](https://fr.wikipedia.org/wiki/Shell_Unix){.internal-link target=_blank} pour le lancement, permettant une automatisation de tout les procéssus décrit au dessus.

On se retrouve avec une image final qui est légère et dans laquelle n'est présents que ce dont on a besoins.

!!! info
    Le projet consisté principalement à essayer de reproduire le modèle déjà en place ce qui a permit à mon tuteur de savoir comment je me débrouillais. J'ai du faire en parti sans modèles, la partie [Nginx](https://www.nginx.com/){.internal-link target=_blank}. Ce projet était centré sur le [DevOps](https://fr.wikipedia.org/wiki/Devops){.internal-link target=_blank}. J'ai réussi à généraliser au maximum ce qui permet à n'importe qui voudrais de l'installer.

## Difficultés rencontrées

Durant le projet, j'ai eu pas mal de difficultés en ce qui concernait [Docker](https://www.docker.com/){.internal-link target=_blank} et ma méconnaissance des fonctionnement de [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} ou encore [Nginx](https://www.nginx.com/){.internal-link target=_blank}.

La partie principale étant [Docker](https://www.docker.com/){.internal-link target=_blank}, j'ai eu des difficultés parce que je ne l'avais presque jamais utilisé. Mais c'est aller très vite mieux, le langage est visuels et tout ce qui touche [Docker](https://www.docker.com/){.internal-link target=_blank} est très bien documenté.

!!! warning "*Liste des difficultées*"
    * La prise en main de [Docker](https://www.docker.com/){.internal-link target=_blank}
    * L'installation de la surcouche [Nginx](https://www.nginx.com/){.internal-link target=_blank} notamment la configuration

## Les comptétences acquises

J'ai réussi à vraiment à gagner en aisance avec [Docker](https://www.docker.com/){.internal-link target=_blank}, il m'a fallu du temps certes [Docker](https://www.docker.com/){.internal-link target=_blank} est un outil très puissant et intéressant à manipuler.

Je me suis aussi entraîné à documenter par exemple en écrivant des phrases dans le *code*, afin d'être le plus clair possible dans le fonctionnement du projet.

J'ai compris le réel fonctionnement et utilités de [Docker](https://www.docker.com/){.internal-link target=_blank}, mon seul projet que j'ai fait à l'école me laisser encore quelques zones d'ombres.

## Mon retour sur le projet

J'ai réussi à vraiment à gagner en aisance avec [Docker](https://www.docker.com/){.internal-link target=_blank}, il m'a fallu du temps certes [Docker](https://www.docker.com/){.internal-link target=_blank} est un outil très puissant et intéressant à manipuler.

!!! tip "*Mot de la fin*"
    Le projet, je l'ai beaucoup aimé, durant ma première année, je n'ai pas pu vraiment découvrir plein de chose différentes, donc c'est enrichissant de découvrir autre chose que le développement pure.