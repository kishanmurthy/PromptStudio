<script setup>

import { defineProps, ref } from 'vue';

const props = defineProps({
    inputTags: {
        type: Array,
        required: true
    }
})

const inputTags = ref(props.inputTags );

const addInput = ()=> {
      inputTags.value.push({text: ""});
    }

const deleteTag = (id) => {
    // splice the node out of the array
    inputTags.value.splice(id, 1);
}

</script>

<template>
    <div class="container-fluid">
    <div class="row">
        <div class="col-md-10">
            <label>Input Tags</label>
        </div>
        <div class="col-md-2">
            <font-awesome-icon class='plus-icon' :icon="['fas', 'plus']" @click="addInput"/>
        </div>
    </div>
    <div class="row">
            <template v-for="(input, index)  in inputTags" :key=index>
                <div class="col-md-10">
                    <input  class = "input-tag" type="text" v-model="input.text" />
                </div>
                <div class="col-md-1">
                    <font-awesome-icon class='plus-icon' :icon="['fas', 'xmark']" @click="deleteTag"/>
                </div>
            </template>
            
    </div>

</div>
</template>


<style scoped>

.plus-icon {
    /* spadding-left: 10px; */
}

.input-tag {
    width: 100%
}

</style>