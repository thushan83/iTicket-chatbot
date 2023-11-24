<template>
  <div class="all-qestion-container">
    <div id="scroller"  v-for="(askedQuestion, i) in AllQuestions" :key="askedQuestion" >
      <p class="asked-question">{{ askedQuestion }}</p>
      <p v-for=" (answer, index) in answers" :key="answer">
        <span v-if="index == i">
          {{ answer }}
        </span>
      </p>
    </div>
  </div>
  <div>
 <input v-model="question" type="text" placeholder="Ask your question">
  <button @click="ask()">Ask</button>
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
}
.asked-question{
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

</style>