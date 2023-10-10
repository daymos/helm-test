
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def load_model_and_tokenizer(questions_list):
    global model, tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    return questions_list


def unload_model_and_tokenizer(questions_list):
    global model, tokenizer
    del model
    del tokenizer
    model = None  # noqa: F841
    tokenizer = None  # noqa: F841
    torch.cuda.empty_cache()
    return questions_list


def calculate_and_normalize_perplexity(questions_list):
    if model is None or tokenizer is None:
        print("Model and tokenizer are not loaded. Please load them first.")
        return

    for item in questions_list:
        if not isinstance(item, dict):
            print(f"Skipping item {item} because it's not a dictionary")
            continue

        if "question" not in item or "justification" not in item:
            print(f"Skipping item {item} because it lacks required keys")
            continue

            question = item["question"]
            justification = item["justification"]

            text = question + " " + justification
            input_ids = tokenizer.encode(text, return_tensors="pt")

            with torch.no_grad():
                output = model(input_ids, labels=input_ids)
                log_likelihood = output.loss

            perplexity = torch.exp(log_likelihood).item()

        # Normalize perplexity
        max_perplexity = 500
        perplexity = min(max(perplexity, 1), max_perplexity)
        normalized_score = 1 + 9 * ((perplexity - 1) / (max_perplexity - 1))
        inverted_score = 11 - normalized_score

        # Update confidence_score
        item["confidence_score"] = int(round(inverted_score))

    return questions_list
