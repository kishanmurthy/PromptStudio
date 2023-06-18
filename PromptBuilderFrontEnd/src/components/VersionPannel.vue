<script setup>
    import DagPannel from './DagPannel.vue';

    import { ref } from 'vue';

    const DAGS = ref([])

    const selectedDAG = ref(0)
    var count = 0
    
    const add_flow = () => {
        count+=1
        DAGS.value.push({'name':`Verson ${count}`, 'inputPanels':[], 'promptPanels':[], 'elements':[]})
    }


</script>

<template>
    <div class="container-fluid">
        <div class="row full-panel">
            <div class="col-md-1">
                <button @click="add_flow">Add Flow</button>
                    <template v-for="(DAG,index) in DAGS">
                        <button class="version-list" @click="selectedDAG=index">
                            {{DAG.name}}
                        </button>
                    </template>
            </div>
            <div class="col-md-11">
                <template v-for="(DAG,index) in DAGS">

                    <template v-if="index==selectedDAG">
                        <DagPannel class="dag-panel" 
                        :dagName="DAG.name" 
                        :inputPanels="DAG.inputPanels" 
                        :promptPanels="DAG.promptPanels" 
                        :elements="DAG.elements" 
                        @update-dag-name="(new_value)=>{DAGS[index].dagName = new_value}"
                        @update:inputPanels="(new_value)=>{DAGS[index].inputPanels = new_value}"
                        @update:promptPanels="(new_value)=>{DAGS[index].promptPanels = new_value}"
                        @update:elements="(new_value)=>{DAGS[index].elements = new_value}"
                       />
                    </template>
                </template> 
            </div>
        </div>
    </div>
</template>

<style>
    @import '@vue-flow/core/dist/style.css';
    @import '@vue-flow/core/dist/theme-default.css';
    .full-panel {
        display: block;
        height: 100vh;
    }

    .dag-panel {
        height: 100vh;
    }
    .version-list {
        cursor: pointer;
        width: 100%;
    }
</style>