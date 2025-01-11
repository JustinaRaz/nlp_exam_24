# MSc Cognitive Science - Natural Language Processing
This repository contains the code for the exam project of Natural Language Processing course in Aarhus University.

## Repository organization
```
├── README.md                <- The top-level README for this project
├── data                     <- Folder containing predefined color-specific tasks for the models to be tested on
|   ├── tasks_bert.txt       <- Tasks formatted for BERT models
|   └── tasks_gpt.txt        <- Tasks formatted for GPT models
├── out                      <- Folder containing outputs from the tasks as csv files
|   ├── output_bert.csv      <- csv file containing outputs from BERT base
|   ├── output_bert_l.csv    <- csv file containing outputs from BERT large
|   ├── output_gpt2.csv      <- csv file containing outputs from GPT2
|   └── output_gpt3.csv      <- csv file containing outputs from GPT3
├── src                      <- The main folder for scripts
|   ├── tools.py             <- A script containing functions used for loading tasks and performing masked word prediction for GPT2, GPT3, BERT base and BERT large 
|   └── main.py              <- A script containing the main function to access masked word prediction across models
├── api.txt                  <- Empty txt file for your personal OpenAI API key
├── .gitignore               <- A list of files not uploaded to git
├── requirements.txt         <- A requirements file specifying the required packages
└── run.sh                   <- Script to set up a virtual environment with the requirements from requirements.txt and run main.py 
```
