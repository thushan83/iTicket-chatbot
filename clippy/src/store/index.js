import { createStore } from "vuex";

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
    askQuestion(payload) {
     console.log('payload', payload)
    }
}

});

