"""

    """

from pathlib import Path

import pandas as pd


PROJ_DATA = '/Users/mmir/Library/CloudStorage/Dropbox/git/14A20240924CSF_find_sibs_based_on_kinship'
PROJ_DATA = Path(PROJ_DATA)


class Directory :
    p = PROJ_DATA

    inp = p / 'inp'
    out = p / 'out'


DIR = Directory()
D = DIR


class FilePath :
    d = Directory()

    rel = d.inp / 'ukb_rel.dat'

    rel_with_infType = d.out / 'ukb_rel_with_infType.csv'
    rel_with_infType_po = d.out / 'ukb_rel_with_infType_po.csv'
    rel_with_infType_fs = d.out / 'ukb_rel_with_infType_fs.csv'

    po_ids = d.out / 'po_ids.txt'
    fs_ids = d.out / 'fs_ids.txt'
    po_fs_ids = d.out / 'po_fs_ids.txt'


FILE_PATH = FilePath()
FP = FILE_PATH


class Var :
    kinship = 'Kinship'
    ibs0 = 'IBS0'
    infType = 'InfType'
    id1 = 'ID1'
    id2 = 'ID2'


VAR = Var()
V = VAR

"""
from Alex's email:

Ah I think the issue is that the kinship file here only gives IBS0, which is the fraction of sites that differ at both alleles, not IBD0, which is what the pi0 in Table 1 is referring to. 

If you look at the UK Biobank relationship inference (Section 3.7 here https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-018-0579-z/MediaObjects/41586_2018_579_MOESM1_ESM.pdf) they simply use IBS0<0.0012 to call parent-offspring pairs different from sibling pairs.

    That is, we assigned each related pair to one of twins, parent-offspring, siblings, 2nd degree or 3rd degree relatives using the kinship coefficient boundaries recommended by the authors of KING (see Table 1 in their publication16). We used IBS0 only to distinguish parent-child from sibling pairs, who have the same expected kinship coefficient. Specifically, we called any pair with IBS0 < 0.0012 as parentoffspring.
"""


def classify_relationship(kinship , ibs0) :
    k0 = 1 / 2 ** (2.5)
    k1 = 1 / 2 ** (3 / 2)
    k2 = .0012

    if k0 <= kinship <= k1 :
        if ibs0 < k2 :
            return 'PO'
        else :
            return 'FS'
    return 'Other'


def main() :
    pass

    ##
    df = pd.read_csv(FP.rel , sep = '\s')

    ##
    fu = lambda x : classify_relationship(x[V.kinship] , x[V.ibs0])
    df[V.infType] = df.apply(fu , axis = 1)

    ##
    df[V.infType].value_counts()

    ##
    df.to_csv(FP.rel_with_infType , index = False)

    ##
    df_po = df[df[V.infType] == 'PO']
    df_po.to_csv(FP.rel_with_infType_po , index = False)

    ##
    df_fs = df[df[V.infType] == 'FS']
    df_fs.to_csv(FP.rel_with_infType_fs , index = False)

    ##
    po_ids = df_po[[V.id1 , V.id2]]
    po_ids = po_ids.stack()
    po_ids = po_ids.drop_duplicates()
    po_ids.to_csv(FP.po_ids , index = False , header = None)

    ##
    fs_ids = df_fs[[V.id1 , V.id2]]
    fs_ids = fs_ids.stack()
    fs_ids = fs_ids.drop_duplicates()
    fs_ids.to_csv(FP.fs_ids , index = False , header = None)

    ##
    po_fs_ids = pd.concat([po_ids , fs_ids])
    po_fs_ids = po_fs_ids.drop_duplicates()
    po_fs_ids.to_csv(FP.po_fs_ids , index = False , header = None)

    ##


    ##

    ##
    df[V.infType].value_counts()


##
def check_iids_are_the_same() :
    pass

    ##
    fn = '/Users/mmir/Library/CloudStorage/Dropbox/git/14A20240924CSF_find_sibs_based_on_kinship/inp/hap.kin0'
    df_kin = pd.read_csv(fn , sep = '\s')

    ##
    df_kin = df_kin[[V.id1 , V.id2 , V.kinship , V.ibs0 , V.infType]]

    ##
    df_rel = df[df[V.infType].isin(['PO' , 'FS'])]

    ##


    ##
    df_merge = pd.merge(df_kin ,
                        df_rel ,
                        on = [V.id1 , V.id2] ,
                        how = 'outer' ,
                        indicator = True)

    ##
    df_merge['_merge'].value_counts()

    ##
    df_merge_both = df_merge[df_merge['_merge'] == 'both']

    ##
    df_merge_both['inf_eq_check'] = df_merge_both[V.infType + '_x'].eq(
            df_merge_both[V.infType + '_y'])

    ##
    df_merge_both['inf_eq_check'].value_counts()


    ##


    ##
