def init_model(location, modelname):

    from torch import cuda
    import torch.nn as nn
    from transformers import DistilBertModel
    import torch
    
    """
    Load the pretrained BERT model for text description data.
    """
    
    device = 'cuda' if cuda.is_available() else 'cpu'
    bert = DistilBertModel.from_pretrained('distilbert-base-uncased')
    
    class BERT(nn.Module):
        def __init__(self, bert):

            super(BERT, self).__init__()

            self.bert = bert
            self.dropout = nn.Dropout(0.1)
            self.relu =  nn.ReLU()
            self.fc1 = nn.Linear(768, 512)
            self.fc2 = nn.Linear(512, 2)
            self.softmax = nn.LogSoftmax(dim=1)

        def forward(self, **kwargs):

            cls_hs = self.bert(**kwargs)
            hidden_state = cls_hs.last_hidden_state
            pooler = hidden_state[:, 0]
            x = self.fc1(pooler)
            x = self.relu(x)
            x = self.dropout(x)
            x = self.fc2(x)
            x = self.softmax(x)

            return x
        
    model = BERT(bert)
    model = model.to(device)

    try:
        model_save_name = modelname
        path = location + model_save_name
        model.load_state_dict(torch.load(path))

    except:
        model_save_name = modelname
        path = location + model_save_name
        model.load_state_dict(torch.load(path, 
                                         map_location=torch.device('cpu')))
                                         
    model.eval()
    
    return model