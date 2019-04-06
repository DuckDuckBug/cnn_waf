import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

class Detector:
    def __init__(self):
        self.tokenizer = pickle.load(open("./tokenizer/tokenizer.pickle", "rb"))
        self.model = load_model("./model/cnn_clf.h5")
        self.max_len = 600
        self.labels_type = ['SQLi', 'anomalous', 'normal', 'XSS', 'SSI', 'BufferOverflow', 'CRLFi', 'XPath', 'LDAPi', 'FormatString']

    def props_to_labels(self, props_matrix):
        labels = []
        for props_vector in props_matrix:
            idx = np.argmax(props_vector)
            label = self.labels_type[idx]
            labels.append(label)
        return labels

    def predict_url(self, url):
        label_pred = self.predict_urls([url])[0]
        return label_pred

    def predict_urls(self, urls):
        seq = self.tokenizer.texts_to_sequences(urls)
        X = sequence.pad_sequences(seq, maxlen=self.max_len)
        Y_pred = self.model.predict(X)
        labels_pred = self.props_to_labels(Y_pred)
        return labels_pred

if __name__ == '__main__':
    # for test
    detector = Detector()
    urls = []
    with open('./data/torpeda_train_test/url_test.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for d in data:
            urls.append(d[:-1])
    labels_pred = detector.predict_urls(urls[:10])
    print(labels_pred)
    label_pred = detector.predict_url(urls[0])
    print(label_pred)