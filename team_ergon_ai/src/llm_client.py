import requests
import json


class LocalLLMClient:
    def __init__(self, host="http://localhost:11434", model="llama3.2:3b"):
        self.host = host
        self.model = model
        self.generate_url = f"{self.host}/api/generate"
        
    def is_alive(self) -> bool:
        try:
            response = requests.get(self.host, timeout=2)
            return response.status_code == 200
        
        except requests.ConnectionError:
            return False
        
    def generate(self, prompt: str, system: str = "", temperature: float = 0.0) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {"temperature": temperature, "top_p": 0.1}
        }
        
        try:
            response = requests.post(self.generate_url, json=payload, timeout=60)
            if response.status_code != 200:
                return ""
            return response.json().get("response", "").strip()
        except requests.ConnectionError:
            return ""
    
    def stream_generate(self, prompt: str, system: str = "", temperature: float = 0.0) -> str:
         payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": True,
            "options": {"temperature": temperature, "top_p": 0.1}
        }
         
         try:
            with requests.post(self.generate_url, json=payload, stream=True, timeout=60) as r:
                for line in r.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        yield chunk.get("response", "")
        
         except requests.ConnectionError:
            return ""
                
                
if __name__ == "__main__":
    client = LocalLLMClient()
    
    if client.is_alive():
        print("Local Ollama Daemon is alive")
        response = client.generate("What is permeability in reservoir rocks?", system="Answer in 20 words or less.")
        
        print(response)
        
    else:
        print("Local LLM is not running yet. Chill")