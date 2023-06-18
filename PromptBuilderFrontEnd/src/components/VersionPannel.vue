<script setup>
    import DagPannel from './DagPannel.vue';
    import { ref } from 'vue'

    const props = defineProps(['versions']);
    const versionData = ref([]);

    // iterate over props and display the flows
    // when add flow is clicked, create a new flow and open that tab
    function loadDag(versionId){
        versionData.value = props.versions[versionId];
    }

    function addFlow(versionId){
        versionData.value = [];
    }

</script>

<template>
    <div class="container-fluid">
        <div class="row full-panel">
            <div class="col-md-2">
                <ol>
                    <li class="version-list" @click="loadDag(version)" v-for="version in Object.keys(props.versions)">
                        {{version}}
                    </li>
                </ol>
                <button class="button-node" @click="addFlow">
                    <font-awesome-icon :icon="['fas', 'plus']" size="lg"/>
                    <span>New Flow</span>
                </button>
            </div>
            <div class="col-md-10">
                <DagPannel v-bind:elements="versionData" class="dag-panel"/>
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
    }

</style>