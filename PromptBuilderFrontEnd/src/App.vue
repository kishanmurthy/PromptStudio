<script setup>
  import { onMounted, ref } from 'vue';
import VersionPannel from './components/VersionPannel.vue';

  const url = 'http://127.0.0.1:5000'
  const DAGS = ref([])
  const selectedDAG = ref(0)

  const showModal = ref(false)
  const modal_input_text = ref('')
  const run_output_text = ref('')
  var run_complete = ref('false')


  const onSave = () => {
    console.log('save')
    console.log(JSON.stringify(DAGS.value[selectedDAG.value]))

    fetch(url+'/save', {
      method: 'POST',
      body: JSON.stringify(DAGS.value[selectedDAG.value]),
      headers: {
      'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .catch(error => console.error(error));        
  }
  
 
  const onRun = ()=>{
    modal_input_text.value = Array(DAGS.value[selectedDAG.value].inputPanels.length).fill('')
    showModal.value=true
    run_output_text.value = ''
    run_complete.value = false
  }

  const onRunModal = () => {
    console.log('run modal')

    var run_data = {
      'DAGS':DAGS.value[selectedDAG.value],
      'input_text':modal_input_text.value,
    }
    console.log(JSON.stringify(run_data))
    fetch(url+'/run', {
      method: 'POST',
      body: JSON.stringify(run_data),
      headers: {
      'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .catch(error => console.error(error));        
  }

  const onPublish = () => {
    console.log('Publish')
    fetch(url+'/publish', {
      method: 'POST',
      body: JSON.stringify(DAGS.value[selectedDAG.value]),
      headers: {
      'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .catch(error => console.error(error));        
  }

  onMounted(async () => {
    const response = await fetch(url+'/load')
    const data = await response.json()
    console.log("Data Received", data)
    DAGS.value = data
  })

  const onDownload = () => {
    console.log('download')
    console.log('save')
    console.log(JSON.stringify(DAGS.value[selectedDAG.value]))

    fetch(url+'/save', {
      method: 'POST',
      body: JSON.stringify(DAGS.value[selectedDAG.value]),
      headers: {
      'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .catch(error => console.error(error));        


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
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'download']" size="lg" @click="onDownload"/>
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'play']" size="lg"  @click="onRun"/>
          </div>
          <div class="col-md-3">
            <font-awesome-icon class="icon-top-bar" :icon="['fas', 'upload']" size="lg" @click="onPublish"/>
          </div>
        </div>
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
        <span class="close" @click="()=>{showModal=false}">&times;</span>

        <label>Input Tags</label>
        <div class="container">
          <div class="row">
            <template v-for="(panel, index)  in DAGS[selectedDAG].inputPanels" :key=index>
              <div class="col-md-1">
                <label>{{ panel.input_tag }}</label>
              </div>
              <div class="col-md-11">
                <textarea v-model="modal_input_text[index]"></textarea>
              </div>
            </template>
            
            <div>
              <button @click="onRunModal">Run</button>
            </div>
            <template v-if="run_complete">
              <div class="col-md-1">
                <label>Output</label>
              </div>
              <div class="col-md-11">
                <textarea v-model="run_output_text"></textarea>
              </div>
            </template>
        </div>

        </div>
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

.icon-top-bar {
  cursor: pointer;
}

</style>
