import json
from flask import Flask,request, json
from chat_manager import ChatManager
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello from iTicket chat server"

@app.route('/chatbot/css')
def css():
    with open("./css/app.43244e21.css") as f:
      return f.read()

@app.route('/chatbot/js')
def js():
 with open("./js/app.f56781df.js") as f:
      return f.read()


@app.route('/chat', methods=['POST'])
def chatlistner():
    return chat_response(request)

cm = ChatManager()    


chatbot_name = "iTicket: "
guest = "You: "

def chat_response(request):
    question = request.json.get("question")
    #default_response = "Sorry I do not have the answer, or I do not understand your question"
    answer = cm.find_answer(question)
    return json.dumps({'answer': ''+answer+'','question': ''+question+''})


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