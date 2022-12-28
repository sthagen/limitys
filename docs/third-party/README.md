# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/limitys/blob/default/sbom.json) with SHA256 checksum ([5238725e ...](https://git.sr.ht/~sthagen/limitys/blob/default/sbom.json.sha256 "sha256:5238725e17f5b9790c56f8d31af1cad53a4f9b80525fa9f8a14bba6db75f510c")).
<!--[[[end]]] (checksum: ff8dac9cb237eb2cf74a20e91cc6c18c)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                               | License                 | Author                      | Description (from packaging data)                                       |
|:-------------------------------------------|:------------------------------------------------------|:------------------------|:----------------------------|:------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)              | [6.0](https://pypi.org/project/PyYAML/6.0/)           | MIT License             | Kirill Simonov              | YAML parser and emitter for Python                                      |
| [gensim](http://radimrehurek.com/gensim)   | [4.2.0](https://pypi.org/project/gensim/4.2.0/)       | LGPL-2.1-only           | Radim Rehurek               | Python framework for fast Vector Space Modelling                        |
| [nltk](https://www.nltk.org/)              | [3.7](https://pypi.org/project/nltk/3.7/)             | Apache Software License | NLTK Team                   | Natural Language Toolkit                                                |
| [numpy](https://www.numpy.org)             | [1.24.0](https://pypi.org/project/numpy/1.24.0/)      | BSD License             | Travis E. Oliphant et al.   | Fundamental package for array computing in Python                       |
| [pandas](https://pandas.pydata.org)        | [1.5.2](https://pypi.org/project/pandas/1.5.2/)       | BSD License             | The Pandas Development Team | Powerful data structures for data analysis, time series, and statistics |
| [scikit-learn](http://scikit-learn.org)    | [1.1.2](https://pypi.org/project/scikit-learn/1.1.2/) | BSD License             | UNKNOWN                     | A set of python modules for machine learning and data mining            |
| [typer](https://github.com/tiangolo/typer) | [0.7.0](https://pypi.org/project/typer/0.7.0/)        | MIT License             | Sebastián Ramírez           | Typer, build great CLIs. Easy to code. Based on Python type hints.      |
<!--[[[end]]] (checksum: 668796176667cd7ab816ba317e7d973f)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
gensim==4.2.0
  - numpy [required: >=1.17.0, installed: 1.24.0]
  - scipy [required: >=0.18.1, installed: 1.9.3]
    - numpy [required: >=1.18.5,<1.26.0, installed: 1.24.0]
  - smart-open [required: >=1.8.1, installed: 6.3.0]
nltk==3.7
  - click [required: Any, installed: 8.1.3]
  - joblib [required: Any, installed: 1.2.0]
  - regex [required: >=2021.8.3, installed: 2022.10.31]
  - tqdm [required: Any, installed: 4.64.1]
pandas==1.5.2
  - numpy [required: >=1.21.0, installed: 1.24.0]
  - python-dateutil [required: >=2.8.1, installed: 2.8.2]
    - six [required: >=1.5, installed: 1.16.0]
  - pytz [required: >=2020.1, installed: 2022.7]
PyYAML==6.0
scikit-learn==1.1.2
  - joblib [required: >=1.0.0, installed: 1.2.0]
  - numpy [required: >=1.17.3, installed: 1.24.0]
  - scipy [required: >=1.3.2, installed: 1.9.3]
    - numpy [required: >=1.18.5,<1.26.0, installed: 1.24.0]
  - threadpoolctl [required: >=2.0.0, installed: 3.1.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 6c48f8b234a9548ea962a0f7d568d111)-->
