from converter.jsonl2doclevel import jsonl2doclevel
from sklearn.metrics import cohen_kappa_score
import pandas as pd

def pairwise_cohen(file_path_1,file_path_2,doclevel_mode,relation_mode,debug=False):
    doclevel_1 = jsonl2doclevel(file_path_1,doclevel_mode,relation_mode,debug)
    doclevel_2 = jsonl2doclevel(file_path_2,doclevel_mode,relation_mode,debug)
    if doclevel_mode == "majority" or doclevel_mode == "majority_mix" or doclevel_mode == "mix":
        return cohen_kappa_score(doclevel_1,doclevel_2)
    elif doclevel_mode == "all":
        cohen_12 = [cohen_kappa_score(doclevel_1.majority,doclevel_2.majority),cohen_kappa_score(doclevel_1.majority_mix,doclevel_2.majority_mix),cohen_kappa_score(doclevel_1.mix,doclevel_2.mix)]
        mode = ["majority","majority_mix","mix"]
        df_cohen = pd.DataFrame({"doclevel_mode":mode,"cohen_1_vs_2":cohen_12})
        return df_cohen
    else:
        raise ValueError(f"Wrong doclevel_mode. Only 'majority', 'majority_mix', 'mix', or 'all' is allowed.")
