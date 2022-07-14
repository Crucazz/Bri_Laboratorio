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
          <div @click="toInicio" class=" mx-auto text-center secondary text-no-wrap rounded-xl">
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
                src="../assets/matematicas.png"
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

   <v-container v-if="items">
      <v-row dense>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
        >
        <a :href="item.url[0]">
          <v-card
          color="#ffffff"

            dark
          >
            <div class="d-flex flex-no-wrap  justify-space-between">
               <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img src="https://www.redcenit.com/redcenit/wp-content/uploads/2016/04/mathematics-1044087_1920.jpg"></v-img>
              </v-avatar>
              <div>
                <v-card-title
                  class="text-h5 "
                > <FONT COLOR="black"> {{item.title[0]}} </FONT></v-card-title>

                <v-card-subtitle >  <FONT COLOR="black"> {{item.abstract[0]}}<br><br> {{item.url[0]}} </FONT> </v-card-subtitle>


              

                <v-card-actions>
                  <v-btn
                    v-if="item.type[0] == 'contenido'"
                    class="ml-2 mt-5" 
                    fab
                    small
                    color="#46eeff"                   
                  >
                    C
                  </v-btn>

                  <v-btn
                    v-if="item.type[0] == 'ejercicio'"
                    class="ml-2 mt-5"                    
                    fab
                    small
                    color="#ff9d46"
                  >
                    E
                  </v-btn>
                  <v-btn
                    v-if="item.type[0]=='fracciones'"
                    class="ml-2 mt-5"                    
                    fab
                    small
                    color="#ff9d46"
                  >
                    E
                  </v-btn>

                  <v-btn
                    v-if="item.format == 'video'"
                    class="ml-2 mt-5"
                    fab
                    small
                    color="#008000"
                  >
                    V
                  </v-btn>
                  <v-btn
                    v-if="item.format == 'doc'"
                    class="ml-2 mt-5"
                    fab
                    small
                    color="#9246ff"
                  >
                    D
                  </v-btn>
                </v-card-actions>
              </div>
             
            </div>
          </v-card>
          </a>
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
      items: null,
      curso: null,
      prueba:{},
    }),
    methods:{
        //Función asíncrona para consultar los datos
        getData: async function(){
          var result=null;
          this.curso = document.URL.split("/")[4];
          if(this.curso == "3")
          {
              result = await this.$http.get('/matematicaCuarto');
              this.prueba = result.data.response;
              this.items = this.prueba.docs;
          }
          else
          {
            try {
              result = await this.$http.get('/matematicaCuarto');
              this.prueba = result.data.response;
              this.items = this.prueba.docs;
                
            } catch (error) {
                console.log('error', error);
            }
          }

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
      this.curso = document.URL.split("/")[4];
      this.getData();
    }
  }
</script>