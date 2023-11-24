<template>
  <div class="container">
    <div id="scroller" class="all-qestion-container">
      <div v-for="(askedQuestion, i) in AllQuestions" :key="askedQuestion" >
        <p class="asked-question">
          <span class="question">
            Me: {{ askedQuestion }}
          </span>
        </p>
        <p v-for="(answer, index) in answers" :key="answer">
          <span class="answer" v-if="index == i">
            ITicket: {{ answer }}
          </span>
        </p>
      </div>
    </div>
    <div>
      <p v-if="!question && AllQuestions.length == 0"> Let me help you navigate in the protal!</p>
      <input v-model="question" type="text" placeholder="Ask your question">
      <button @click="ask()">Ask</button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'AskQuestion',
  data () {
    return {
      question: '',
      AllQuestions: []
    }
  },
  computed: {
   answers () {
     console.log('awnser', this.$store.state.answer)
     return this.$store.state.answers
   }
  },
  methods: {
  async ask () {
    this.AllQuestions.push(this.question)
    // this.question = ''
    console.log('question', this.question)
   await this.$store.dispatch("askQuestion", this.question)
   this.question = ''
   const scroller = document.getElementById('scroller')
   const container = scroller;
      container.scrollTop = container.scrollHeight;
  },
}
}
</script>
<style>
.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  border: 1px solid #ccc;
}
input{
  padding: 0.5rem;
  border: 1px solid #ccc;
}
button{
  padding: 0.5rem;
  border: 1px solid #ccc;
  background: #eee;
}
.all-qestion-container{
height: 10rem !important;
overflow-y: auto;
margin: 1rem;
}
.asked-question{
display: flex;
justify-content: end;
width: 100%;
}
.question{
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  background-color: beige;
  padding: 0 0.5rem;
  width: fit-content;
  border-radius: 4px;
}
.answer{
  background-color: #eee;
  padding: 0 0.5rem;
  float: inline-start;
  margin-bottom: 1.8rem;
  border-radius: 4px;
}

</style>