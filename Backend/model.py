import pickle
#from sklearn.linear_model import LogisticRegression


def get_model():
    lrmodel = pickle.load(open("files/dataset.pkl", "rb"))
    cv = pickle.load(open("files/cv.pkl", "rb"))
    return (lrmodel,cv)