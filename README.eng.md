HTR-United
=========

## What is HTR-United
HTR-United is a Github organization without any other form of legal personality. It aims at **gathering HTR/OCR transcriptions of all periods and style of writing, mostly but not exclusively in French**. It was born from the mere necessity -for projects- to possess potentiel ground truth to rapidly train models on smaller corpora.

## Only data?

Eventually, this organization will also aim at sharing -under free licenses- models suited for requested HTR processors. This will make it possible for projects with smaller capacities to benefit from ready-to-use models. Thus, if you share your data, and according to the rythm followed by the other members, you will soon be able to use such models.

However, keep in mind there exists a virtuous circle Transcription<->Training which will eventually, we hope, considerably improve the transcriptions created by young projects starting from scratch.

## How does it work?
There are two cases:
1. [You already have data in a repository](#you-already-have-data-in-a-repository)
2. [You don't have one and prefer to help the organization directly](#you-dont-have-one)
    
### You already have data in a repository
It's rather convinient: you stay in control, and there's no issue with joining the organization. However, if you want your dataset to gain visibility, it seems important to us that you describe it here. In deed, if you take benefit from data or models provided by HTR-United, you may as well contribute!

To do so, you just need to [open an issue](https://github.com/HTR-United/htr-united/issues/new) or request an update on the deposit repository by adding a line formated as follows:

```yaml
        name: "Title"
        url: 'Link to repository'
        description: 'Description'
        language: French
        other-languages:
            - "Optionel"
        time: 1800--1897
        hands: 5  # Number of hands
        license:
            - {name: 'CC-BY 4.0', url: 'https://creativecommons.org/licenses/by/4.0/'} # Of course, you can change the licence
        format: Alto-XML
        volume:
            - {count: "NUMBER OF LINES", metric: lines} # or
            - {count: "NUMBER OF PAGES", metric: pages} # or
```

### You don't have one
Well, we'll be happy to get help from you. [Open an issue here](https://github.com/HTR-United/htr-united/issues/new) and we will gladly help to create and share your repository on HTR-United. Skills with `git` are appreciated but, if you want to share data, we will help you. It's the purpose of this organization!
