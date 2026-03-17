import time
import firebase_admin
from firebase_admin import firestore, credentials
import requests # Para a API do Google Fit

# 1. Ligar ao Firebase
cred = credentials.Certificate("chave-projeto.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def buscar_e_enviar():
    while True:
        # 2. Pedir dados ao Google Fit (exemplo simplificado)
        # Aqui usarias o teu token OAuth obtido no Google Cloud
        passos_atuais = requests.get("https://www.googleapis.com/fitness/v1/users/me/dataset/...", headers=headers).json()
        
        # 3. Guardar no Firebase
        doc_ref = db.collection('monitorizacao').document('utilizador_01')
        doc_ref.set({
            'passos': passos_atuais,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        
        print(f"Dados atualizados: {passos_atuais} passos.")
        time.sleep(30) # Espera 30 segundos antes de pedir outra vez

buscar_e_enviar()