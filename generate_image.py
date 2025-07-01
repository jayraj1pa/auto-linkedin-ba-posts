import replicate
import os

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def generate_linkedin_image(prompt="A modern illustration of a business analyst analyzing charts and data in a corporate setting, clean and minimal style, white background"):
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

    output = replicate.run(
        "stability-ai/sdxl:latest",
        input={
            "prompt": prompt,
            "width": 768,
            "height": 768,
            "style_preset": "photographic"
        }
    )

    # Download the image
    import requests
    image_url = output[0]
    img_data = requests.get(image_url).content
    with open("linkedin_image.png", "wb") as f:
        f.write(img_data)

    print("🖼️ Image generated and saved as linkedin_image.png")

# TEMP: Test the function
if __name__ == "__main__":
    generate_linkedin_image()
