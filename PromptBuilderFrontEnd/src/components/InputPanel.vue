<script setup>

import { defineEmits, defineProps, onUpdated, ref, watch } from 'vue';

const emit = defineEmits(['update:input_name','update:input_tag'])
const props = defineProps({
    input_name: String,
    input_tag:  String,
})

const input_name = ref(props.input_name)
const input_tag = ref(props.input_tag)

onUpdated(() => {
    input_name.value = props.input_name;
    input_tag.value = props.input_tag;
});


watch(input_name, (newValue) => {
  emit('update:input_name', newValue);
});

watch(input_tag, (newValue) => {
  emit('update:input_tag', newValue);
});

</script>

<template>
    <div class="container-fluid" style="margin-top:-40px">
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