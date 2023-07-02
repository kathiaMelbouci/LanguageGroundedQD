import matplotlib.pyplot as plt
import sys
import json
import MiscUtils
import numpy as np



if __name__=="__main__":

    fn=sys.argv[1]
    with open(fn,"r") as fl:
        progress_dict=json.load(fl)

    start_at=0
    if len(sys.argv)>2:
        start_at=int(sys.argv[2])

    #print("train_loss:\n",progress_dict["train_loss"])
    print("MIN train_loss:\n",min(progress_dict["train_loss"]))
    #print("val_loss:\n",progress_dict["val_loss"])
    print("MIN val_loss:\n",min(progress_dict["val_loss"]))
    plt.plot(progress_dict["train_loss"][start_at:],"r",label="train")
    plt.plot(progress_dict["val_loss"][start_at:],"b",label="validation")
    lr=progress_dict["lr"] if "lr" in progress_dict.keys() else "not logged"
    plt.title(f"epoch with best val loss={progress_dict['epoch_with_best_val_loss']}, LR at cur epoch ={np.round(lr,6)})")
    #plt.title(f"min train_loss={min(progress_dict['train_loss'])}\n min val_loss={min(progress_dict['val_loss'])}")
    plt.legend(fontsize=16)
    plt.tight_layout()
    plt.grid("on")
    plt.show()
