import transformers 
from transformers import AutoTokenizer, pipeline, set_seed
import torch
import os


def load_CRT(file_name):

    """
    Function that loads CRT questions from the .txt file.

    Input: file name (.txt).
    Output: a list of strings, where each string represent a CRT question.
    """

    file_path = os.path.join("crt_questions", file_name)
    with open(file_path) as file:
        rows = []
        for question in file:
            cleaned_question = question.rstrip()  
            rows.append(cleaned_question)
    
    return rows

def CRT(generator, text):

    # Defining text for the task:

    reasoning = " Let’s think step by step to answer this question. "
    prefix = "Question: "
    suffix = " Answer: "

    answers = []
    for question in text:
        prompt = reasoning + prefix + question + suffix
        set_seed(2000)
        response = generator(prompt) 
        answers.append(response[0]['generated_text'])
    return answers


def save_output(file_name, variable):
    
    with open("output/" + file_name, "w") as file:
        for line in variable:
            file.write(line + "\n")

