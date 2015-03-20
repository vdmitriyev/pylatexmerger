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
