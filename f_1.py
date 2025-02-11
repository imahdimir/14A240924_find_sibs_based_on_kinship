"""

    """

from pathlib import Path

import pandas as pd
import numpy as np


class Directory :
    proj_data = '/Users/mmir/Library/CloudStorage/Dropbox/git/14A240924_find_sibs_based_on_kinship_CSF'
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
    all_wgs_fns = d.inp / 'all_WGS_filenames.txt'
    qc = d.inp / 'qc.parquet'
    imp_sample = d.inp / '22828.sample'

    qualified_iids = d.out / 'qualified_iids.txt'
    rel_with_infType = d.out / 'ukb_rel_with_infType.csv'

    qualified_rel = d.out / 'qualified_rel.csv'



FILE_PATH = FilePath()
FP = FILE_PATH


class FilePathPattern :
    d = Directory()


FILE_PATH_PAT = FilePathPattern()
FPT = FILE_PATH_PAT


class Var :
    iid = 'IID'
    id_1 = 'ID_1'
    id_2 = 'ID_2'
    id1 = 'ID1'
    id2 = 'ID2'


VAR = Var()
V = VAR


def main() :
    pass

    ##
    df_fs_po_ids = pd.read_csv(FP.po_fs_ids , header = None , dtype = 'string')

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
    df_qc['p22006'].value_counts()

    ##
    # keeping only white british
    msk = df_qc['p22006'].astype('Int8').eq(1)
    df_qc1 = df_qc[msk]

    ##
    df_qc1['p22006'].value_counts()

    ##
    df_qc1['p22019'].astype('Int8').value_counts()

    ##
    # keeping only Sex chromosome aneuploidy is nan (others are 1)

    msk = df_qc1['p22019'].isna()

    df_qc2 = df_qc1[msk]

    ##
    df_qc2['p22027'].value_counts()

    ##
    # keeping only Outliers for heterozygosity or missing rate eq nan
    msk = df_qc2['p22027'].isna()

    df_qc3 = df_qc2[msk]

    ##

    ##

    ##
    df_imp = pd.read_csv(FP.imp_sample, sep = '\s')

    ##
    assert df_imp[V.id_1].eq(df_imp[V.id_2]).all()

    ##
    df_imp = df_imp[[V.id_1]]

    ##
    df_imp = df_imp.iloc[1:]

    ##
    df_imp = df_imp.astype('string')

    ##

    ##
    df = df_fs_po_ids.copy()

    ##
    msk = df[0].isin(df_imp[V.id_1])

    df1 = df[msk]

    ##

    msk = df1[0].isin(df_qc3['eid'])

    df2 = df1[msk]

    ##
    msk = df2[0].isin(df_all_wgs_fns[0])

    df3 = df2[msk]

    ##
    df3[1] = df3[0]

    ##
    df3.to_csv(FP.qualified_iids , header = False , index = False, sep='\t')

    ##
    # just to check the number of rows being equal to the saved df3
    df4 = pd.read_csv(FP.qualified_iids , header = None , dtype = 'string')

    ##


    ##
    # keeping only qulified iids in ukb_rel data
    df_rel = pd.read_csv(FP.rel_with_infType , dtype = 'string')

    ##
    msk = df_rel[V.id1].isin(df3[0])
    msk &= df_rel[V.id2].isin(df3[0])

    ##
    df_rel_1 = df_rel[msk]

    ##
    df_rel_1['infType'].value_counts()

    ##
    df_rel_1.to_csv(FP.qualified_rel , index = False)

    ##


    ##



    ##








    ##






    ##


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
