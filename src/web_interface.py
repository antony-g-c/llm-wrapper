import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from src.llm_wrapper import LLMWrapper  # Corrected import



app = FastAPI()

# Initialize the LLMWrapper with a default model
llm = LLMWrapper(model_name="facebook/opt-1.3b")

@app.get("/", response_class=HTMLResponse)
async def home():
    # HTML for the dropdown and input fields
    return """
        <html>
            <body>
                <h2>Text Generation using Hugging Face Models</h2>
                <form action="/generate/" method="post">
                    <label for="model">Choose a model:</label>
                    <select name="model" id="model">
                        <option value="facebook/opt-1.3b">facebook/opt-1.3b</option>
                        <option value="gpt2">gpt2</option>
                        <option value="EleutherAI/gpt-neo-2.7B">EleutherAI/gpt-neo-2.7B</option>
                        <option value="gpt-3.5-turbo">gpt-3.5-turbo</option>
                    </select><br><br>
                    
                    <label for="prompt">Enter your prompt:</label><br>
                    <textarea name="prompt" rows="4" cols="50" required></textarea><br><br>

                    <label for="max_length">Max Length:</label>
                    <input type="number" name="max_length" value="50"><br><br>

                    <input type="submit" value="Generate Text">
                </form>
            </body>
        </html>
    """

@app.post("/generate/", response_class=HTMLResponse)
async def generate(model: str = Form(...), prompt: str = Form(...), max_length: int = Form(50)):
    # Switch model based on user input
    llm.switch_model(model)
    
    # Generate the text
    generated_text = llm.generate(prompt, max_length)
    
    return f"""
        <html>
            <body>
                <h2>Generated Text</h2>
                <p><strong>Model:</strong> {model}</p>
                <p><strong>Prompt:</strong> {prompt}</p>
                <p><strong>Generated Text:</strong></p>
                <pre>{generated_text}</pre>
                <br><br>
                <a href="/">Go back</a>
            </body>
        </html>
    """
