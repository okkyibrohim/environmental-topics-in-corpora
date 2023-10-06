from converter.jsonl2doclevel import jsonl2doclevel
from nltk import agreement
import pandas as pd
import numpy as np

def single_fleiss(label_1,label_2,label_3):
    taskdata=[[0,str(i),str(label_1[i])] for i in range(0,len(label_1))]+[[1,str(i),str(label_2[i])] for i in range(0,len(label_2))]+[[2,str(i),str(label_3[i])] for i in range(0,len(label_3))]
    ratingtask = agreement.AnnotationTask(data=taskdata)
    return ratingtask.multi_kappa()

def three_annotators_fleiss(file_path_1,file_path_2,file_path_3,doclevel_mode,relation_mode,debug=False):
    doclevel_1 = jsonl2doclevel(file_path_1,doclevel_mode,relation_mode,debug)
    doclevel_2 = jsonl2doclevel(file_path_2,doclevel_mode,relation_mode,debug)
    doclevel_3 = jsonl2doclevel(file_path_3,doclevel_mode,relation_mode,debug)
    if doclevel_mode == "majority" or doclevel_mode == "majority_mix" or doclevel_mode == "mix":
        return single_fleiss(doclevel_1,doclevel_2,doclevel_3)
    elif doclevel_mode == "all":
        fleiss_majority = single_fleiss(doclevel_1.majority,doclevel_2.majority,doclevel_3.majority)
        fleiss_majoritymix = single_fleiss(doclevel_1.majority_mix,doclevel_2.majority_mix,doclevel_3.majority_mix)
        fleiss_mix = single_fleiss(doclevel_1.mix,doclevel_2.mix,doclevel_3.mix)
        mean = (fleiss_majority+fleiss_majoritymix+fleiss_mix)/3
        df_fleiss = pd.DataFrame({"majority":[fleiss_majority],"majority_mix":[fleiss_majoritymix],"mix":[fleiss_mix],"mean_fleiss":mean})
        return df_fleiss
    else:
        raise ValueError(f"Wrong doclevel_mode. Only 'majority', 'majority_mix', 'mix', or 'all' is allowed.")
