# iTicket ChatBot
iTicket Chat Bot provides help doing things in iTicket in terms of web links

A simple chatbot trained to facilitate providing menu navigation help tips. It mainly focus on giving most suitable menu navigation path for the entity specified in the question. Its capable of answering questions related  to iticket orders, products, locations with menu navigation tips.

Technologies Used
 - NLTK
 - Pytorch
 - Vue.js
  
Front-end: we created a Vue component that stores the conversation with our API
Back-end: REST API that communicates with our own AI written in Python (NLP and Deep Learning)
Techniques used : 
Tokenizing (extracting unique words) 
Stemming (resolve the base form or verbs)
Bag of Words (marking occurrences of words in questions against all known words)
Neural Network (model trained to predict most suitable label for the incoming question)

** Possible Improvements**

- Improve training data with broader pattern sets than it has now to improve the quality of the responses
- Improve the Neural Network layer (Now it uses three linear layers) wise trying out different layer types and different loss functions to improve training
- Improve training data to include more diverse set of labels to make the model more aware of the iticket domain (now its limited to location, products, articles)
- Find possibilities to improve the easy expansion of the training data (auto learn by crawling the menu etc)
- Real interaction with iTicket DOM structure to click/move to menu location going further from menu path suggestions






