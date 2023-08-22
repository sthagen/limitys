# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/limitys/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([73ac7715 ...](https://git.sr.ht/~sthagen/limitys/blob/default/etc/sbom/cdx.json.sha256 "sha256:73ac7715b5d7fa71c9b6df62ef4a4694a4e35acedea7b8418b0ac6fafc26f3a4")).
<!--[[[end]]] (checksum: 5c2a0f56ca2fb5bf6bf7f5af649c3494)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                         | License       | Author            | Description (from packaging data)                                  |
|:-------------------------------------------|:------------------------------------------------|:--------------|:------------------|:-------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)              | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/) | MIT License   | Kirill Simonov    | YAML parser and emitter for Python                                 |
| [gensim](http://radimrehurek.com/gensim)   | [4.3.1](https://pypi.org/project/gensim/4.3.1/) | LGPL-2.1-only | Radim Rehurek     | Python framework for fast Vector Space Modelling                   |
| [typer](https://github.com/tiangolo/typer) | [0.9.0](https://pypi.org/project/typer/0.9.0/)  | MIT License   | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 1d34d7add94a85ea1ed0d03582907c57)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                              | Author                                                                                | Description (from packaging data)                                                 |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-------------------------------------|:--------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                          | UNKNOWN                                                                               | Composable command line interface toolkit                                         |
| [numpy](https://www.numpy.org)                                   | [1.25.2](https://pypi.org/project/numpy/1.25.2/)           | BSD License                          | Travis E. Oliphant et al.                                                             | Fundamental package for array computing in Python                                 |
| [python-dateutil](https://github.com/dateutil/dateutil)          | [2.8.2](https://pypi.org/project/python-dateutil/2.8.2/)   | Apache Software License; BSD License | Gustavo Niemeyer                                                                      | Extensions to the standard Python datetime module                                 |
| [pytz](http://pythonhosted.org/pytz)                             | [2023.3](https://pypi.org/project/pytz/2023.3/)            | MIT License                          | Stuart Bishop                                                                         | World timezone definitions, modern and historical                                 |
| [regex](https://github.com/mrabarnett/mrab-regex)                | [2023.8.8](https://pypi.org/project/regex/2023.8.8/)       | Apache Software License              | Matthew Barnett                                                                       | Alternative regular expression module, to replace re.                             |
| [scipy](https://scipy.org/)                                      | [1.11.1](https://pypi.org/project/scipy/1.11.1/)           | BSD License                          | "SciPy Developers" <scipy-dev@python.org>                                             | Fundamental algorithms for scientific computing in Python                         |
| [six](https://github.com/benjaminp/six)                          | [1.16.0](https://pypi.org/project/six/1.16.0/)             | MIT License                          | Benjamin Peterson                                                                     | Python 2 and 3 compatibility utilities                                            |
| [smart-open](https://github.com/piskvorky/smart_open)            | [6.3.0](https://pypi.org/project/smart-open/6.3.0/)        | MIT License                          | Radim Rehurek                                                                         | Utils for streaming large files (S3, HDFS, GCS, Azure Blob Storage, gzip, bz2...) |
| [threadpoolctl](https://github.com/joblib/threadpoolctl)         | [3.2.0](https://pypi.org/project/threadpoolctl/3.2.0/)     | BSD License                          | Thomas Moreau                                                                         | threadpoolctl                                                                     |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License   | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+                            |
<!--[[[end]]] (checksum: 67ea000c43cabd95e918733881b23bcf)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
gensim==4.3.1
├── numpy [required: >=1.18.5, installed: 1.25.2]
├── scipy [required: >=1.7.0, installed: 1.11.1]
│   └── numpy [required: >=1.21.6,<1.28.0, installed: 1.25.2]
└── smart-open [required: >=1.8.1, installed: 6.3.0]
PyYAML==6.0.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 83f85f05902bc0f117874503c158015a)-->
