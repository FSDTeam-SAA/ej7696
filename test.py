# import os
# import json
# from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()

# uri = os.environ.get("MONGO_URI")

# collection = MongoClient(uri)['test']['examquestionbanks']

# data = collection.find({}, {'question.explanation'}).to_list()

# print('-'*60)
# print(f"Total find : {len(data)} question")
# print('-'*60)



# with open("explanation_data.json", 'w', encoding="utf-8") as f:
#     json.dump(data, f, indent=4, default=str)

import ast
import json
from asset.core.clear_data import CleanData

with open('question_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data = str(data)
data = CleanData(data)

if isinstance(data, str):
    clean_data = ast.literal_eval(data)
else:
    clean_data = data

with open("explanation_data_1.json", 'w', encoding="utf-8") as f:
    json.dump(clean_data, f, indent=4, ensure_ascii=False)

