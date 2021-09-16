---
name: Add a new description
about: Template to add the description of a new dataset
title: "[catalog] New repo {project-name/dataset-name}"
labels: project
assignees: ''

---

## Description of the dataset

### Checklist
- [ ] name of the corpus is explicitly stated
- [ ] name of the project is explicitly stated
- [ ] authors and roles are explicitly stated
- [ ] a license is associated with the dataset
- [ ] the dataset is described in a clear and explicit way enabling other users to understand its content and context of creation
- [ ] the dataset uses standard formats such as PAGE XML or ALTO XML and is aligned with images

### Relevant information

- name of the corpus<sup>[1](#fn1)</sup>: 
- name of the project<sup>[2](#fn2)</sup>:
- description generated with [our form](https://htr-united.github.io/document-your-data-en.html)
```
[paste description here]
```

### Autonomy

Check applicable situation:

- [ ] I know how to make a Pull Request and will create the corresponding directory and files under "[htr-united/catalog/](https://github.com/HTR-United/htr-united/tree/master/catalog)"
- [ ] I don't know how to do a Pull Request, I need assistance to add the description of my dataset under "[htr-united/catalog/](https://github.com/HTR-United/htr-united/tree/master/catalog)"

---

<a name="fn1">1</a>: This name will be used to create a YAML file dedicated to this dataset.  *For example: if your dataset is called "My Awesome Dataset", its description will be saved under "my-awesome-dataset.yml"*

<a name="fn2">2</a>: This name will be used to create a folder under "catalog/" containing all the datasets related to your project. *For example: if you project is called "My Awesome Project", the YAML file(s) describing your datasets will be saved under "catalog/my-awesome-project/"*
