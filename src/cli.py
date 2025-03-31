import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import argparse
from llm_wrapper import LLMWrapper

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Generate text using Hugging Face models.")
    parser.add_argument("--model", type=str, default="facebook/opt-1.3b", choices=[
        "facebook/opt-1.3b", "gpt2", "EleutherAI/gpt-neo-2.7B", "gpt-3.5-turbo"], 
        help="Choose the model to use for text generation."
    )
    parser.add_argument("--prompt", type=str, required=True, help="The prompt text to generate from.")
    parser.add_argument("--max_length", type=int, default=50, help="Maximum length of the generated text.")

    # Parse arguments
    args = parser.parse_args()

    # Initialize LLMWrapper with the selected model
    llm = LLMWrapper(model_name=args.model)
    print(f"Generating text with {args.model}:")
    
    # Generate and display the result
    generated_text = llm.generate(args.prompt, max_length=args.max_length)
    print(f"\nGenerated Text:\n{generated_text}")

if __name__ == "__main__":
    main()
