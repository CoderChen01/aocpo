import Vue from 'vue'
import Axios from 'axios'

const requests = Axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
    timeout: 5000
    })

export default requests