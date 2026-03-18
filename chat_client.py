from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

istoric_mesaje = []

print("=== Chatbot Local (Ollama) ===")
print("Scrie 'exit' pentru a închide.\n")

while True:
    user_input = input("Tu: ")
    if user_input.lower() == 'exit':
        break

    istoric_mesaje.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="tinyllama", 
        messages=istoric_mesaje
    )

    ai_response = response.choices[0].message.content
    print(f"AI: {ai_response}\n")

    istoric_mesaje.append({"role": "assistant", "content": ai_response})
