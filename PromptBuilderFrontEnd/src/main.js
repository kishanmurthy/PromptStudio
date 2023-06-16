import './assets/main.css'


import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.css'


import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faDownload, faFloppyDisk, faPlay, faUpload } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faFloppyDisk, faDownload,faPlay,faUpload)

const app = createApp(App)

app.use(createPinia())

app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
