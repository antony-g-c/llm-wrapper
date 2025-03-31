from transformers import pipeline

class LLMWrapper:
    def __init__(self, model_name="facebook/opt-1.3b"):
        """
        Initialize the Hugging Face pipeline with a specific model.
        :param model_name: The Hugging Face model name to use (e.g., "facebook/opt-1.3b").
        """
        self.available_models = [
            "facebook/opt-1.3b",  # Example: open-source, smaller model
            "gpt2",               # GPT-2 (small version)
            "EleutherAI/gpt-neo-2.7B",  # A larger GPT-Neo model
            "gpt-3.5-turbo",      # GPT-3.5 from OpenAI (requires API key)
        ]
        if model_name not in self.available_models:
            raise ValueError(f"Model {model_name} not in the available models list.")
        
        self.model_name = model_name
        self.pipeline = pipeline("text-generation", model=self.model_name)

    def list_available_models(self):
        """
        List all available models that can be used in the wrapper.
        """
        print("Available models:")
        for model in self.available_models:
            print(f"- {model}")

    def switch_model(self, model_name):
        """
        Switch the current model to a new one from the available models.
        :param model_name: The new model to load (e.g., "gpt2", "facebook/opt-1.3b").
        """
        if model_name not in self.available_models:
            raise ValueError(f"Model {model_name} is not available. Please choose from the list.")
        self.model_name = model_name
        self.pipeline = pipeline("text-generation", model=self.model_name)
        print(f"Model switched to {model_name}")

    def generate(self, prompt, max_length=50):
        """
        Generate text based on a given prompt using the current model.
        :param prompt: The input prompt for the model.
        :param max_length: The max length of the generated response.
        :return: The generated text.
        """
        response = self.pipeline(prompt, max_length=max_length, truncation=True)
        return response[0]["generated_text"]

# Example usage (for testing)
if __name__ == "__main__":
    # Initialize with a default model (e.g., facebook/opt-1.3b)
    llm = LLMWrapper()
    print("Generated text with the default model:")
    print(llm.generate("Explain the importance of AI in healthcare."))
    
    # List available models
    print("\nListing available models:")
    llm.list_available_models()
    
    # Switch model to GPT-2 and generate text
    llm.switch_model("gpt2")
    print("\nGenerated text after switching to GPT-2:")
    print(llm.generate("Explain the importance of AI in healthcare."))
