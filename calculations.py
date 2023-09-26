import pandas as pd
import numpy as np
import json

from questionnaire import questionnaire

expert_answer = "Expert Answer"
taster_answer = "Taster Answer"

def str_to_list(str_obj) -> list:
    return json.loads(str_obj)

def get_expert_data() -> list:
    with open('expert.json') as f:
        load = json.load(f)
        result = str_to_list(load['results'])
        return result
    

def get_taster_data() -> list:
    with open('taster.json') as f:
        load = json.load(f)
        result = str_to_list(load['results'])
        return result
    
def list_to_df(list) -> pd.DataFrame:
    return pd.DataFrame.from_records(list).dropna(subset=['answer'])
    
class Scorer:
    def __init__(self):
        self.expert_data = list_to_df(get_expert_data())
        self.taster_data = list_to_df(get_taster_data())

    def get_comparison_df(self):
        result = pd.merge(self.expert_data, self.taster_data, on=["index", "type", "additional"], how='outer')
        result = result.rename(columns={"answer_x": expert_answer, "answer_y": taster_answer})
        return result
    
    def get_score(self):
        total = self.get_total_answer_count()
        correct_answer_index_list = self.get_correct_ans_index()
        return int(len(correct_answer_index_list) / total * 100)
    
    def get_correct_ans_index(self):
        merged = self.get_comparison_df()
        boolean_match = merged[expert_answer] == merged[taster_answer]
        correct_answer_index_list = boolean_match.loc[boolean_match == True].index.to_list()
        return correct_answer_index_list
    
    def get_total_answer_count(self):
        merged = self.get_comparison_df()
        total = len(merged)
        return total
    
    def get_all_questions(self) -> pd.DataFrame:
        result_df = pd.DataFrame({'index': [str(index) for index, v in questionnaire.items()],
                'Question': [v['question'] for index, v in questionnaire.items()],
                'Length': [len(v['options']) for index, v in questionnaire.items()]
                })
        return result_df
    
    def get_question_summary(self) -> pd.DataFrame:
        result = pd.merge(self.get_comparison_df(), self.get_all_questions(), on = 'index', how='left')
        # result.loc[result['type'] == 'slider', 'Expert Answer'] = "Matt"
        # get_slider_q = result.loc[result['type'] == 'slider'].question.to_list()
        # questionnaire
        return result
    
    def get_summary_taster_view(self)-> pd.DataFrame:
        return self.get_question_summary()[['Question', expert_answer, taster_answer]]