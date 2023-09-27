import pandas as pd
import numpy as np
import json

from database import Database

db = Database()

expert_answer = "Expert Answer"
taster_answer = "Taster Answer"

def str_to_list(str_obj) -> list:
    return json.loads(str_obj)

    
def list_to_df(list) -> pd.DataFrame:
    return pd.DataFrame.from_records(list).dropna(subset=['answer'])
    
class Scorer:

    no_score_questions = db.get_no_score_questions()

    def __init__(self, taster_name, wine_id):
        self.taster_name = taster_name
        self.wine_id = wine_id

    def get_expert_data(self) -> dict:
        return db.get_expert_result(self.wine_id)

    def get_taster_data(self) -> dict:
        return db.get_taster_results(self.taster_name, self.wine_id)

    def get_comparison_df(self):
        result = pd.merge(self.dict_to_df_raw(self.get_expert_data()), 
                          self.dict_to_df_raw(self.get_taster_data()), 
                          on=["Question"], how='outer')
        result = result.rename(columns={"Answer_x": expert_answer, "Answer_y": taster_answer})
        return result
    
    def dict_to_df_raw(self, dict):
        return pd.DataFrame(dict.items(), columns=["Question", "Answer"])
        
    
    def get_score(self):
        answer_summary = self.get_answer_summary()
        total = sum(answer_summary["Total"])
        score = sum(answer_summary["Score"])
        print("score: ")
        print(score)
        print("total: ")
        print(total)
        return int(score / total * 100)
    
    def get_answer_summary(self):
        merged = self.get_comparison_df()

        merged["Key"] = merged.Question.str.split("_").str[0]
        merged = merged.loc[~merged["Key"].isin(db.get_no_score_questions())]
        merged = merged.drop('Key', axis=1)

        not_nested_list_df = merged.loc[(-merged[expert_answer].apply(lambda x: isinstance(x, list))) & 
                                    (-merged[taster_answer].apply(lambda x: isinstance(x, list)))]
        nested_list_df = merged.loc[(merged[expert_answer].apply(lambda x: isinstance(x, list))) | 
                                    (merged[taster_answer].apply(lambda x: isinstance(x, list)))]
        
        nested_list_df['Score'] = nested_list_df.apply(lambda row: count_overlapping_elements(row[expert_answer], 
                                                                                                      row[taster_answer]), axis=1)
        nested_list_df['Total'] = nested_list_df.apply(lambda row: unique_values_in_union(row[expert_answer], 
                                                                                                      row[taster_answer]), axis=1)
        not_nested_list_df["Score"] = (not_nested_list_df[expert_answer] == not_nested_list_df[taster_answer]).astype(int)
        not_nested_list_df.loc[:, "Total"] = 1
        result_df = pd.concat([not_nested_list_df, nested_list_df], axis=0)

        return result_df
    
    def get_all_questions(self) -> pd.DataFrame:
        questionnaire = db.get_questionnaire()
        result_df = pd.DataFrame({'index': [str(index) for index, v in questionnaire.items()],
                'Question': [v['question'] for index, v in questionnaire.items()],
                'Length': [len(v['options']) for index, v in questionnaire.items()]
                })
        return result_df
    
    def get_question_summary(self) -> pd.DataFrame:
        result = self.get_comparison_df()
        result["Key"] = result.Question.str.split("_").str[0]
        questionnaire_dict = db.get_questionnaire_id_to_question()
        questionnaire_df = pd.DataFrame(list(questionnaire_dict.items()), columns=['Key', 'Question Text'])
        result_df = pd.merge(result, questionnaire_df, on=["Key"], how="left")
        return result_df.fillna("-")
    
    def get_summary_taster_view(self)-> pd.DataFrame:
        return self.get_question_summary()[['Question Text', expert_answer, taster_answer]]
    

def count_overlapping_elements(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        set1 = set(list1)
        set2 = set(list2)
        overlap = set1.intersection(set2)
        return len(overlap)
    else:
        # Handle the case where one or both inputs are not iterable (e.g., float)
        return 0

def unique_values_in_union(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        set1 = set(list1)
        set2 = set(list2)
        union = set1.union(set2)
        return len(union)
    elif isinstance(list1, list) and not isinstance(list2, list):
        return len(list1)
    elif not isinstance(list1, list) and isinstance(list2, list):
        return len(list2)
    else:
        return 0