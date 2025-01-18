import transformers 
from transformers import AutoTokenizer, pipeline, set_seed
import torch
import os
import functions
from codecarbon import EmissionsTracker
import argparse


def inputs():
    parser = argparse.ArgumentParser(description = "A Python script that tests GPT-2 language models' performance on mathematical and non-mathematical CRT task.")
    parser.add_argument("-lm",
                        "--language_model",
                        type = str,
                        required = True,
                        choices = ["small", "medium", "large", "xlarge"],
                        help = "GPT-2 language model that should be tested.")
    parser.add_argument("-crt",
                        "--crt_type",
                        type = str,
                        required = True,
                        choices = ["original", "alternative"],
                        help = "The type of CRT for the model to perform. Either original or alternative.")
    args = parser.parse_args()
    return args

def main():

    # Defining paths to the models:

    gpt2_small = "openai-community/gpt2"
    gpt2_medium = "openai-community/gpt2-medium"
    gpt2_large = "openai-community/gpt2-large"
    gpt2_extra_large = "openai-community/gpt2-xl"

    tracker = EmissionsTracker(output_file = "emissions.csv", output_dir = "emissions/")
    tracker.start()

    args = inputs()
    language_m = args.language_model
    crt_test = args.crt_type

    # Finding the model to load:

    if language_m == "small":
        model_of_choice = gpt2_small
    elif language_m == "medium":
        model_of_choice = gpt2_medium
    elif language_m == "large":
        model_of_choice = gpt2_large
    elif language_m == "xlarge":
        model_of_choice = gpt2_extra_large

    tokenizer = AutoTokenizer.from_pretrained(model_of_choice)

    response_generator = pipeline(
    "text-generation",
    model = model_of_choice,
    torch_dtype = torch.float16,
    temperature = 0.5,  
    max_new_tokens = 100)

    # Finding correct CRT test:

    if crt_test == "original":
        file = "original_CRT.txt"
    elif crt_test == "alternative":
        file = "alternative_CRT.txt"

    qs = functions.load_CRT(file)

    print("{} CRT task is being performed by GPT-2 {} model. It will take a while.".format(crt_test, language_m))

    tracker.start_task("{}_CRT_using_GPT-2_{}".format(crt_test, language_m))

    # TASK
    final_responses = functions.CRT(response_generator, qs)

    tracker.stop_task("{}_CRT_using_GPT-2_{}".format(crt_test, language_m))

    print("Saving the output...")

    functions.save_output("{}_CRT_GPT-2_{}".format(crt_test, language_m), final_responses)

    tracker.stop()
if __name__ == "__main__":
    main()