<script setup>

import { ref } from 'vue';
import { Panel, PanelPosition, Position, useVueFlow } from '@vue-flow/core'

const inputTags = ref('')
const inputCount = ref(0)
const promptCount = ref(0)

const { nodes, addNodes, setNodes, setEdges, dimensions, setTransform, toObject } = useVueFlow()

function addInput() {
  inputCount.value++

  const newNode = {
    id: `input-node-${inputCount.value}`,
    label: `Input ${inputCount.value}`,
    type: "input",
    position: { x: 100, y: Math.random() * dimensions.value.height },
    sourcePosition: Position.Right,
  }

  addNodes([newNode])
}

function addPrompt() {
  promptCount.value++

  const newNode = {
    id: `prompt-node-${promptCount.value}`,
    label: `Prompt ${promptCount.value}`,
    type: "default",
    position: { x: 450, y: Math.random() * dimensions.value.height },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
  }

  addNodes([newNode])
}

function addOutput() {
    const outputNode = {
        id: 'output-node', 
        label: 'Output',
        type: "output",
        position: { x: 800, y: Math.random() * dimensions.value.height }, 
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
    width: 100px;
    display: block;
    border: 1px #ccc;
    border-radius: 5px;
    padding: 5px 7.5px;
    margin: 5px 0px;
  }
  .button-node svg {
    float: left;
    padding-right: 10px;
  }
  .button-node span {
    float: left;
  }

</style>