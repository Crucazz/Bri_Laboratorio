<template>
    <v-container max-width="900"
    class="mx-auto">
     <v-row
      class="fill-height"
      align="center"
      justify="center"
    >
      <v-col cols="2"
          sm="2" >
          <div  @click="toInicio"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="125"
              class=" mx-auto text-center secondary text-no-wrap rounded-xl"
            >
              <v-img v-if="curso==3"
                src="../assets/tercero.png"
              >
              </v-img>
              <v-img v-else
                src="../assets/cuarto.png"
              >
              </v-img>
            </v-card>
          
          </div>
            
      </v-col>
      <v-col cols="8"
          sm="8" >
          <div  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="400"
              class=" mx-auto text-center secondary text-no-wrap rounded-xl"
            >
              <v-img
                src="../assets/logo.png"
              >
              </v-img>
            </v-card>
          
          </div>
            
      </v-col>
      <v-col cols="2"
          sm="2" >
          <div  @click="toCursos"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="125"
              class=" mx-auto text-center secondary text-no-wrap rounded-xl"
            >
              <v-img
                src="../assets/historia.png"
              >
              </v-img>
            </v-card>
          </div>
            
      </v-col>
      
    </v-row>
     <v-row
      class="pa-2"
      align="center"
      justify="center"
    >
    <v-col  cols="14"
          sm="5"
          md="2">
        </v-col>
      <v-col  cols="16"
          sm="10"
          md="8">
        
  <v-text-field
  label="¿Qué estas buscando?"
  outlined
  dense
  >
    <v-icon
      slot="append"
      color="green"
      @click="buscar"
    >
      mdi-minus
    </v-icon>
  </v-text-field>
    </v-col>
    
    </v-row>


    <v-row
      class="pa-2"
      align="center"
      justify="center"
    >



    <v-container>
      <v-row dense>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
        >
          <v-card
          color="#be9220"

            dark
          >
            <div class="d-flex flex-no-wrap  justify-space-between">
               <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img :src="item.src"></v-img>
              </v-avatar>
              <div>
                <v-card-title
                  class="text-h5 "
                  v-text="item.title"
                ></v-card-title>

                <v-card-subtitle >{{item.cuerpo}} <br><br> {{item.link}}</v-card-subtitle>
              

                <v-card-actions>
                  <v-btn
                    v-if="item.materia == 'si'"
                    class="ml-2 mt-5"
                    outlined
                    rounded
                    small
                  >
                    C
                  </v-btn>

                  <v-btn
                    v-if="item.ejercicios == 'si'"
                    class="ml-2 mt-5"
                    outlined
                    rounded
                    small
                  >
                    E
                  </v-btn>
                </v-card-actions>
              </div>
             
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>


  </v-row>

    


  </v-container>
</template>

<script>
  export default {  
    name: 'iniciomatematicas',
    data: () => ({
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
          title: 'La historia secreta de baradit',
          cuerpo: 'Los europeos iban al circo a ver y deleitarse con indigenas chilenos',
          link: 'http://google.com',
          materia: 'si',
          ejercicios: 'no'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Fundacion de roma',
          cuerpo: 'Romulo y remo fueron dos niños abandonados...',
          link: 'http://google.com',
          materia: 'no',
          ejercicios: 'si'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Alejandro magno, el emperador ideal',
          cuerpo: 'Conocido como uno de los mayores emperadores de la historia con decenas de cuentos e historias',
          link: 'http://google.com',
          materia: 'si',
          ejercicios: 'si'
        },
      ],
      curso: null,
    }),
    methods:{
        //Función asíncrona para consultar los datos
        getData: async function(){
          this.curso = document.URL.split("/")[4]; 
        },
        toInicio () {
          this.$router.push('/');
        },
        toCursos () { 
          this.$router.push({name:'cursos', params:{id:this.curso}});
        },
        buscar (){
          this.$router.push('/');
        }
    },
    //Función que se ejecuta al cargar el componente
    created:function(){
        this.getData();
    }
  }
</script>