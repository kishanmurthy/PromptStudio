<script setup>

import { Background } from '@vue-flow/background'
import { Controls } from '@vue-flow/controls'
import '@vue-flow/controls/dist/style.css'
import { VueFlow, useVueFlow } from '@vue-flow/core'
import { MiniMap } from '@vue-flow/minimap'
import { ref } from 'vue'
import Begin from './Begin.vue'
import Prompt from './Prompt.vue'
import Run from './Run.vue'
import { defaultDag } from './assets/default-dag.js'

const state = ref('begin')

const inputTags = ref([{text:''}])

const Prompts = ref([])

const Outputs = ref([])


const { onConnect, addEdges } = useVueFlow()

const elements = ref(defaultDag)

onConnect((params) => addEdges(params))



</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-10 dag-panel">
          <VueFlow
            v-model="elements"
            class="basicflow"
            :default-edge-options="{ type: 'smoothstep' }"
            :default-viewport="{ zoom: 1.4 }"
            :min-zoom="0.2"
            :max-zoom="4"
            fit-view-on-init
          >
            <Background pattern-color="#aaa" gap="8" />
            <MiniMap />
            <Controls />
          </VueFlow>
      </div>
      <div class="col-md-2">
        <template v-if="state=='begin'" >
          <Begin :inputTags="inputTags"/>
        </template>
        <template v-if="state=='prompt'">
            <Prompt />
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
