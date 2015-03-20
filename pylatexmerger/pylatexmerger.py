# -*- coding: utf-8 -*-

__author__ = 'Viktor Dmitriyev'
__copyright__ = 'Copyright 2015, Viktor Dmitriyev'
__credits__ = ['Viktor Dmitriyev']
__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = '-'
__email__   = ''
__status__  = 'dev'
__date__    = '18.03.2015'
__description__ = 'Merging separated LaTeX parts of ab article into single TEX file.'

import os
import shutil

class DirectoryHelper():

    def __init__(self, config):
        """
            (obj, class)-> None
        """
        self.config = config

        self.current_dir = os.path.dirname(os.path.abspath(__file__)) + '\\'

        try:
            #self.publication_path = self.config.PUBLICATION_PATH + '\\'
            self.publication_path = self.config.PUBLICATION_PATH
        except Exception, ex:
            self.publication_path = self.current_dir
            print '[i] publication path was set as a current dir: {}'.format(self.publication_path)

        print '[i] current directory: {}'.format(self.current_dir)
        self.temp_dir = self.current_dir + self.config.TEMP_DIRECTORY + '\\'

    def clear_directory(self, directory):
        """
            (obj, str) -> None

            Clears given 'directory'.
        """
        for root, dirs, files in os.walk(directory):
            for f in files:
                os.unlink(os.path.join(root, f))

            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

    def prepare_working_directory(self):
        """
            (obj) -> None

            Prepearing current directory for working:
                -   checking if temp folder is existing and creating it;
                -   clearing temp directory;
                -
        """

        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

        self.clear_directory(self.temp_dir)


    def move_from_temp_directory(self):
        """
            (obj) -> None

            Current method will implement versioning of publication.
        """

    def upper_directory(self):
        """
            (obj) -> None

            Identify upper directory.
        """

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        up_dir = cur_dir[:cur_dir.rfind('\\')] + '\\'
        return up_dir

    def save_file(self, file_name, text):
        """
            (obj,str,str) -> None

            Save to 'file_name' given 'text'.
        """

        with open(file_name, 'w') as content_file:
            content = content_file.write(text)

    def read_file(self, file_name):
        """
            (obj, str) -> (str)

            Reads text from 'file_name' and return it
        """

        with open(file_name, 'r') as file_input:
            file_content = file_input.read()
        return file_content

class PrepearPublication():

    def __init__(self, config):
        """
            (obj, class) -> None

            Init method
        """

        self.config = config
        self.dir_helper = DirectoryHelper(config)

        self.dir_helper.prepare_working_directory()
        print '[i] working directory prepeared'

        self.temp_dir = self.dir_helper.temp_dir
        self.source_tex_file = self.dir_helper.publication_path + self.config.TEX_FILE
        self.publication_path = self.dir_helper.publication_path
        print '[i] main tex file: "{}"'.format(self.source_tex_file)

        self.dest_tex_file = self.temp_dir + self.config.TEX_FILE


    def info(self):
        print "Publication is ready [IN CASE OF NO ERROR]"
        print "Check following folder: \n" + self.temp_dir

    def construct_path(self, str_input):
        """
            (obj, str) -> (str)

            Transform 'str_input' to proper file name.
        """

        str_result = str_input[len('\input{'):-1]
        str_result = self.publication_path + str_result

        #print dir(self)

        print '[i] constructed path {}'.format(str_result)

        if str_result[-3:] != 'tex':
             str_result = str_result + '.tex'
        return str_result

    def replace_bibliography(self, text):
        """
            (obj, str) -> (str)

            Returns text where bibliography is replaced by content from 'bbl' file.
        """

        indexBegin = 0
        indexEnd = 0
        indexBegin = text.find('\\bibliography{', indexBegin+1)
        indexEnd = text.find('}', indexBegin+1)
        text_to_replace = text[indexBegin:indexEnd+1]
        new_text = self.dir_helper.read_file(file_name = self.temp_dir + self.config.BBL_FILE)
        bbl_text = ""
        for line in new_text.split('\n'):
            bbl_text = bbl_text + '\t' + line + '\n'
        text = text.replace(text_to_replace, bbl_text)

        return text

    def replace_includes(self, file_name):
        """
            (obj,str) -> (str)

            Recursive method that returns text with replaced tex tags by inserting text there.
        """

        indexBegin = 0
        indexEnd = 0
        text = self.dir_helper.read_file(file_name)
        while indexBegin != -1:
            indexBegin = text.find('\input{', indexBegin+1)
            indexEnd = text.find('}', indexBegin+1)
            text_to_replace = text[indexBegin:indexEnd+1]
            if indexBegin != -1:
                # print 'text_to_replace : ' + text_to_replace
                new_path = self.construct_path(text_to_replace)
                new_text = self.replace_includes(file_name = new_path)
                text = text.replace(text_to_replace, new_text)

        return text

    def copy_supported_files(self):

        for directory in self.config.DIRS_TO_COPY:
            shutil.copytree(self.dir_helper.publication_path + directory,
                            self.temp_dir + directory)

        for file_ in self.config.FILES_TO_COPY:
            index = file_.rfind('\\')
            dest_file = file_
            if index != -1:
                dest_file = file_[index+1:]

            #print '[i] dest_file: {}'.format(dest_file)

            shutil.copy2(self.dir_helper.publication_path + file_,
                         self.temp_dir + dest_file)

    def create_bat_file(self):
        """
            (obj) -> None

            Creating bat files.
        """

        bat_commands = '@echo off\n'
        bat_commands = bat_commands + 'rem @author Viktor Dmitriyev\n'

        bat_commands = bat_commands + '\necho "Compiling LaTex to PDF. Please, wait ..."\n'
        bat_commands = bat_commands + 'pdflatex {}\n'.format(self.config.TEX_FILE)
        bat_commands = bat_commands + 'pdflatex {}\n'.format(self.config.TEX_FILE)

        bat_commands = bat_commands + '\necho "Deleting unnecessary files"\n'
        bat_commands = bat_commands + 'del *.aux\n'
        bat_commands = bat_commands + 'del *.log\n'
        bat_commands = bat_commands + '\necho "Opening pdf"\n'
        bat_commands = bat_commands + 'pdflatex {}\n'.format(self.config.TEX_FILE[:-3] + 'pdf')

        self.dir_helper.save_file(self.temp_dir + self.config.BAT_FILE_NAME, bat_commands)

        print '[i] batch file was created: "{}"'.format(self.config.BAT_FILE_NAME)

    def process(self):
        """
            (obj) -> None

            Main method that executes others in right order.
        """

        self.copy_supported_files()
        updated_text = self.replace_includes(file_name=self.source_tex_file)
        final_text = self.replace_bibliography(updated_text)
        self.dir_helper.save_file(file_name=self.dest_tex_file, text=final_text)
        self.create_bat_file()
        self.info()

def main():

    # try:
    import configs as configs
    publication = PrepearPublication(configs)
    publication.process()
    # except Exception, ex:
    #     print '[e] exception: {}'.format(str(ex))
    #     print '[i] create file with configs "configs.py", check README for details'

if __name__ == '__main__':
    main()
