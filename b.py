"""

    """

from pathlib import Path

import pandas as pd


class Directory :
    proj_data = '/Users/mmir/Library/CloudStorage/Dropbox/git/14A20240924_find_sibs_based_on_kinship_CSF'
    proj_data = Path(proj_data)
    p = proj_data

    inp = p / 'inp'
    med = p / 'med'
    out = p / 'out'


DIR = Directory()
D = DIR


class FilePath :
    d = Directory()

    po_fs_ids = d.out / 'po_fs_ids.txt'
    filtered_ids = d.inp / 'filtered_ids.txt'


FILE_PATH = FilePath()
FP = FILE_PATH


class FilePathPattern :
    d = Directory()


FILE_PATH_PAT = FilePathPattern()
FPT = FILE_PATH_PAT


class Var :
    pass


VAR = Var()
V = VAR


def main() :
    pass

    ##
    df_fs_po_ids = pd.read_csv(FP.po_fs_ids , header = None , dtype = 'string')

    ##
    df_fs_po_ids = df_fs_po_ids.drop_duplicates()

    # There is no dups

    ##
    df_filtered_ids = pd.read_csv(FP.filtered_ids ,
                                  header = None ,
                                  dtype = 'string')

    ##
    _fu = lambda x : x.strip()
    df_fs_po_ids = df_fs_po_ids.applymap(_fu)
    df_filtered_ids = df_filtered_ids.applymap(_fu)

    ##
    msk = df_fs_po_ids[0].isin(df_filtered_ids[0])

    df1 = df_fs_po_ids[msk]

    ##


    ##


    ##


    ##


    ##


##
if __name__ == '__main__' :
    main()
