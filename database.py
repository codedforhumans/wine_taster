import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

from questionnaire import questionnaire


class Database:
    cred = credentials.Certificate("vyn-taster-firebase-adminsdk-hn7hz-4293134ee0.json")

    # Application Default credentials are automatically created.
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    user_collection_name = "users"
    user_input_collection_name = "input"
    wine_id_collection_name = "wine_id"
    wine_id_document_name = "wines"

    def __init__(self):
        pass

    def load_questionnaire(self) -> None:
        for key, value in questionnaire.items():
            self.db.collection("questionnaire").document(key).set(value)

    def get_questionnaire(self) -> dict:
        docs = self.db.collection("questionnaire").stream()
        result_dict = {}
        for doc in docs:
            result_dict[doc.id] = doc.to_dict()
        return result_dict

    def submit_user_input(self, name, phone, type, drink_name, dict_submit) -> None:
        
        doc_ref = self.db.collection(self.user_input_collection_name).document(name)
        doc_ref.set({drink_name: {"type": type, "result": dict_submit}}, merge = True)

    def add_user(self, name, phone, type) -> None:
        doc_ref = self.db.collection(self.user_collection_name).document(name)
        doc_ref.set({"phone": phone, "type": type}, merge = True)

    def stream_all_user_info(self):
        docs = self.db.collection(self.user_collection_name).stream()
        result_dict = {}
        for doc in docs:
            result_dict[doc.id] = {"phone": doc.to_dict()["phone"], "type": doc.to_dict()["type"]}
        return result_dict
    
    def user_present(self, name, phone) -> bool:
        doc_ref = self.db.collection(self.user_collection_name).document(name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            if doc_dict["phone"] == phone:
                return True
        return False

    def user_present_add_otherwise(self, name, phone, type) -> None:
        if not self.user_present(name, phone):
            self.add_user(name, phone, type)

    def get_wine_ids(self):
        doc_ref = self.db.collection(self.wine_id_collection_name).document(self.wine_id_document_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            return list(doc_dict.keys())
        
    def get_wine_names(self):
        doc_ref = self.db.collection(self.wine_id_collection_name).document(self.wine_id_document_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            return list(doc_dict.values())

        

        




# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

# doc_ref = db.collection("users").document("aturing")
# doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

# users_ref = db.collection("users")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")