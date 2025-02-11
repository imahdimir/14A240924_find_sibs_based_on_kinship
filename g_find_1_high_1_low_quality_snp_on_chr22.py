"""

    """

from pathlib import Path

import pandas as pd



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

    # copied from 5A
    all_flt_snps = d.inp / 'all_flt_snps.parquet'
    one_low_one_high_quality_snp_on_chr22 = d.out / 'one_low_one_high_quality_snp_on_chr22.txt'
    many_high_and_low_quality_snps_on_chr22 = d.out / 'many_high_and_low_quality_snps_on_chr22.txt'


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
    df = pd.read_parquet(FP.all_flt_snps)

    ##
    df['chr'] = df['0'].str.split(':')

    ##
    _fu = lambda x : x[0]
    df['chr'] = df['chr'].apply(_fu)

    ##
    msk = df['chr'] == '22'
    df1 = df[msk]

    ##
    # sorting by info score and then getting the first and last rows
    df1 = df1.sort_values('7')

    ##
    df2 = df1.iloc[[0, -1]]

    df3a = df1.iloc[0:100]
    df3b = df1.iloc[-100 :]

    ##
    df4 = pd.concat([df3a, df3b])

    ##
    df2.to_csv(FP.one_low_one_high_quality_snp_on_chr22 , index = False, header=False,  sep = '\t')

    ##
    df4.to_csv(FP.many_high_and_low_quality_snps_on_chr22 , index = False, header = False, sep = '\t')

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


##
if __name__ == '__main__' :
    main()
