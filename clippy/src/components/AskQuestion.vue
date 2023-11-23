<template>
  <div class="all-qestion-container">
    <div  v-for="askedQuestion in AllQuestions" :key="askedQuestion" >
      <p class="asked-question">{{ askedQuestion }}</p>
      <p> {{ awnser }}</p>
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
   awnser () {
     console.log('awnser', this.$store.state.answer)
     return this.$store.state.answer
   }
  },
  methods: {
  async ask () {
    this.AllQuestions.push(this.question)
    // this.question = ''
    console.log('question', this.question)
   await this.$store.dispatch("askQuestion", this.question)
   this.question = ''
  }
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
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  max-height: 30%;
  overflow: scroll;
}
.asked-question{
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

</style>