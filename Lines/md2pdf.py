"""
convert markdown to pdf
edit by hichens
"""

import os
import sys

if __name__ == "__main__":
    dirs = '../docs/'
    out_dirs = '../outs/'
    md_path = os.path.join(out_dirs, 'TBBT.md')
    pdf_path = os.path.join(out_dirs, 'TBBT.pdf')

    ## get the sub dirs
    dir_names = []
    for dir_name in os.listdir(dirs):
        # print(dir_name)
        dir_names.append(dir_name)
    dir_names.sort(key=lambda x: int(x.split("-")[-1]))
    
    ## get all the file path and sort it 
    file_paths = []
    for dir_name in dir_names:
        dir_path = os.path.join(dirs, dir_name)
        
        unsorted_file_paths = []
        for file_name in os.listdir(dir_path):
            unsorted_file_paths.append(file_name)
        
        unsorted_file_paths.sort(key=lambda x: int(x.split("-")[3]))
        for i, file_path in enumerate(unsorted_file_paths):
            unsorted_file_paths[i] = os.path.join(dir_path, file_path)
        
        file_paths += unsorted_file_paths
    
    ## write to one file 
    F = open(md_path, 'w')
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            contents = f.readlines()
            F.writelines(contents)
            F.writelines("\n\n\n\n\n")
    F.close()

    ## convert to pdf
    os.system("md2pdf ../outs/TBBT.md ../outs/TBBT.pdf")