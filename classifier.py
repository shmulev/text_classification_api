import numpy as np
import pickle
from utils import stemming

def classify(dataJSON):
	#load the pretrained model
	try:
		clf = pickle.load(open("clf.pkl", "rb"))

		#classify new command
		#CLF_THRES = 0.17
		#dict = {0: "Open list", 1: "show", 2: "sort", 3: "close"}

		label = clf.predict([dataJSON["text"]])[0]
		prob = clf.predict_proba([dataJSON["text"]])[0].max()
		#probs = np.array([i > CLF_THRES for i in probs], dtype='int')
		#return labels.tolist()
		return str(label), str(prob)
		
	except Exception as error:
		return repr(error)