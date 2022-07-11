import axios from 'axios'
import Vue from 'vue'
//axios.defaults.baseURL = 'http://localhost:8000';

const axiosInstance = axios.create({ 
  baseURL: 'http://127.0.0.1:4000'
})

//Para acceder a axios desde this.$http
Vue.prototype.$http = axiosInstance;

axios.defaults.headers.common['Authorization'] = 'Bearer' + localStorage.getItem('token');