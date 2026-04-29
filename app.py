
 
import gradio as gr
import os, requests, json

API_BASE_URL = "https://api.ithu.tw/v1"
MODEL_NAME = "gpt-oss-120b"

def greet(name):
    # return "Hello " + name + "!"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": "gpt-oss-120b",
        "messages": [
            {"role": "system", "content": "You are a Chinese teacher. Explain the input statement in Traditional Chinese."},
            {"role": "user", "content": name}
        ]
    }

    response = requests.post(
        f"{API_BASE_URL}/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"請求失敗，狀態碼: {response.status_code}")
        

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()  
