### About

A really huge amount of people around the glob is using [LaTeX](http://www.latex-project.org/) as a primary software tool for maintaining their texts. Especially, it's very popular word processing package in academia, at least at the technical part of it.

This is tiny Python scripts that is helping to write a collaborative publication using LaTeX, especially when the writing itself is done in parallel by couple of people. Basically, script merges all separated part of the single TeX publication in a single TeX file.

### What Is It Useful For?

Usually, the scientific publication is done by small group of people. Before starting write process, the structure of a publication should be identified. One of the main issues while working on one single publication within the group is the merging procedure. In order to write a publication I try to organize it in a following way:

* Separate content of the publication from it's processing part
* Make process of publication writing transparent (host and share all the publication files through the dropbox)
* Organize versioning (default feature of documents hosting services like dropbox)

Check [sample-paper](sample-paper) folder for concrete example of the paper organization.

### Example

Check [sample-paper](sample-paper) folder for the example publication that is using LaTeX template [LNBIP](http://www.springer.com/computer/lncs?SGWID=0-164-6-793326-0) (Lecture Notes in Business Information Processing) from Springer. Before running python script, you will need to create 'configs.py' at the same directory and specify path to your publication:

```
# -*- coding: utf-8 -*-

################
# Configurations
################

TEMP_DIRECTORY = '__temp__'
BAT_FILE_NAME = '_build_latex.bat'
TEX_FILE = 'sample-paper.tex'
BBL_FILE = 'sample-paper.bbl'

# a list of the files that will be copied
FILES_TO_COPY = ['sprmindx.sty', 'svmultln.cls', 'splncs.bst', 'svlnbip.clo', 'bibliography\\{}'.format(BBL_FILE)]
DIRS_TO_COPY = ['models\\png']

# path to publication
PUBLICATION_PATH = '../sample-paper/'
```

### Getting Started (Fast Run)
```
git clone https://github.com/vdmitriyev/pylatexmerger.git
cd pylatexmerger
cd pylatexmerger
python pylatexmerger.py
```


### Author

* Viktor Dmitriyev
