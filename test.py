# import os
# import json
# from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()

# uri = os.environ.get("MONGO_URI")

# collection = MongoClient(uri)['test']['examquestionbanks']

# data = collection.find({}, {'question.explanation'}).to_list()

# # print(list(data))



# with open("explanation_data.json", 'w', encoding="utf-8") as f:
#     json.dump(data, f, indent=4, default=str)

import ast
import json
from asset.core.clear_data import CleanData
with open('explanation_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data = str(data)

clean_data = ast.literal_eval(data)

with open("explanation_data_1.json", 'w', encoding="utf-8") as f:
    json.dump(clean_data, f, indent=4, default=str)

