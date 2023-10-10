# noqa: E501 

import os
from tqdm import tqdm
from typing import List, Dict, Any

from data_model import initialize_object_from_schema, question_schema, schema
from helpers import load_llm_model, unload_llm_model, setup_llm_pipeline
from scoring import calculate_and_normalize_perplexity, load_model_and_tokenizer
from helpers import categorize_risk, convert_to_json_and_validate, analyse_document
from constants import MEDICAL_RECORD, base_questions, specific_questions


def main_pipeline(
    medical_text: str,
    schema: Dict[str, Any],
    base_questions: List[Dict[str, Any]],
    specific_questions: List[Dict[str, Any]]
) -> Dict[str, Any]:
    try:
        use_quantization = not os.environ.get("DISABLE_QUANTIZATION", False)

        model_id_1 = "mistralai/Mistral-7B-Instruct-v0.1"

        # Initialize DTO from schema
        dto = initialize_object_from_schema(schema)

        # Load first LLM model and analyze document
        model, tokenizer = load_llm_model(model_id_1, use_quantization=False)
        llm = setup_llm_pipeline(model, tokenizer)
        dto = analyse_document(llm, dto, base_questions, specific_questions, medical_text)

        confidence = calculate_and_normalize_perplexity(load_model_and_tokenizer(dto["questions"]))
        dto["questions"] = confidence

        unload_llm_model(model)


        dto["general_info"]["meta"]["risk_profile"] = categorize_risk(dto)

        return convert_to_json_and_validate(dto)

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


# Run the pipeline
result = main_pipeline(MEDICAL_RECORD, schema, base_questions, specific_questions)
print("Pipeline result:", result)
