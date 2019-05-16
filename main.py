from models.naive_bayes import NB_classifier
from models.linear import L_classifier
import models.tools.file_writer
from models.tools.Corpus import Corpus

train_corpus = Corpus('train.csv')
model = L_classifier(8)
model.train(train_corpus)
print(model.w)

val_corpus = Corpus('val.csv')
val_corpus.set_predict(model.predict(val_corpus))

val_corpus.set_label_title(('Anger', 'Anticipation', 'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise', 'Trust'))
eval_result = val_corpus.eval()
print(eval_result)

# pred_file = open('predict.csv', 'a')


