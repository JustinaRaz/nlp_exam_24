# MSc Cognitive Science - Natural Language Processing
This repository contains the code for the exam project of Natural Language Processing course in Aarhus University.

## Repository organization
```
├── crt_questions              <- 2 text files with the CRT questions.
|   ├── alternative_CRT.txt    <- 10 CRT questions (non-mathematical nature).
|   └── original_CRT.txt       <- 3 CRT questions (mathematical nature).
├── emissions                  <- Contains calculations of CO2 emissions produced by running each LM.
├── output                     <- Contains plots [emissions] and raw output of all GPT-2 LMs.    
├── README.md                  <- Brief project description.                    
├── emissions.ipynb            <- Notebook for plotting "emissions" results.                
├── functions.py               <- Necessary pre-defined functions [reasoning condition].
├── functions_no_reasoning.py  <- Necessary pre-defined functions [no reasoning condition].          
├── main.py                    <- Main script [reasoning condition].
├── main_no_reasoning.py       <- Main script [no reasoning condition].
├── requirements.txt           <- Necessary libraries for running the code.
└── setup.sh                   <- Script for creating virtual environment and installing necessary libraries.
```

## To reproduce

Follow the steps below to reproduce the results.

1. Open the terminal and locate the folder with all repository files:
    ```
    cd path_to_folder
    ```
3. In the terminal, run the following command to install the required packages and set up the virtual environment:
    ```
    bash setup.sh
    ```
4. Activate virtual environment:
   ```
   source ./env/bin/activate
   ```
5. Run the code [for reasoning condition]:
   ```
   python main -lm __ -crt __
   ```
   
