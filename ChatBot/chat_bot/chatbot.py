
chatbot_name = "iTicket: "
guest = "You: "

def main():
    default_response = "Sorry I do not have the answer, or I do not understand your question"
    print(chatbot_name,"Welcome how can I help you ?")
    while True:        
        question = ""
        question = input(guest)
        print(chatbot_name, default_response)


if __name__ == "__main__":
    main()