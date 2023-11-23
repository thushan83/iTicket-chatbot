import json
from flask import Flask,request, json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from iTicket chat server"


@app.route('/chat', methods=['POST'])
def chatlistner():
    return chat_response(request)


chatbot_name = "iTicket: "
guest = "You: "

def chat_response(request):
    question = request.json.get("question")
    default_response = "Sorry I do not have the answer, or I do not understand your question"
    return json.dumps({'res': ''+default_response+'','question': ''+question+''})


def main():
    default_response = "Sorry I do not have the answer, or I do not understand your question"
    print(chatbot_name,"Welcome how can I help you ?")
    while True:        
        question = ""
        question = input(guest)
        print(chatbot_name, default_response)

app.run()

#if __name__ == "__main__":
#    main()