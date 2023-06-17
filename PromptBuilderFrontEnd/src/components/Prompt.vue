<script setup>

import { ref } from 'vue';
const promptTag = ref('')
const outputTag = ref('')
const outputFormat = ref('')
const selected = ref('')
</script>

<template>
    <div class="container-fluid">
    <h3>Prompt</h3>
    <label>Prompt</label>
    <input type="textarea" v-model="promptTag" />
    <label>Output Tag Name</label>
    <input type="text" v-model="outputTag" />
    <label>Output Format</label>    
    <select v-model="selected">
        <option selected>JSON</option>
        <option>CSV</option>
        <option>Text</option>
    </select>

    
    </div>
</template>


<style scoped>
select {
    width: 100%;
}

</style>