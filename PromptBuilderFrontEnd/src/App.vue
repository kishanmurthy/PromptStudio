<script setup>
  import { ref } from 'vue';
import VersionPannel from './components/VersionPannel.vue';

  const DAGS = ref([])
  const selectedDAG = ref(0)

</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-8">
        <h3>Prompt Builder</h3>
      </div>
      <div class="col-md-2">
        <div class="row">
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'floppy-disk']" size="lg"/>
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'download']" size="lg" />
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'play']" size="lg" />
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'upload']" size="lg" />
          </div>
        </div>
      </div>
      <div class="col-md-2">
        <h4>Placeholder Text</h4>
      </div>
    </div>
    <VersionPannel 
      :DAGS="DAGS"
      :selectedDAG="selectedDAG"
      @update-DAGS="(new_value)=>{DAGS = new_value}"
      @update:selectedDAG="(new_value)=>{selectedDAG = new_value}"
    />
  </div>

</template>

<style scoped>

</style>
