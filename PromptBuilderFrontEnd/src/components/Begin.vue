<script setup>

import { ref } from 'vue';
const inputTags = ref('')

</script>

<template>
    <div class="container-fluid">
    <h3>Begin</h3>
    <label>Input Tags</label>
    <input type="text" v-model="inputTags" />      
    </div>
</template>


<style>
</style>