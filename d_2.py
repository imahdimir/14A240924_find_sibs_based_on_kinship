"""

    """

from pathlib import Path

import pandas as pd
import numpy as np


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
    all_wgs_fns = d.inp / 'all_WGS_filenames.txt'
    qc = d.inp / 'qc.parquet'


FILE_PATH = FilePath()
FP = FILE_PATH


class FilePathPattern :
    d = Directory()


FILE_PATH_PAT = FilePathPattern()
FPT = FILE_PATH_PAT


class Var :
    iid = 'IID'


VAR = Var()
V = VAR


def main() :
    pass

    ##
    df_fs_po_ids = pd.read_csv(FP.po_fs_ids , header = None , dtype = 'string')

    ##
    df_filtered_ids = pd.read_csv(FP.filtered_ids ,
                                  header = None ,
                                  dtype = 'string')

    ##
    df_all_wgs_fns = pd.read_csv(FP.all_wgs_fns ,
                                 header = None ,
                                 dtype = 'string')

    ##
    df_all_wgs_fns[V.iid] = df_all_wgs_fns[0].str.split('_')

    ##
    _fu = lambda x : x[0]

    df_all_wgs_fns[V.iid] = df_all_wgs_fns[V.iid].apply(_fu)

    ##
    df_all_wgs_fns[0] = df_all_wgs_fns[V.iid]

    ##
    df_all_wgs_fns = df_all_wgs_fns.drop(columns = V.iid)

    ##
    df_all_wgs_fns = df_all_wgs_fns.drop_duplicates()

    ##
    df_qc = pd.read_parquet(FP.qc)

    ##
    def common_items_count(listA , listB) :
        return len(set(listA) & set(listB))

    ##
    # Populate the matrix with counts of common items
    lists = [df_fs_po_ids[0] , df_filtered_ids[0] , df_all_wgs_fns[0] ,
             df_qc['eid']]

    # List of names for columns and indices
    list_names = ['UKB_REL_PO_FS_IDS' , 'FILTERED_IDS_FROM_SAMPLE_QC' ,
                  'WGS_FILENAMES_IDS' , 'QC_IDS']

    # Create an empty DataFrame with the list names as columns and index
    df = pd.DataFrame(index = list_names , columns = list_names)

    # Use nested loops to fill the DataFrame with the common item counts
    for i in range(len(lists)) :
        for j in range(len(lists)) :
            df.iloc[i , j] = common_items_count(lists[i] , lists[j])

    ##


    ##


    ##


    ##


    ##


    ##


    ##


##
if __name__ == '__main__' :
    main()
