def chatbot(input_text):
  input_text = input_text.lower()

  rules_responses = {
      "hi": "Hello! How can I assist you today?",
      "how are you": "I'm your bot, but thanks for asking!",
      "what is your name": "I'm a chatbot.",
      "bye": "Goodbye! Have a great day!",
  }

  for rule, response in rules_responses.items():
      if rule in input_text:
          return response

  return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
  print("Welcome to the Simple Chatbot!")
  print("You can start chatting. Type 'bye' to exit.")

  while True:
      user_input = input("You: ")
      if user_input.lower() == 'bye':
          print("Chatbot: Goodbye! Have a great day!")
          break
      else:
          bot_response = chatbot(user_input)
          print("Chatbot:", bot_response)

if __name__ == "__main__":
  main()