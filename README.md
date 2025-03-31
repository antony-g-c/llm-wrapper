# LLM Wrapper

A simple wrapper for interacting with Large Language Models (LLMs) using Hugging Face's `transformers` library. This project demonstrates how to integrate an LLM into a web interface using FastAPI. The wrapper allows you to generate text based on a user-provided prompt.

## Features

- Easy integration with Hugging Face's pre-trained models.
- Web interface using FastAPI for generating text from a user input prompt.
- Configurable text generation with options like `max_length`.
- Example implementation with the `gpt2` model (you can choose other models too).

## Technologies Used

- **Python**: Programming language.
- **FastAPI**: For building the web interface.
- **Hugging Face Transformers**: To interact with pre-trained language models like GPT-2.
- **Uvicorn**: For running the FastAPI app.
- **Git**: Version control.

## Installation

### 1. Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/antony-g-c/llm-wrapper.git
cd llm-wrapper
