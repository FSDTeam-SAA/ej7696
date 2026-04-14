import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.environ.get("MONGO_URI")

collection = MongoClient(uri)['test']['examquestionbanks']

data = collection.find({}, {'question.explanation'}).to_list()

print(list(data))



with open("explanation_data.json", 'w', encoding="utf-8") as f:
    json.dump(data, f, indent=4, default=str)