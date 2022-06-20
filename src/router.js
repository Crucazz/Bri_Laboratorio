import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'


Vue.use(Router)

export default new Router({
	mode: 'history',
	routes: [
		// Rutas iniciales (Seleccion curso y asignatura)
		{path: '/', component: Home},

		{
			path: '/cursos/:id',
			name: 'cursos',    
			component: () => import(/* webpackChunkName: "cursos" */ './views/cursos.vue')
		},

		//Rutas para historia
		{
			path: '/historia/:id',
			name: 'iniciohistoria',    
			component: () => import(/* webpackChunkName: "iniciohistoria" */ './views/inicioHistoria.vue')
		},

		//Rutas para Matematicas
		{
			path: '/matematicas/:id',
			name: 'iniciomatematicas',    
			component: () => import(/* webpackChunkName: "iniciomatematicas" */ './views/inicioMatematicas.vue')
		},
		
	]
})