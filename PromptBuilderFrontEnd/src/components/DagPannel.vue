<script setup>

import { Background } from '@vue-flow/background';
import { Controls } from '@vue-flow/controls';
import '@vue-flow/controls/dist/style.css';
import { VueFlow, useVueFlow } from '@vue-flow/core';


import { MiniMap } from '@vue-flow/minimap';
import { onMounted, ref, watch } from 'vue';
import InputPanel from './InputPanel.vue';
import NodeControl from './NodeControl.vue';
import Prompt from './Prompt.vue';
import Run from './Run.vue';

import { defineEmits, defineProps } from 'vue';
// const props = defineProps({
//    DAG: {
//     type: Object,
//     required: true,
//   },
// });
// name':`Verson ${count}`, 'inputPanels':[], 'promptPanels':[], 'elements'

const props = defineProps({
  dagName: {
    type: String,
    required: true,
  },
  inputPanels: {
    type: Array,
    required: true,
  },
  promptPanels : {
    type: Array,
    required: true,
  },
  elements : {
    type: Array,
    required: true,
  },
});

const emits = defineEmits(['update:dagName', 'update:inputPanels', 'update:promptPanels', 'update:elements'])




const state = ref('')
const tag_id = ref(0)

const dagName = ref(props.dagName)
const inputPanels = ref([])
const promptPanels = ref([])
const elements = ref([])

const { onConnect, addEdges } = useVueFlow()

onConnect((params) => addEdges(params))

const addNodePanel = (panel_type, name, value) => {
  console.log(panel_type,value)
  if (panel_type == 'input')
    inputPanels.value.push({'name':name, 'text':''})
  else if (panel_type == 'prompt')
    promptPanels.value.push({'name':name, 'prompt_value':'', 'output_tag': '', 'output_format': 'JSON'})
    
  state.value = panel_type
  tag_id.value = value - 1
  console.log(inputPanels[tag_id])
}

const clickNode = (panel_type, value) => {
  console.log("inside click node",panel_type,value)
  state.value = panel_type
  tag_id.value = value - 1
  console.log(inputPanels.value[tag_id.value])
}

onMounted(() => {
  dagName.value = props.dagName
  inputPanels.value = props.inputPanels
  promptPanels.value = props.promptPanels
  elements.value = props.elements
})

// onUpdated(() => {
//   dagName.value = props.dagName
//   inputPanels.value = props.inputPanels
//   promptPanels.value = props.promptPanels
//   elements.value = props.elements
// })

watch(dagName, (newValue) => {
  emits('update:dagName', newValue);
});

watch(inputPanels, (newValue) => {
  emits('update:inputPanels', newValue);
});

watch(promptPanels, (newValue) => {
  emits('update:promptPanels', newValue);
});

watch(elements, (newValue) => {
  emits('update:elements', newValue);
});

</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-10 dag-panel">
          <VueFlow
            v-model="elements"
            class="basicflow"
            :default-edge-options="{ type: 'smoothstep' }"
            :min-zoom="0.2"
            :max-zoom="4"
          >      
            <NodeControl @add-node-panel="addNodePanel" @click-node="clickNode"/>
            <Background pattern-color="#aaa" gap="8" />
            <MiniMap />
            <Controls />
          </VueFlow>
      </div>
      <div class="col-md-2">
        <template v-if="state=='input'" >
          <!-- <Begin :inputTags="inputTags"/> -->
          <InputPanel :input_name="inputPanels[tag_id].name" 
          :input_tag="inputPanels[tag_id].input_tag"
          @update:input_name="(new_value)=>{inputPanels[tag_id].name = new_value}"
          @update:input_tag="(new_value)=>{inputPanels[tag_id].input_tag = new_value}"

          /> 
        </template>
        <template v-if="state=='prompt'">
            <Prompt
            :prompt_name = "promptPanels[tag_id].name" 
            :prompt_value = "promptPanels[tag_id].prompt_value"
            :output_tag = "promptPanels[tag_id].output_tag"
            :output_format = "promptPanels[tag_id].output_format"
            @update:prompt_name="(new_value)=>{promptPanels[tag_id].name = new_value}"
            @update:prompt_value="(new_value)=>{promptPanels[tag_id].prompt_value = new_value}"
            @update:output_tag="(new_value)=>{promptPanels[tag_id].output_tag = new_value}"
            @update:output_format="(new_value)=>{promptPanels[tag_id].output_format = new_value}"
            />
        </template>
        <template v-if="state=='run'">
            <Run/>
        </template>
      </div>
    </div>
  </div>

</template>


<style scoped>
  /* these are necessary styles for vue flow */
  .dag-panel {
    height: 90vh;
  }
</style>
