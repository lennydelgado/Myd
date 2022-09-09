# Votre site

Avant toute chose, il vous faut votre site avant de pouvoir utiliser le projet.
Voyons comment le faire ensemble.

Commencez par créer un répertoire [GitHub](https://github.com/){.internal-link target=_blank}, pour ça, il faudra d'abord, vous crée un compte si ce n'est pas déjà fait.

Une fois, votre répertoire crée, vous allez devoir le cloner.
<BR>

<div class="termy">
```console
$ git clone git@github.com:votre-nom-utilisateur/nom-du-répertoire.git

<span style="color: green;">INFO</span>:     -  Clonage dans 'nom-du-répertoire'...
<span style="color: green;">INFO</span>:     -  Vous semblez avoir cloné un répo vide.
```
</div>
<BR>
Une fois que vous êtes dans votre répertoire vide vous allez créer la base de votre site à l'aide de la commande :
<BR>
<div class="termy">

```console
$ mkdocs new docs

<span style="color: green;">INFO</span>:     -   Creating project directory : docs
<span style="color: green;">INFO</span>:     -   Writing config file : docs\mkdocs.yml
<span style="color: green;">INFO</span>:     -   Writing initial docs : docs\docs\index.md
```

</div>

Si tout, c'est bien passé vous devriez vous retrouvez avec ceci :

```console
Votre répertoire
    └── docs
        ├── docs
        │   └── index.md
        └── mkdocs.yml
```

!!! info
    Il faut si vous souhaitez utiliser **Myd**, obligatoirement appeler son fichier crée par la commande ```mkdocs new "nom du fichier"``` que le fichiers soit nommée **docs**.

Maintenant, que vous avez la base de votre site web, je vous invite à regarder la documentation de [MkDocs](https://www.mkdocs.org/){.internal-link target=_blank} ainsi que des répertoires publique de documentation comme celle de [Typer](https://github.com/tiangolo/typer){.internal-link target=_blank} pour voir ce que vous pouvez faire. Faîte votre site web comme vous le désirez et une fois qu'il est prêt vous pouvez passer à [l'utilisation de Myd](how-to-use-myd-project.md).