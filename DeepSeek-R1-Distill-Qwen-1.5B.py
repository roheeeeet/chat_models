import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="nscale",
    api_key='Use_your_own_api_key', #Use Your Own API Key here
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    messages=[
        {
            "role": "user",
            "content": "Write a short poem on the Beauty of learning"
        }
    ],
    temperature=0.7
)

print(completion.choices[0].message)
