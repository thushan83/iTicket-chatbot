<template>
  <AskQuestion/>
</template>

<script>
import AskQuestion from './components/AskQuestion.vue'

export default {
  name: 'App',
  components: {
    AskQuestion
  }
}
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
body{
  display: flex;
  justify-content: center;
}
</style>
