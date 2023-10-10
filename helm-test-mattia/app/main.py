# noqa: E501 

import os
from tqdm import tqdm
from langchain import PromptTemplate, LLMChain
from typing import List, Dict, Any

from constants import assessment_template, template, question_template
from data_model import initialize_object_from_schema, question_schema, schema
from helpers import load_llm_model, unload_llm_model, setup_llm_pipeline
from scoring import calculate_and_normalize_perplexity, load_model_and_tokenizer
from helpers import categorize_risk, convert_to_json_and_validate
from constants import MEDICAL_RECORD, base_questions, specific_questions



def analyse_document(llm, initial_object, base_questions, specific_questions, context_p):  # noqa: E501 

    print(initial_object)

    for key, question in tqdm(base_questions.items()):

        prompt = PromptTemplate(template=template, input_variables=["question", "context"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        response = llm_chain.run({"question": question, "context": context_p})
        initial_object["general_info"][key] = response

        if key == "treatment_plan":
            prompt = PromptTemplate(template=assessment_template, input_variables=["context"])
            llm_chain = LLMChain(prompt=prompt, llm=llm)
            response = llm_chain.run({"context": response})

            initial_object["general_info"]["meta"]["treatment_assessment"] = response

    for question in tqdm(specific_questions):
        question_item = initialize_object_from_schema(question_schema)

        prompt = PromptTemplate(template=question_template, input_variables=["question","context"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        response = llm_chain.run({"question": question, "context": context_p})

        question_item["question"] = question
        question_item["justification"] = response.split("$$SEPARATOR$$")[1].replace("Answer:", "")
        question_item["answer"] = response.split("$$SEPARATOR$$")[0].replace("Answer:", "").replace("\n", "")

        initial_object["questions"].append(question_item)

    return initial_object


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
