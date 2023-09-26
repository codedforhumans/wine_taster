import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

from questionnaire import questionnaire


class Database:
    cred = credentials.Certificate("vyn-taster-firebase-adminsdk-hn7hz-4293134ee0.json")

    # Application Default credentials are automatically created.
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    user_collection_name = "test_users"
    user_input_collection_name = "taster_input_test"

    def __init__(self):
        pass

    def load_questionnaire(self) -> None:
        for key, value in questionnaire.items():
            self.db.collection("questionnaire").document(key).set(value)

    def submit_user_input(self, name, email, type, drink_name, input_list) -> None:
        
        doc_ref = self.db.collection(self.user_input_collection_name).document(name)
        doc_ref.set({"email": email, "type": type})
        doc_ref_subset = doc_ref.collection("input").document(drink_name)
        for i in len(input_list):
            index = input_list[i]["index"]
            answer = input_list[i]["answer"]
            doc_ref_subset.set({index: answer})

    def add_user(self, name, email, type) -> None:
        doc_ref = self.db.collection(self.user_collection_name).document(name)
        doc_ref.set({"email": email, "type": type})
    
    def user_present(self, name, email) -> bool:
        doc_ref = self.db.collection(self.user_collection_name).document(name)
        doc = doc_ref.get()
        if doc.exists:
            doct_dict = doc.to_dict()
            if doct_dict["email"] == email:
                return True
        return False

    def user_present_add_otherwise(self, name, email, type) -> None:
        if not self.user_present(name, email):
            self.add_user(name, email, type)

        




# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

# doc_ref = db.collection("users").document("aturing")
# doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

# users_ref = db.collection("users")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")