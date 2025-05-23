import requests
from config import HF_API_KEY

MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

headers = {
"Authorization": f"Bearer {HF_API_KEY}"}

def caption_single_image():
    image_source = "test.jpg" # Hardcoded filename
    try:
        with open(image_source, "rb") as f:
            image_bytes = f.read()
    except Exception as e:
        print(f"Could not load image from {image_source}.\nError: {e}")
        return

    response = requests.post(API_URL, headers=headers, data=image_bytes)
    result = response.json()

    if isinstance(result, dict) and "error" in result:
        print(f"[Error] {result['error']}")
        return

    caption = result[0].get("generated_text", "No caption found.")
    print("Image:", image_source)
    print("Caption:", caption)

def main():
    caption_single_image()

if __name__ == "__main__":
    main()