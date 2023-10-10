# flake8: noqa

MEDICAL_RECORD = """
Medical Record
Pa#ent Name: John Smith
DOB: 06/16/1982
MRN: 456789123
Sex: Male
Chief Complaint
hemorrhoids, new patient
Pa/ent’s Care Team
Primary Care Provider: Name: Care Provider MD Address: 123 Main Street, Cocoa, FL 12345 Phone: (123) 456-
7899 Fax: (123) 456-7899 NPI: 1234567899
Sports Medicine: Name: Sports Medicine Address: 123 Main Street, Cocoa, FL 12345 Phone: (123) 456-7899
Fax: (123) 456-7899 NPI: 1234567899
Patient’s Pharmacies
Pharmacy: Name: Pharmacy Address: 123 Main Street, Cocoa, FL 12345 Phone: (123) 456-7899 Fax: (123) 456-
7899
Vitals
Ht: 6 P 2 in
Wt: 165 lbs
BMI: 21.2
Pulse: 96 bpm
RR: 16
02Sat: 87%
Allergies
• Allergies not reviewed (last reviewed 11/28/2022)
• NKDA
Medica/ons
• Clenpiq 10 rng-3.5 gram-12 gram/160 ml oral solution Take 320 ml by oral route as directed
• diclofenac 1 % topical gel BMI: 21.2 02Sat: 87% 02/10/23 prescribad 11 /28/22 filled · APPLY 2 GRAMS
TO THE AFFECTED AREA(S) TOPICALLY FOUR TIMES A DAY
• meloxicarn 15 mg tablet TAKE ONE TABLET BY MOUTH ONE TIME DAILY
Problems
Reviewed Problems · No known problems
Family History
Family History not reviewed (last reviewed 11/28/2022)
Mother
- Arthritis
- Hypertensive disorder
- Hypercholesterolemia
Father
- Hypertensive disorder
- Congestive heart failure
- Dlabatas mallitus

- Chronic obstructive lung disease
- Arthritis
- Heart disease
Brother
- Congestive heart failure
- Asthma
Social History
Social History not reviewed (last reviewed 11/28/2022)
Ac#vi#es of Dally Living
Are you deaf or do you have serious difficulty hearing?: No
Are you able to walk?: Yes: walks without restric@ons
Do you have transporta@on difficul@es?: No
Diet and Exercise
What type of diet are you following?: Regular
What Is your exercise level?: None
Educa#on and Occupa#on
What is the highest grade or level of school you have completed or the highest degree you have received?:
High school graduate
Are you currently employed?: Yes
What Is your occupation?: Lineman
Advance Directive
Do you have a medical power of attorney?: No
Is blood transfusion acceptable in an emergency?: Yes
Substance Use
Do you or have you eversmoked tobacco?: Currant every day smoker
How much tobacco do you chew?; none
At what age did you start smoking tobacco?: 20
How much tobacco do you smoke?: 1 pack per day
How many years have you smoked tobacco?: 20
What is your level of alcohol consump@on?: None
How many years have you consumed alcohol?: 20
What is your level of caffeine consump@on?: Occasional
Marriage and Sexuality
What is yourrela@onship status?: Married
Are you sexually ac@ve?: Yes
Do you use protec@on during sex?: No
How many children do you have?: 3
Home and Environment
Do you have any pets?: Yes
Are you passively exposed to smoke?: Yes
Lifestyle
Do you feel stressed (tense, restless, nervous, or anxious, or unable to sleep at night)?: Not at all
Do you use your seat belt or car seat rou@nely?: No
PMG Social History
Do you have a supportsystem?: Yes
Domes@c violence history: No

Contracep@on used: Vasectomy
Other tobacco products: None
Living will: No
Educa@on specifics: Public school
Home health; No
Received rabies vaccine in 2002 - travelled to Namibia
Gender Iden#ty and LGBTQ
Iden@ty GenderIden@ty: Choose not to disclose
First name used: John
Sexual orienta@on: Choose not to disclose
Surgical History
Surgical History not reviewed (last reviewed 11/28/2022)
Past Medical History
Patient diagnosed with haemorrhoids in 2009, treated with hydrocortisone cream, and fully resolved

H P I
Pa@ent is a 41 y/o male with history of lateral epicondyli@s who isseen for the first @me at this prac@ce.
Pa@ent never had a colonoscopy. Pa@ent is complaining ofsymptoma@c haemorrhoidstwo months ago, one of
which had ruptured and bled last year. Pa@ent hasfamily history of colon cancer (grandfather on his eigh@es).
Pa@ent denies blood in stool.
ROS
ROS as noted in the HPJ
Physical Exam
Cons#tu#onal: General Appearance: healthy-appearing, well-nourished, and well-developed. Level of Distress:
NAO. Ambula@on: ambula@ng normally.
Psychiatric: Insight: good Judgement. Mental Status: ac@ve and alert. Orienta@on: to @me, place, and person.
Memory: recent memory normal.
Abdomen: Bowel Sounds: normal. Inspec@on and Palpa@on: no tenderness, guarding, masses, rebound
tenderness, or CVA tenderness and soP and non-distended. Liver: non-tender and no hepatomegaly. Spleen:
non-tender and no splenomegaly. Hernia: none palpable.
Assessment/ Plan
1. Haemorrhoids
Pa@ent is asymptoma@c right know. I advised to seek evalua@on for banding procedure aPer colonoscopy
(depending on evalua@on done)
K64.9: Unspecified haemorrhoids.
2. Screening for malignant neoplasm of colon
Pa@ent will have colonoscopy with average risk. Consentsigned. Risks associated with this procedure such as
bleeding, Infec@on and perfora@on were discussed with the pa@ent.
Z12.11: Encounter for screening for malignant neoplasm of colon
• Clenpiq 10 mg-3.5 gram-12 gram/160 ml oral solu#on - Take 320 ml by oral route as directed Qty:
(320) ml Refills: 0
3. Family history of cancer of colon-

Pa@ent has family history of colon cancer (grandfather on his eigh@es) Z80.0: Family history of malignant
neoplasm of diges@ve organs
Haematochezia
4. Pa@ent has BRBPR last year
K92.1: Melena
"""



template = """
[INST] Answer each question in no more then 20 words.. Example:
"Yes Because of advancements in technology." [/INST]
Context: {context}
Question: {question}
"""

question_template = """
[INST] Please provide two distinct parts for each question's answer. First, state 'Yes' or 'No', then follow it with the string "$$SEPARATOR$$" and provide a justification for your 'Yes' or 'No' answer. Separate the prompt from the answer with the string "%%SEPARATOR%%". Example:
%%SEPARATOR%%
"Yes $$SEPARATOR$$ Because of advancements in technology." [/INST]
Context: {context}.
Question: {question}
"""

assessment_template = """
[INST] given this doctor treatment plan, classify it as "mild", "average", "aggressive". Only answer with one word. [/INST]
Context: {context}
 """

base_questions = {
  "chief_complaint": "What is the patient main complaint?",
  "treatment_plan": "what treatment plan is the doctor suggesting?",
  "allergies": "Does the patient have allergies and if so, which ones?",
  "preexisting_medications": "Is the patient on medications?"
}

specific_questions = [
  "Does the patient have a family history of colon cancer in their first-degree relatives?",
  "Has the patient experienced minimal bright red blood per rectum?",
  "Has the patient had significant loss of blood?",
  "Does the patient have a history of skin problems?",
  "Has the patient used hydrocortisone cream for the haemorrhoids that they are recently experiencing?",
  "Were any high risk traits found on the patient’s genetic test?",
  "Has the patient had a colonoscopy in the last 5 years?",
  "Has the patient had any recent foreign travel?",
  "How long has the patient been known to healthcare services?"
]


specific_questions = [
  "Does the patient have a family history of colon cancer in their first-degree relatives?",
  "Has the patient experienced minimal bright red blood per rectum?"
]