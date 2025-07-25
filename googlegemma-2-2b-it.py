import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="nebius",
    api_key='Your_API_Key', #paste your own api key
)

completion = client.chat.completions.create(
    model="google/gemma-2-2b-it",
    messages=[
        {
            "role": "user",
            "content": "Any Query" #ask any query you want
        }
    ],
    temperature=0.1
)

print(completion.choices[0].message)
