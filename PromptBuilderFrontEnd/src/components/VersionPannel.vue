<script setup>
    import DagPannel from './DagPannel.vue';
</script>

<template>
    <div class="container-fluid">
        <div class="row full-panel">
            <div class="col-md-1">
                <button>Add Flow</button>
            </div>
            <div class="col-md-11">
                <DagPannel class="dag-panel"/>
            </div>
        </div>
    </div>
</template>

<style>
    @import '@vue-flow/core/dist/style.css';
    @import '@vue-flow/core/dist/theme-default.css';
    .full-panel {
        display: block;
        height: 1000px;
    }

    .dag-panel {
        height: 100%;
    }
</style>