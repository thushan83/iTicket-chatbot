from chat_manager import ChatManager

def main():  
    chatbot_name = "iTicket: "
    guest = "You: "
    cm = ChatManager()  
    print(chatbot_name,"Welcome!, how can I help you ?")
    while True:
        question = ""
        question = input(guest)
        print(chatbot_name, cm.find_answer(question))

if __name__ == "__main__":
    main()
  