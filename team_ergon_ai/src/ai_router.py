import os
import requests
from llm_client import LocalLLMClient
from dotenv import load_dotenv
load_dotenv()


class AIRouter:
    def __init__(self):
        self.local_client = LocalLLMClient()
        
    
    def generate(self, prompt: str, system:str = "") -> str:
        # Check if local llm is alive. Otherwise, use gemini.
        if self.local_client.is_alive():
            print("[+] Using local LLM")
            response = self.local_client.generate(prompt, system)
            if response:
                return response
        
        print("[!] Local LLM not available, using Gemini")
        return self.generateWithGemini(prompt, system)
            
    def generateWithGemini(self, prompt: str, system:str = "") -> str:
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            print("[!] Gemini API Key not set")
            return ""
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

        payload = {
            "contents":
            [
                {"parts": 
                    [
                        {"text":prompt}
                    ]
                }
            ]
        }
        
        if system:
            payload["systemInstruction"] = {
                "parts": 
                [
                    {"text": system}
                ]
            }

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            else:
                print(f"[!] Gemini API Error: {response.status_code} - {response.text}")
                return ""
        
        except requests.RequestException as e:
            print(f"[!] Network error contacting Gemini: {e}")
            return ""
        
            
            
        
    
if __name__ == "__main__":
    client = AIRouter()
    print(client.generate("Hello"))
    