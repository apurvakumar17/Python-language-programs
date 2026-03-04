import google.generativeai as genai

genai.configure(api_key="AIzaSyBSonnWlAMSWwrFGJ8pq1rjUI4j88iifnU")

model = genai.GenerativeModel("gemini-2.5-flash")  # or whichever free model you want
response = model.generate_content("Hello how are you")
print(response.text)