# Mise en place

## L'éditeur de code

La première chose à installer est un éditeur de texte afin de pouvoir programmer. En soit, il serait possible de programmer avec n'importe lequel, y compris Bloc-notes sur Windows. Cependant il existe de nombreux éditeurs avancés permettant l'accès à beaucoup de fonctionnalités liées à la programmation.

Ici nous allons installer **Visual Studio Code** qui est un des éditeurs les plus utilisés et qui permet de développer facilement sous n'importe quel langage de programmation.

Télécharger VSCode:

```txt
https://code.visualstudio.com/
```

Un fois installé, nous allons pouvoir installer les plugins nécessaires au développement python.

![image](./assets/02/vscode_plugins.png)

Pour chacune des extensions suivantes, le télécharger et les installer:

- **Python**: Gère le code python sous VSCode.
- **isort**: Trie automatiquement les imports de librairies dans un fichier de code.
- **Black Formatter**: Formate les fichiers de code.
- **Pylint**: Surligne les erreurs ou les pratiques déconseillées.

Quelques raccourcis utiles pour plus tard:

- `shift + alt + f` Formate le fichier actuel avec Black Formatter.
- `shift + alt + o` Trie les imports de librairies avec isort.
- `ctrl + :` Commente les lignes de code sélectionnées.

## Anaconda

Nous allons maintenant passer aux environnements virtuels. En programmant en python (mais pas forcément pour les autres langages) il est souvent nécessaire d'utiliser des environnements virtuels.

### Les bibliothèques

En informatique, lorsque que l'on écrit un programme, il est très courant d'utiliser des bibliothèques. Les bibliothèques sont du code téléchargeable sur internet pouvant être utilisé par d'autres développeurs.

Par exemple, si je veux programmer un algorithme de machine learning assez complexe, il est probable qu'une librairie existe avec une implémentation de cet algorithme. Au lieu de tout recoder, je peux installer cette librairie et avec accès aux différents algorithmes déjà développés. Cela permet de gagner du temps et d'utiliser des implémentations de code souvent robustes et efficaces.

![image](./assets/02/lib_import.png)

### Les environnements virtuels

Dans tous langages, la gestion des bibliothèques peut être une tâche ardue. En effet, la majeure partie des bibliothèques ont des dépendances (dépendent d'autres bibliothèques). Cela peut engendrer des conflits de compatibilité entre bibliothèques.

```txt
Une bibliothèque A dépend d'une bibliothèque C en version 1.0.0.
Une bibliothèque B dépend d'une bibliothèque C en version 1.1.0.

Si j'installe A et B, un conflit apparaît car une seule version d'une dépendance est autorisée dans l'environnement d'un projet.
```

De plus, si une bibliothèque est directement installée à une version spécifique sur l'ordinateur, il faudra la désinstaller plus tard si un nouveau projet requiert une version différente.

![image](./assets/02/v_env.webp)

Pour pallier ces problèmes on utilise des environnements virtuels. La création d'un environnement virtuel permet de:

- Créer un environnement contenant les bibliothèques souhaitées pour un projet spécifique.
- Gérer les possibles conflits entre bibliothèques.

Donc pour chaque projet, on peut créer un environnement virtuel dédié avec les librairies seulement nécessaires à ce projet.

### Installation de Conda

Télécharger miniconda:

```txt
https://www.anaconda.com/download/success
```

Durant l'installation, cocher les 2 cases marquées comme recommandé.
