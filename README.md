HTR-United
=========

## Qu'est-ce que HTR-United

HTR-United est une organisation github sans autre forme de personnalité juridique. Elle vise à **mettre en commun les transcriptions HTR/OCR de textes français du 18 au 21e siècle**. Elle est née du simple besoin - pour des projets - d'avoir de potentiels vérités de terrain pour entraîner des modèles rapidement sur des corpus plus petits.

## Que des données ?

À terme, l'objectif de cette organisation sera probablement de partager aussi - sous licence libre - des modèles pour les moteurs HTR demandés, afin que les projets les moins dotés puissent profiter de modèles. Ainsi, si vous partagez vos données, et suivant le rythme possible des autres partenaires, vous profiterez sûrement d'un modèle sous peu.

Cependant, n'oubliez pas: il existe un cercle vertueux Transcription<->Entraînement qui permettra à terme - nous l'espérons - d'améliorer pour les plus jeunes projets les transcriptions partant de 0.

## Comment cela fonctionne ?

Il existe deux cas de figure:

1. [Vous avez déjà un dépôt de données](#vous-avez-déjà-un-dépôt-de-données)  
2. [Vous n'en avez pas et préférez fournir directement l'organisation](#vous-nen-avez-pas)
    
### Vous avez déjà un dépôt de données

C'est plutôt pratique: vous gardez la main, pas de problèmes de rajout à l'organisation. Mais, histoire de faire grossir la visibilité de votre set de données, il nous parait important de le décrire ici ! En effet, si vous profitez des données de HTR-United, voire de ses modèles, autant renvoyer la pareille. 

Pour ce faire, il suffit d'[ouvrir une issue](https://github.com/HTR-United/htr-united/issues/new) ou de proposer une modification sur le répertoire de dépôt en rajoutant une ligne formatée telle que:

```yaml
        name: "Titre"
        url: 'Lien vers le dépôt'
        description: 'Description'
        language: French
        other-languages:
            - "Optionel"
        time: 1800--1897
        hands: 5  # Nombre de mains
        license:
            - {name: 'CC-BY 4.0', url: 'https://creativecommons.org/licenses/by/4.0/'} # Vous pouvez bien sûr changer la licence
        format: Alto-XML
        volume:
            - {count: "NOMBRE DE LIGNES", metric: lines} # ou
            - {count: "NOMBRE DE PAGES", metric: pages} # ou
```

### Vous n'en avez pas

Et bien, nous serons heureux de vous aidez. [Ouvrez un ticket ici](LIEN VERS ISSUES AVEC TEMPLATE AJOUT D'UN DÉPÔT) et nous serons heureux de vous aider à créer et partager votre dépôt, sur HTR-United. Des compétences en `git` sont bienvenues mais, si vous voulez partager des données, on vous aidera, c'est le but de cette organisation !
