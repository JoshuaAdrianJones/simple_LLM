from ollama import chat
from pydantic import BaseModel


class GeneralOutput(BaseModel):
    content: str


models = {
    "qwen": "qwen3:8b",
    "gemma": "gemma3:12b",
    "llama": "llama3.2:3b-instruct-fp16",
    "embed": "mxbai-embed-large:latest"
}


def generate_general_output(model, model_temperature, prompt, system_prompt):
    max_tokens = 4096
    num_ctx = 4096
    response = chat(
        model=model,
        messages=[
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{prompt}"},
        ],
        format=GeneralOutput.model_json_schema(),
        options={
            "temperature": model_temperature,
            "num_predict": max_tokens,
            "num_ctx": num_ctx,
        },
    )
    # Create GeneralOutput object directly instead of trying to parse JSON
    return GeneralOutput.model_validate_json(response.message.content)


msg = generate_general_output(models["qwen"], 0.7, "What is the capital of France?", "You are a helpful assistant.")
print(msg.content)  # Should print the capital of France
