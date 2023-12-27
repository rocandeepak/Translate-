from google.cloud import translate_v2

def translate_recipe(recipe_text, target_language='ta'):
    # Set your Google Cloud project credentials before using the API
    # Replace 'YOUR_PROJECT_KEY' with your actual project key
    # See Google Cloud documentation for more details: https://cloud.google.com/translate/docs/quickstart
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

    # Create a Translate client
    translate_client = translate_v2.Client()

    # Translate the recipe text to the target language
    result = translate_client.translate(recipe_text, target_language=target_language)

    # Return the translated text
    return result['input'], result['translatedText']

# Example usage
recipe_text = "Mix flour, sugar, and eggs. Bake at 350 degrees for 30 minutes."
translated_input, translated_text = translate_recipe(recipe_text)

print(f"Original Recipe: {translated_input}")
print(f"Translated Recipe (Tamil): {translated_text}")