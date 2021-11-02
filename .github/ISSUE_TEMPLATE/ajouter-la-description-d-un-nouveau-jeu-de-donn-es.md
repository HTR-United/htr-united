---
name: Ajouter la description d'un nouveau jeu de données
about: Template pour ajouter la description d'un nouveau dataset
title: "[catalog] Nouveau repo {project-name/dataset-name}"
labels: project
assignees: ''

---

## Description du jeu de données

### Checklist
- [ ] le nom du corpus est exprimé explicitement
- [ ] le nom du projet est exprimé explicitement
- [ ] les auteur-rices et les rôles sont exprimés explicitement
- [ ] une license est associée au jeu de données
- [ ] le jeu de données est clairement et explicitement décrit, de manière à permettre aux autres utilisateurs de comprendre son contenu et le contexte de sa création
- [ ] le jeu de données utilise des formats standards comme PAGE XML ou ALTO XML et les transcriptions sont alignées avec des images

### Informations inmportantes

- nom du corpus<sup>[1](#fn1)</sup>: 
- nom du projet<sup>[2](#fn2)</sup>:
- description générée à l'aide de [notre formulaire](https://htr-united.github.io/document-your-data.html):
```
[Copier la description ici]
```

### Autonomie

Cocher la situation applicable :

- [ ] Je sais comment faire une Pull Request et je m'occupe de créer un dossier + fichier correspondant à mon dépôt dans "[htr-united/catalog/](https://github.com/HTR-United/htr-united/tree/master/catalog)"
- [ ] Je ne sais pas comment faire une Pull Request, j'ai besoin d'aide pour ajouter une description de mon jeu de données sous "[htr-united/catalog/](https://github.com/HTR-United/htr-united/tree/master/catalog)"

---

<a name="fn1">1</a>: Ce nom sera utilisé pour créer le fichier YAML dédié au jeu de données. *Par exemple : si votre jeu de données s'appelle "Mon Super Dataset", sa description sera enregistrée sous "mon-super-dataset.yml"*

<a name="fn2">2</a>: Ce nom sera utlisé pour créer un dossier dans "catalog/", il contiendra toutes les descriptions des jeux de données liés à ce projet. *Par exemple : si vous projet s'appelle "Mon Super Projet", le(s) fichier(s) YAML sera(ont) enregistrés sous "catalog/mon-super-projet/"*
