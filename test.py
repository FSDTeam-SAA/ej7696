"""from asset.core.prompts import GenBookPrompt

prompt = GenBookPrompt()

print(prompt)
"""

"""from dotenv import load_dotenv
from asset.config.gen_model import LoadGenAI

load_dotenv()

model = LoadGenAI(model_name='gemini-2.5-flash')

resp = model.invoke('what is transformer?? explain within five line')

print(resp.content)"""
"""
import os
from random import random
from dotenv import load_dotenv
from asset.core.prompts import GenBookPrompt
from asset.config.gen_model import LoadGenAI

load_dotenv()

model = LoadGenAI(model_name='gemini-2.5-flash')



ex_name='API 510 - Pressure Vessel Inspector',
sheet_content=('FOR: September 2025, January 2026, and May 2026'
                '- API 510, Pressure Vessel Inspection Code: In-service Inspection, Rating, Repair, and Alteration, 11th Edition, October 2022, Errata 1 (March 2023)'
                '- API Recommended Practice 571, Damage Mechanisms Affecting Fixed Equipment in the Refining Industry, 3rd edition, March 2020 (Sections: 2, 3.3, 3.8, 3.9, 3.11, 3.14, 3.15, 3.17, 3.22, 3.27, 3.35, 3.36, 3.37, 3.46, 3.61, 3.67)'
                '- API Recommended Practice 572, Inspection Practices for Pressure Vessels, 5th Edition, November 2023.'
                '- API Recommended Practice 576, Inspection of Pressure-relieving Devices, 5th Edition, September 2024'
                '- API Recommended Practice 577, Welding Processes, Inspection, and Metallurgy, 3rd Edition, October 2020.'
                '- API Recommended Practice 578, Material Verification Program for New and Existing Assets, 4th edition, February 2023'
                '- ASME, Boiler and Pressure Vessel Code, 2023 Edition:'
                    ' - Section V, Nondestructive Examination, Articles 1, 2, 6, 7 and 23 (Section SE-797 only)'
                    '- Section VIII, Rules for Construction of Pressure Vessels, Division 1; Introduction (U), UG, UW, UCS, Appendices 1-4, 6, 8, and 12'
                    ' - Section IX, Qualification Standard for Welding, Brazing, and Fusing Procedures; (Welding only)'
                '- ASME PCC-2, Repair of Pressure Equipment and Piping, 2022 (Articles: 101, 201, 202, 209, 210, 211, 212, 215, 216, 304, 305, 312, 501, 502)))')


knowledge_content=('API Authorized Pressure Vessel Inspectors must have a broad knowledge base relating to maintenance, inspection, repair, and alteration of pressure vessels. The examination is designed to determine if individuals have such knowledge.'
                        'I. THICKNESS MEASUREMENTS, INSPECTION INTERVALS AND VESSEL INTEGRITY: Corrosion Rates and Inspection Intervals, Joint Efficiencies, Static Head, Internal Pressure, External Pressure, Pressure Testing, Impact Testing, Weld Size for Attachment Welds at Openings, Nozzle Reinforcement.'
                        'II. WELDING PROCEDURE AND QUALIFICATION EVALUATION: Based on ASME Section IX, including Weld Procedure Review (WPS, PQR, WPQ) and general welding requirements from ASME Section VIII, Div. 1 and API 510. Welding processes limited to SMAW, GTAW, GMAW, SAW. Base metals limited to P-No. 1, 3, 4, 5, and 8.'
                        'III. NONDESTRUCTIVE EXAMINATION: Based on ASME Section V, including Article 1 (General), Article 2 (Radiography), Article 6 (Liquid Penetrant), Article 7 (Magnetic Particle - Yoke and Prod only), Article 23 (Ultrasonic Thickness - SE-797 only).'
                        'IV. PRACTICAL KNOWLEDGE - GENERAL & SPECIFIC: Requirements from API 510, API RP 571 (specified sections), API RP 572, API RP 576, API RP 577, API RP 578, and ASME PCC-2 (specified articles).')
 




prompt = GenBookPrompt(ex_name=ex_name, sheet_content=sheet_content, knowledge_content=knowledge_content)

#print(prompt)

#path = 'data/text_file'
path = 'data/response'
os.makedirs(path, exist_ok=True)

serial = len(os.listdir(path=path))

f_path = os.path.join(path, f"response_{serial+1}.txt")
resp = model.invoke(prompt)


                       
print(resp.content)

with open(f_path, 'w') as file:
    file.write(resp.content)"""

"""from dotenv import load_dotenv
from asset.core.process_gemi3_response import get_text
from asset.config.gen_model import LoadGenModel
from asset.core.clear_data import CleanData

import ast
load_dotenv()
model = LoadGenModel()
x = [{'type': 'text', 'text': '```json\n[\n  {\n    "question": "A pressure vessel is currently operating with a 12-year internal inspection interval justified by a documented Risk-Based Inspection (RBI) assessment. According to API 510, 11th Edition, what is the maximum permitted interval for performing the visual external inspection of this vessel?",\n    "options": [\n      {\n        "option": "5 years",\n        "is_correct": true\n      },\n      {\n        "option": "6 years",\n        "is_correct": false\n      },\n      {\n        "option": "10 years",\n        "is_correct": false\n      },\n      {\n        "option": "12 years",\n        "is_correct": false\n      }\n    ],\n    "explanation": "According to API 510, 11th Edition, Section 6.5.1.1, external inspections shall be conducted at least every five years or at the same interval as the required internal or on-stream inspection, whichever is less. Even if the internal inspection interval is extended beyond five years via RBI or low corrosion rates, the visual external inspection remains capped at a maximum 5-year interval."\n  }\n]\n```', 'extras': {'signature': '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'}}]
#res = model.invoke('hi')

cl = CleanData(get_text(x))

print(cl)
print(len(cl))"""

import json

data = json.load(open('120.json', 'r'))

ques = data['text']

ques = ques[:120]

print(ques[119])

