import pandas as pd
import numpy as np

#可能是essays_mairesse+mairesse_attributes 然后删了几个 最后是80维

if __name__ == "__main__":
    # mairesse = pd.read_csv("../data/essays/psycholinguist_features/essays_mairesse.csv", header=None)
    mairesse = pd.read_csv("../data/essays/psycholinguist_features/essays_mairesse_final.csv", header=None)
    columns = pd.read_csv("../data/essays/psycholinguist_features/mairesse_attributes.csv", header=None)
    labels = np.transpose(columns.values.tolist())[0].tolist() #transpose转置
    labels.remove('BROWN-FREQ numeric')
    labels.remove('K-F-FREQ numeric')
    labels.remove('K-F-NCATS numeric')
    labels.remove('K-F-NSAMP numeric')
    labels.remove('T-L-FREQ numeric')
    mairesse.columns = labels
    mairesse = mairesse[mairesse.columns[:-5]]
    mairesse.to_csv("../data/essays/psycholinguist_features/essays_mairesse_labeled_final.csv", index=False)
    print("done")
