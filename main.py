from fastapi import FastAPI
import google.generativeai as genai
from config import settings

app = FastAPI()


@app.get("/prompt")
def get_gemini(prompt: str):
    # gemini set api key and model
    genai.configure(api_key=settings.GEMINI_KEY)
    model = genai.GenerativeModel(settings.GEMINI_MODEL)

    # set prompt input
    promptInput= f"""
                {prompt}
                Langsung jawab singkat"""
    
    # send prompt and get response
    response = model.generate_content(
        promptInput,
        generation_config={
            "temperature": 0.4 #set temprature from 0 to 2, set 0.4 for less randomness, more focused
        }
    )
    return {"text": response.text}