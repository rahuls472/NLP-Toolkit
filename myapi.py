
import nlpcloud

class API:
    # def __init__(self):
    #     client = nlpcloud.Client("t5-base-en-generate-headline", "c36f586839e3bdf4f41111c0a0f33efe8f19e0fe", gpu=False)


    def Heading(self,Text):
        client = nlpcloud.Client("t5-base-en-generate-headline", "c36f586839e3bdf4f41111c0a0f33efe8f19e0fe", gpu=False)
        Response=client.summarization(Text)
    
        return Response['summary_text']
    

    def sentiment_analysis(self,Text):
        import nlpcloud

        client = nlpcloud.Client("distilbert-base-uncased-emotion", "c36f586839e3bdf4f41111c0a0f33efe8f19e0fe", gpu=False)
        response = client.sentiment(Text)

        return response
    

    def Ner_analysis(self,entity,para):
        

        client = nlpcloud.Client("finetuned-llama-3-70b", "c36f586839e3bdf4f41111c0a0f33efe8f19e0fe", gpu=True)
        response = client.entities(para,searched_entity=entity)
        return response