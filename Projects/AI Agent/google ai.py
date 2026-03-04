import google.generativeai as genai

genai.configure(api_key="api")

model = genai.GenerativeModel("gemini-2.5-flash")  # or whichever free model you want
response = model.generate_content("Hello how are you")
print(response.text)
