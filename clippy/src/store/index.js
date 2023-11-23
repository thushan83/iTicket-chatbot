import { createStore } from "vuex";
import * as API from "@/API/index";

export default createStore({
  state: {
    awnsers: [],
    anwser: "",
  },
  mutations: {
    saveAwnser(state, payload) {
      state.awnsers = payload;
    },
},
actions: {
    async askQuestion(context, payload) {
     console.log('payload', payload)
     const response = await API.askAIQuesion(payload)
     console.log('response', response)
    }
}

});

