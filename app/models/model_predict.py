import torch
from transformers import DistilBertTokenizer
from app.models.model_load import init_model
import matplotlib
import matplotlib.colors as mcolors
from spacy.lang.en import English

class Predict:
    def __init__(self, *args):
        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
        self.model = init_model('app/models/saved_weights/', 'model.pt')
        self.SpaCy_model = English()
        self.SpaCy_model.add_pipe('sentencizer')

    def classify(self, sentence):
        with torch.no_grad():
            inputs = self.tokenizer(sentence, return_tensors="pt")
            outputs = self.model(**inputs)
            exps = torch.exp(outputs)
            exps_np = exps[0][1].numpy()
        return exps_np

    def hex_color(self, prediction):
        # Get last prediction in case of strings
        if type(prediction) == str:
            prediction = self.classify(prediction)
        cmap = matplotlib.cm.BuGn
        norm = mcolors.Normalize(vmin=0, vmax=1)
        return matplotlib.colors.rgb2hex(cmap(norm(prediction)))

    def HTML_values(self, span):
        colors_background = []
        colors_text = []
        sentences = []
        doc = self.SpaCy_model(span)

        for sentence in doc.sents:
            value = self.classify(sentence.text)
            color = self.hex_color(value)
            if value > 0.8:
                text_color = "#FFFFFF"
            else:
                text_color = "#000000"
            colors_text.append(text_color)
            colors_background.append(color)
            sentences.append(sentence.text)
        return sentences, colors_text, colors_background

