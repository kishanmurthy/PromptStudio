<script setup>
    import DagPannel from './DagPannel.vue';

    import { defineEmits, defineProps, onMounted, onUpdated, ref, watch } from 'vue';

    const emit = defineEmits(['update:DAGS', 'update:selectedDAG'])
    

    const props = defineProps({
        DAGS: {
            type: Array,
            required: true
        },
        selectedDAG: {
            type: Number,
            required: false
        }
    })

    const DAGS = ref([])

    const selectedDAG = ref(0)
    var count = 0
    
    const add_flow = () => {
        count+=1
        DAGS.value.push({'name':`Version ${count}`, 'inputPanels':[], 'promptPanels':[], 'elements':[]})
    }

    onMounted(() => {
        DAGS.value = props.DAGS
        selectedDAG.value = props.selectedDAG
    })

    onUpdated(() => {
        DAGS.value = props.DAGS
        selectedDAG.value = props.selectedDAG
        count = DAGS.value.length
    }),

    watch(DAGS, () => {
        emit('update:DAGS', DAGS.value)
    })

    watch(selectedDAG, () => {
        emit('update:selectedDAG', selectedDAG.value)
    })

</script>

<template>
    <div class="container-fluid">
        <div class="row full-panel">
            <div class="col-md-2" style="padding:20px 0; width: 14.5%;">
                <ul type="square">
                    <template v-for="(DAG,index) in DAGS">
                        <li class="version-list" @click="selectedDAG=index">
                            <a>{{DAG.name}}</a>
                        </li>
                    </template>
                </ul>
                <button class="button-node new-flow" @click="add_flow">
                    <font-awesome-icon :icon="['fas', 'plus']" size="lg"/>
                    <span>New Flow</span>
                </button>
            </div>
            <div class="col-md-10" style="padding:0">
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
    ol { 
        margin-top: 20px !important;
    }
    li {
        padding: 5px 0;
        cursor: pointer;
    }
    .new-flow {
        background: #CBCBCB !important;
        margin-left: 10px;
    }
</style>