<script setup>

import { defineEmits, defineProps, ref } from 'vue';
// defineEmits(['update:panel'])
const props = defineProps({
    input_name: String,
    input_tag:  String,
})

const input_name = ref(props.input_name)
const input_tag = ref(props.input_tag)

watch(() => props.input_name, (newValue) => {
  input_name.value = newValue;
});

watch(() => props.input_tag, (newValue) => {
  input_tag.value = newValue;
});


watch(input_name, (newValue) => {
  emit('update:input_name', newValue);
});

watch(input_tag, (newValue) => {
  emit('update:input_tag', newValue);
});

</script>

<template>
    <div class="container-fluid">
        <h3>{{ input_name }}</h3>
        <label>Input Tag</label>
        <input  class = "input-tag" type="text" v-model="input_tag" />
    </div>
</template>

  


<style scoped>

.input-tag {
    width: 100%
}

</style>