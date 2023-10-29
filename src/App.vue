<script setup>
import axios from 'axios'
import { ref } from 'vue'

const msg = ref('')

function getMessage() {
  axios.get('/hello')
       .then((res) => {
         msg.value = res.data.message
       })
       .catch((error) => {
         console.error(error)
       })
}

</script>

<template>
  <header>
    <h1>Vue + FastAPI Example</h1>
    <hr>
  </header>

  <main>
    <div>
      <button @click="getMessage">get message</button>
      <p>{{ msg }}</p>
    </div>
  </main>
</template>

<style scoped>
</style>
