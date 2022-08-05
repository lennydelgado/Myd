# Installation

## Prérequis

Ce projet a été entièrement réalisé dans un environnement Linux Debian et il devrait être compatible avec tous les systèmes supportant Linux.

Tout d'abord, vous aurez besoin de [Docker](https://www.docker.com/){.internal-link target=_blank} pour plus d'informations concernant son installation allez voir la documentation [ici](https://docs.docker.com/engine/install/){.internal-link target=_blank}.

Vous aurez également de [Python](https://www.python.org/){.internal-link target=_blank}, vous pouvez l'installer en cliquant [ici](https://www.python.org/downloads/){.internal-link target=_blank}. Il vous faudra également [Pip](https://pypi.org/project/pip/){.internal-link target=_blank}, pour suivre les instructions d'installation, je vous redirige [ici](https://pip.pypa.io/en/stable/installation/){.internal-link target=_blank}.

Enfin, vous aurez aussi besoin de [Visual Studio Code](https://code.visualstudio.com/){.internal-link target=_blank}. Il vous permettra de faire de la [redirection de port](https://fr.wikipedia.org/wiki/Redirection_de_port){.internal-link target=_blank}, de manière simple.

## Mise en place environnement virtuel Python

Nous allons voir ensemble comment mettre en place l'environnement virtuel [Python](https://www.python.org/){.internal-link target=_blank} qui nous servira à installer toutes les librairies nécessaires au bon fonctionnement du projet.

Tapons la commande suivante : 

<div class="termy">
```console
$ python -m venv env-myd
```
</div>

Cette commande à pour effet de vous crée le dossier dans lequel ce trouveras toutes les futures librairies que nous installerons mais d'abord il faut l’activer, pour cela taper la commande suivante :

<div class="termy">
```console
$ source aboslute-path-to-project/env-myd/bin/activate
```
</div>

Si tout s’est bien passé normalement votre terminal devrais afficher ceci :

<div class="termy">
```console
$ (env-myd)
<span style="color: green;">INFO</span>:     -  Ici la parenthèse nous montre que l'environnement actif est "env-myd"
```
</div>

Vous pouvez à présent changer l’interpréteur [Python](https://www.python.org/){.internal-link target=_blank} sur **Visual studio code**.

Pour cela ouvrez **Visual studio code**, appuyez sur ```Ctrl + Shift + P``` puis tapez dans la barre de recherche *interpréteur*, ensuite ajoutez un nouveau chemin pour l'interpréteur et entrez le chemin absolu du dossier de l'environnement virtuel.

## Récupération du projet

Nous vous donnons ci-dessous la commande à effectuer pour cloner le répertoire [GitHub](https://github.com/lennydelgado/Myd-project){.internal-link target=_blank}, pour cela taper la commande suivante :
<div class="termy">
```console
$ git clone git@github.com:lennydelgado/Myd.git

<span style="color: green;">INFO</span>:     -  Clonage dans 'Myd'...
<span style="color: green;">INFO</span>:     -  Réception d'objets: 100% (17/17), 7.77 Mio/s, fait.
<span style="color: green;">INFO</span>:     -  Résolution des deltas: 100% (2/2), fait.
```
</div>


Vous devriez maintenant vous retrouver avec ceci :

```console
Myd-project/
│
├── debian_myd/
│   ├── build-debian.sh
│   └── debian_myd.dockerfile
│
├── python_myd/
│   ├── build-python.sh
│   └── python3.10.4.dockerfile
│
├── nginx/
│   ├── build-myd-docs.sh
│   ├── myd-docs.dockerfile
│   └── run-nginx.sh
|
├── conf/
|   └── exemple.conf
|
├── logs/
|
├── requirement.txt
|
└── myd.py
```

## Installation des dépendances

Maintenant que vous avez installé et activez l'environnement virtuel et récupérer le projet vous pouvez installer toutes les librairies nécessaires au fonctionnement du projet sans aucune crainte, il vous suffit d'entrer la commande suivante :
<div class="termy">
```console
$ (env-myd) pip install -r requirement.txt

<span style="color: green;">INFO</span>:     -  Installation des dépendances
```
</div>

Maintenant que l’installation est terminée je vous invite à [crée votre premier site avec MkDocs](create-mkdocs-website.md) et à le publier sur un de vos répertoire GitHub, si c’est déjà le cas vous pouvez directement passée à [l’utilisation du projet](how-to-use-myd-project.md).
