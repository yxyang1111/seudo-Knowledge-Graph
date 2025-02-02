#config.py

#Data
Data_path = "../data/"
Spacy_name = "zh_core_web_trf"

#NLP rules
patterns =  r'。|？|！|；|\r|;| '

#Model
Embedding_model_path = '/home/user/embeddings/bge_keyworkds_projectName_fields_tunning_v3'
LLM_model

#Database
neo4j_uri = "bolt://localhost:7687"
neo4j_auth = ("neo4j", "s3cretPassword")