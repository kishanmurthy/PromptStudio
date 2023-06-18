<script setup>
  import { ref } from 'vue';
import VersionPannel from './components/VersionPannel.vue';

  const url = 'http://127.0.0.1:5000'
  const DAGS = ref([])
  const selectedDAG = ref(0)

  const showModal = ref(false)

  const onSave = () => {
    console.log('save')
    console.log(JSON.stringify(DAGS.value[selectedDAG.value]))

    fetch('/save', {
      method: 'POST',
      body: JSON.stringify(DAGS.value[selectedDAG.value]),
      headers: {
      'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .catch(error => console.error(error));        
  }
  
  const onDownload = () => {
    console.log('download')
  }

  const onRun = () => {
    console.log('run')
  }

  const onUpload = () => {
    console.log('upload')
  }


  



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
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'floppy-disk']" size="lg" @click="onSave"/>
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'download']" size="lg" />
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'play']" size="lg"  @click="()=>{showModal=False}"/>
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
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="()=>{showModal=False}">&times;</span>
        <h2>Modal Title</h2>
        <p>Modal content goes here.</p>
      </div>
    </div>
  </div>

</template>

<style scoped>
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover {
  color: black;
}

</style>
