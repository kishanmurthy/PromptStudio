<script setup>

import { ref } from 'vue';
const inputValues = ref('')
const outputValue = ref('')
</script>

<template>
    <div class="container-fluid">
    <h3>Run</h3>
    <label>Input 1</label>
    <input type="textarea" v-model="inputValues" />
    <label>Output</label>
    <input type="textarea" v-model="outputValue" />
    </div>
</template>


<style scoped>
select {
    width: 100%;
}

</style>