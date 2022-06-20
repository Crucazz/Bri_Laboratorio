<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      v-if="user"
    >
      <v-list dense>
        <router-link @click="getDatos()" to="/">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Inicio</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>

          





         <router-link v-if="user.rol==1" to="/minManage/Configuracion">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Iniciar/cerrar proceso <br> Postulación</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>   




        

        <router-link to="/minManage/infoMinors">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Información de Minors</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==1" to="/minManage/editAll">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Información de <br> Usuarios</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==1" to="/minManage/crearMinor">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Añadir/crear Minors</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==4" to="/minManage/alumnoAvance">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Mis Minors</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==4 && registroFinal.switch_postulacion==1" to="/minManage/postulacion">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Postular a minor</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==4" to="/minManage/revisarPostulacion">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Estado de mis <br> postulaciones</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==4 && registroFinal.switch_postulacion==1" to="/minManage/tomarAsignatura">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Tomar asignatura</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>



        <router-link v-if="user.rol==2" to="/minManage/minorsCoordinador">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Administrar Minor</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>


        <router-link v-if="user.rol==3" to="/minManage/revisarPostulacionesCarrera">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Revisar postulaciones<br>  de alumnos</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==2" to="/minManage/revisarPostulacionesCoordinador">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Revisar postulaciones <br> de alumnos</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>


        <router-link v-if="user.rol==1  || user.rol==3" to="/minManage/minors">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Minors</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>


        <router-link v-if="user.rol==2" to="/minManage/historicoCoordinador">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Alumnos historico</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==1" to="/minManage/historico">
          <v-list-item link @click="getDatos()">
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Alumnos historico</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==1" to="/minManage/PostulacionesHistoricoAdmin">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Postulaciones historico</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>


        <router-link v-if="user.rol==2" to="/minManage/PostulacionesHistoricoCoord">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Postulaciones historico</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>

        <router-link v-if="user.rol==3" to="/minManage/PostulacionesHistoricoJefeCarrera">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-contact-mail</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Postulaciones historico</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>
        

        <br><br><br><br><br><br><br><br><br><br>
        
        <v-list-item link>
            <v-list-item-content>
              <v-btn class="blue" color="white" text small @click="goToNotifications(user)" >
                Notificaciones
                <v-badge
                v-if="notificaciones>0"
                class="ml-2"
                color="orange"
                content="!"
                >
                </v-badge> 
              </v-btn>
            </v-list-item-content>
          </v-list-item>

        <v-list-item link>
            <v-list-item-content>
              <v-btn class="blue" color="white" text small @click="goToAlumno(user)" >
                Información Personal
              </v-btn>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link>
            <v-list-item-content>
              <v-btn class="blue" color="white" text small @click="cerrar" >
                Cerrar sesión 
              </v-btn>
            </v-list-item-content>
          </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="blue darken-4"
      dark
      v-if="user"
    >
      <v-app-bar-nav-icon  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>      
      <v-toolbar-title>
        Plataforma de Minors
      </v-toolbar-title>
      <img src="https://dimulti.usach.cl/sites/dingmulti/files/logo-blanco.png" style="float: right; margin: 0 0 1em 2em" alt="Logo de usach" width="150" height="45">
      
    </v-app-bar>

<nav class="navbar navbar-expand navbar-light fixed-top" v-if="!user">
       <div class="">
        
      <a href="https://dimulti.usach.cl/" class="navbar-brand"> 
        <img src="https://dimulti.usach.cl/sites/dingmulti/files/dingmulti.png" alt="Logo de Dimulti">
      </a>
    </div>
      <div class="container">
        <div class="collapse navbar-collapse">


          <ul class="navbar-nav ml-auto" v-if="!user">
            <li class="nav-item" >
              <router-link to="/minManage/login" class="nav-link">Iniciar sesión </router-link>
            </li>
            <li class="nav-item" >
              <router-link to="/minManage/roles/all" class="nav-link">inicio</router-link>
            </li>
          </ul>

          <ul class="navbar-nav ml-auto" v-if="user">
            <li class="nav-item" >
              <a href="https://dimulti.usach.cl/" :@click="handleClick" class="nav-link">Cerrar sesion</a>
            </li>
            <li class="nav-item" >
              <router-link to="/" class="nav-link">inicio</router-link>
            </li>
          </ul>


        </div>
      </div>
    </nav>




    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="text-center">            
              <router-view/>
          </v-col>
        </v-row>
      </v-container>
    </v-content>



  </v-app>








</template>    

<script>

import {mapGetters} from 'vuex'

export default {
  name: 'App',
  computed: {
      ...mapGetters(['user'])

  },
  data(){
        return{
            registroFinal:[],
            drawer: null,
            notificaciones:0,
            actual:null,
            cosas: null,     
        }
    },
      
  methods: {
      getData: async function(){
            try {
                var result = await this.$http.get('/minManage/estado_global');
                let response = result.data;                

                this.registroFinal  = response;

                this.cosas = this.$cookies.get("tokken");
                if(this.user==null && this.cosas!=null)
                {
                  var result2 = await this.$http.post('/minManage/user', { jwt: this.cosas.jwt});
                  let response2 = result2.data; 
                  this.$store.dispatch('user', response2);
                }

                
            } catch (error) {
                console.log('error', error);
            }
      },

      //Función asíncrona para consultar los datos
      getDatos: async function(){
          try {
              let response = await this.$http.post('minManage/notificaciones_no_leidas',{
                id: this.user.id,
              });
              this.notificaciones  = response.data;
              } 
          catch (error) {
                console.log('error', error);
            }
        },
      cerrar() {
        this.$store.dispatch('user',null);
        this.$cookies.remove("tokken");
        this.cosas=[];
        this.$router.push('/');
        
      },

      goToAlumno(item) {
        try {
              this.getDatos();
              const alumnoID = item.id;
              this.$router.push({name:'editUsuario',params:{id:alumnoID}});
            } 
          catch (error) {
                console.log('error', error);
            }
          
      },
      goToNotifications(item) {
          try {
              let response2 = this.$http.post('minManage/cambiar_estado_notificaciones',{
                id: this.user.id,
              });
              this.actual  = response2.data;
              this.getDatos();
              const alumnoID = item.id;
              this.$router.push({name:'notificaciones_user',params:{id:alumnoID}});
              } 
          catch (error) {
                console.log('error', error);
            }
          
      },
    },
    created:function(){
        this.getData();
        this.getDatos();
    },
    
  props: {
      source: String,
    }
    
};
</script>