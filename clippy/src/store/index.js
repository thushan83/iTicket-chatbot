import { createStore } from "vuex";
import * as API from "@/API/index";

export default createStore({
  state: {
    answers: [],
    answer: "",
  },
  mutations: {
    saveAwnser(state, payload) {
      state.answer = payload;
      state.answers.push(payload);
    },
},
actions: {
    async askQuestion(context, payload) {
     console.log('payload', payload)
     const response = await API.askAIQuesion(payload)
     console.log('response', response.answer)
      context.commit('saveAwnser', response.answer)
    }
}

});

