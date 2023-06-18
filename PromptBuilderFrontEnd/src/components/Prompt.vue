<script setup>

import { defineProps, onUpdated, ref, watch } from 'vue';

const emit = defineEmits(['update:prompt_name','update:prompt_value','update:output_tag','update:output_format'])

const props = defineProps({
    nodeId: String,
    prompt_name: String,
    prompt_value: String,
    output_tag: String,
    output_format: String,
})

const promptName = ref(props.prompt_name)
const promptTag = ref(props.prompt_value)
const outputTag = ref(props.output_tag)
const outputFormat = ref(props.output_format)

onUpdated(() => {
    promptName.value = props.prompt_name;
    promptTag.value = props.prompt_value;
    outputTag.value = props.output_tag;
    outputFormat.value = props.output_format;
});

watch(promptName, (newValue) => {
  emit('update:prompt_name', newValue);
});

watch(promptTag, (newValue) => {
  emit('update:prompt_value', newValue);
});

watch(outputTag, (newValue) => {
  emit('update:output_tag', newValue);
});

watch(outputFormat, (newValue) => {
  emit('update:output_format', newValue);
});


</script>

<template>
    <div class="container-fluid" style="margin-top:-40px">
    <h3>{{promptName }}</h3>
    <label>Prompt</label>
    <textarea v-model="promptTag"/>
    <label>Output Tag Name</label>
    <input style="width:100%" type="text" v-model="outputTag" />
    <label>Output Format</label>    
    <select v-model="outputFormat">
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

textarea {
  font-size: 10px;
  height: 250px !important;
  width: 100%;
}

</style>