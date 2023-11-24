<template>
  <div class="container">
    <div class="all-qestion-container">
      <div id="scroller"  v-for="(askedQuestion, i) in AllQuestions" :key="askedQuestion" >
        <p class="asked-question">
          <span class="test">
            Me: {{ askedQuestion }}
          </span>
        </p>
        <p v-for="(answer, index) in answers" :key="answer">
          <span v-if="index == i">
            ITicket: {{ answer }}
          </span>
        </p>
      </div>
    </div>
    <div>
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
  border: 1px solid #ccc;
  max-height: 10rem;
  overflow: scroll;
  display: contents;
  width: 30rem;
}
.asked-question{
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}
.test{
  width: fit-content;
  background-color: beige;
  padding: 0 0.5rem;
  float: inline-end;

}

</style>