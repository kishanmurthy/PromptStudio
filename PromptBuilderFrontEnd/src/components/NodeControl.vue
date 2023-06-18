<script setup>

import { Panel, PanelPosition, Position, useVueFlow } from '@vue-flow/core';
import { ref } from 'vue';

const emit = defineEmits(['addNodePanel','clickNode'])
const inputTags = ref('')
var inputCount = 0
var promptCount = 0

const { nodes, addNodes, setNodes, setEdges, dimensions, setTransform, toObject } = useVueFlow()

function addInput() {
  inputCount++

  const newNode = {
    id: 'input-node-'+ inputCount.toString(),
    number_id: inputCount,
    label: 'Input '+ inputCount.toString(),
    type: "input",
    position: { x: 75, y: 550-inputCount*100 },
    sourcePosition: Position.Right,
    style: (el) => {
      if (el.selected) return { background: '#0041d0cc', color: '#d6d6d6' }
      return { background: '#0041d0', color: '#d6d6d6'  }
    },
    events: {
      click: (event) => {
        console.log("click",event.node.number_id)
        emit('clickNode', 'input',event.node.number_id)    
      }
    }
  }

  emit('addNodePanel', 'input', 'Input '+ inputCount.toString(),inputCount,'input-node-'+ inputCount.toString())
  addNodes([newNode])
}

function addPrompt() {
  promptCount++

  const newNode = {
    id: `prompt-node-${promptCount}`,
    number_id: promptCount,
    label: `Prompt ${promptCount}`,
    type: "default",
    position: { x: 425, y: 550-promptCount*150 },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
    style: (el) => {
      if (el.selected) return { background: '#1a192bcc', color: '#d6d6d6' }
      return { background: '#1a192b', color: '#d6d6d6'  }
    },
    events: {
      click: (event) => {
        console.log("click",event.node.number_id)
        emit('clickNode', 'prompt',event.node.number_id)    
      }
    }
  }
  emit('addNodePanel', 'prompt', 'Prompt '+ promptCount.toString(),promptCount,`prompt-node-${promptCount}`)
  addNodes([newNode])
}

function addOutput() {
    const outputNode = {
        id: 'output-node', 
        label: 'Output',
        type: "output",
        style: (el) => {
          if (el.selected) return { background: '#ff0072cc', color: '#d6d6d6' }
          return { background: '#ff0072', color: '#d6d6d6'  }
        },        
        position: { x: 750, y: 300 }, 
        targetPosition: Position.Left,
    }
    addNodes([outputNode])
}


</script>

<template>
<Panel :position="PanelPosition.TopRight">
    <button class="button-node" @click="addInput">
        <font-awesome-icon :icon="['fas', 'plus']" size="lg"/>
        <span>Input</span>
    </button>
    <button class="button-node" @click="addPrompt">
        <font-awesome-icon :icon="['fas', 'plus']" size="lg"/>
        <span>Prompt</span>
    </button>
    <button class="button-node" @click="addOutput">
        <font-awesome-icon :icon="['fas', 'plus']" size="lg"/>
        <span>Output</span>
    </button>
</Panel>
</template>

<style>
  .button-node {
    min-width: 100px;
    display: block;
    border: 1px #ccc;
    border-radius: 5px;
    padding: 5px 7.5px;
    margin: 5px 0px;
    background: #DDDDDD;
  }
  .button-node svg {
    float: left;
    padding-right: 10px;
  }
  .button-node span {
    float: left;
  }

</style>