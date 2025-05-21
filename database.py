import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("rovads\rovads-ai-firebase-adminsdk-fbsvc-9ec00012e1.json")
firebase_admin.initialize_app(cred)
