<template>
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
      question: ''
    }
  },
  methods: {
  ask () {
    console.log(this.question)
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

</style>