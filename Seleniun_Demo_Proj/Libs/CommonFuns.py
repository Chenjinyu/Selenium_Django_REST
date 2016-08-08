import sys
from datetime import datetime
from os import makedirs
import posixpath
from os.path import join, exists, dirname, abspath, basename, splitext
from os import makedirs, walk, stat, walk



def get_current_script_name():
    return splitext(basename(sys.argv[0]))[0]

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

def get_current_date():
    return datetime.now().strftime("%Y_%m_%d")

def get_project_root():
    return dirname(abspath(__file__))[:-4]
    
def create_folder(folder_path):
    makedirs(join(folder_path, get_current_timestamp()))
    
if __name__ == '__main__': 
    print get_current_timestamp()
    create_folder(get_project_root())
    
    
    