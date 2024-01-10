LLM_MAPPING = {
    "GPT_3_5_TURBO_16K_0613": "gpt-3.5-turbo-16k-0613",
    "GPT_3_5_TURBO_0613": "gpt-3.5-turbo-0613",
    "GPT_3_5_TURBO_1106": "gpt-3.5-turbo-1106",
    "GPT_4_0613": "gpt-4-0613",
    "GPT_4_32K_0613": "gpt-4-32k-0613",
    "GPT_4_1106_PREVIEW": "gpt-4-1106-preview",
    "MISTRAL_7B_INSTRUCT_V01": "huggingface/mistralai/Mistral-7B-Instruct-v0.1",
    "MIXTRAL_8X7B_INSTRUCT_V01": "huggingface/mistralai/Mixtral-8x7B-Instruct-v0.1",
}

LLM_PROVIDER_MAPPING = {
    "OPENAI": [
        "GPT_3_5_TURBO_16K_0613",
        "GPT_3_5_TURBO_0613",
        "GPT_3_5_TURBO_1106",
        "GPT_4_0613",
        "GPT_4_32K_0613",
        "GPT_4_1106_PREVIEW",
    ],
    "HUGGINGFACE": ["MISTRAL_7B_INSTRUCT_V01", "MIXTRAL_8X7B_INSTRUCT_V01"],
}
