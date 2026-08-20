import os

from groq import Groq, GroqError


class AIClient:
    def __init__(self, user, financial_data):
        self.user = user
        self.financial_data = financial_data
        self.api_key = ""
        self.client = None

    def get_api_key(self):
        if self.api_key:
            print("API Key is already active.\n")
            return self.api_key
        
        env_key = os.environ.get("GROQ_API_KEY")
        if env_key:
            self.api_key = env_key
            print("API Key loaded from environment variables.\n")
            return self.api_key
            
        while True:
            user_input = input("Please enter your GROQ API key: ").strip()
            if user_input:
                self.api_key = user_input
                print("API KEY saved for this session...\n")
                break
            print("Please enter a valid API key.\n")
            
        return self.api_key

    def ai_chat(self):
        if not self.api_key:
            self.get_api_key()

        if not self.api_key:
            print("No valid API Key provided.")
            return

        data = self.financial_data.df
        if data.empty:
            print("No financial data available...")
        else: 
            try:
                self.client = Groq(api_key=self.api_key)
                print("---AI Helper---")
                
                while True:
                    print("Press 5 to close.")
                    prompt = input("Please enter your desire: ").strip()
                    print()
                    
                    if not prompt:
                        print("Invalid prompt.\n")
                        continue
                    elif prompt == "5":
                        print("Closing...\n")
                        break
                    else:
                        processed_data = self.financial_data.df.to_string(index=False)
                        final_prompt = f"{prompt}, using this information: {processed_data}, and this user info: {self.user}"
                        
                        stream = self.client.chat.completions.create(
                            messages=[
                                {
                                    "role": "system",
                                    "content": "you help the user to improve their personal finances"
                                },
                                {
                                    "role": "user",
                                    "content": final_prompt
                                }
                            ],
                            model="llama-3.3-70b-versatile",
                            temperature=0.5,
                            max_completion_tokens=2000,
                            stream=True,
                        )
                        
                        print("---Response---")
                        for chunk in stream:
                            content = chunk.choices[0].delta.content or ""
                            print(content, end="", flush=True)
                        print("\n")
                        
            except GroqError as e:
                print(f"API ERROR: {e}\n")