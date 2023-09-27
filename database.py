import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from natsort import natsorted

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
    
    def get_questionnaire_id_to_question(self) -> dict:
        return {k: v["question"] for k, v in self.get_questionnaire().items()}

    def submit_user_input(self, name, type, drink_name, dict_submit, wine_id = None) -> None:
        
        doc_ref = self.db.collection(self.user_input_collection_name).document(name)
        doc_ref.set({drink_name: {"type": type, "result": dict_submit, "wine_id": wine_id}}, merge = True)

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
            sort_result = natsorted(list(doc_dict.keys()))
            return sort_result
    
    def get_wine_mapping(self):
        doc_ref = self.db.collection(self.wine_id_collection_name).document(self.wine_id_document_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            return doc_dict
        
    def get_wine_names(self):
        doc_ref = self.db.collection(self.wine_id_collection_name).document(self.wine_id_document_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            return list(doc_dict.values())
    
    def get_wine_id_from_name(self, name):
        mapping_dict = self.get_wine_mapping()
        return get_key(mapping_dict, name)
    
    def get_expert_result(self, wine_id):
        name = "tamara"
        doc_ref = self.db.collection(self.user_input_collection_name).document(name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            for wine_name, value in doc_dict.items():
                if value["wine_id"] == wine_id:
                    return value["result"]
    
    def get_taster_results(self, taster_name, wine_id):
        doc_ref = self.db.collection(self.user_input_collection_name).document(taster_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            for key, value in doc_dict.items():
                if key == wine_id:
                    return value["result"]
                
    def get_no_score_questions(self) -> list:
        full_questionnaire = self.get_questionnaire()
        question_numbers = []
        for q_id, value in full_questionnaire.items():
            if not value["scored"]:
                question_numbers += [q_id]
        return question_numbers
        
        
def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

        

        




# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

# doc_ref = db.collection("users").document("aturing")
# doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

# users_ref = db.collection("users")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")