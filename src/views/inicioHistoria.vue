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
          <div @click="toInicio"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
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
  v-model="query"
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
                <v-img src="https://apptk.es/wp-content/uploads/2017/01/historia-para-ninos-370x370.jpg"></v-img>
              </v-avatar>
              <div>
                <v-card-title
                  class="text-h5 "
                > <FONT COLOR="black"> {{item.title[0]}} </FONT></v-card-title>

                <v-card-subtitle >  <FONT COLOR="black"> {{item.abstract[0]}}  <br><br> {{item.url[0]}} </FONT> </v-card-subtitle>


              

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
    name: 'iniciohistoria',
    data: () => ({
      items: null,
      curso: null,
      query:"",
      prueba:{},
      docs: [
              {
                "_version_": 1738020385406844928, 
                "abstract": [
                  "La presente c\u00e1psula, de la asignatura de Historia, Geograf\u00eda y Ciencias Sociales, aborda el Objetivo de Aprendizaje N\u00ba 09 de las Bases Curriculares. Nuestra entretenida narradora, nos invita a aprender sobre las interesantes civilizaciones Griega y Romana, donde estaban ubicadas y c\u00f3mo eran sus caracter\u00edsticas y condiciones geogr\u00e1ficas."
                ], 
                "grade": [
                  3
                ], 
                "id": "51e60517-ab57-45b4-8921-e7a2cac96e6f", 
                "subject": [
                  "historia"
                ], 
                "title": [
                  "Ubicaci\u00f3n geogr\u00e1fica de civilizaciones Griega y Romana/Historia, Geograf\u00eda y Cs. Sociales"
                ], 
                "topic": [
                  "civilizaciones"
                ], 
                "type": [
                  "video"
                ], 
                "url": [
                  "https://www.youtube.com/watch?v=e9c_3_pXKJY&ab_channel=MinisteriodeEducaci%C3%B3nGobiernodeChile"
                ]
              },
              {
        "_version_": 1738257594480328704, 
        "abstract": [
          "\u00bfA qu\u00e9 esperas? \u00bfSab\u00edas que el cepillo, la pasta de dientes, y muchas m\u00e1s\ncosas que todav\u00eda utilizamos, fueron inventadas por los \nantiguos egipcios?"
        ], 
        "format": [
          "video"
        ], 
        "grade": [
          3
        ], 
        "id": "0f51685a-4a58-41da-8e68-7ebe33123a77", 
        "subject": [
          "historia"
        ], 
        "title": [
          "Curiosidades del Antiguo Egipto | Videos Educativos para Ni\u00f1os.\n"
        ], 
        "topic": [
          "civilziaciones"
        ], 
        "type": [
          "contenido"
        ], 
        "url": [
          "https://www.youtube.com/watch?v=DMrlYBTaAsE&ab_channel=HappyLearningEspa%C3%B1ol"
        ]
      },  
      ] 
    }),
    methods:{
        //Función asíncrona para consultar los datos
        getData: async function(){
          try {
              
              if(this.curso==3)
                this.items={};
              var result = await this.$http.get('/historia/'+this.curso);
              this.prueba = result.data.response;
              this.items = this.prueba.docs;
              
                
                
            } catch (error) {
                console.log('error', error);
            }
          },
        toInicio () {
          this.$router.push('/');
        },
        toCursos () { 
          this.$router.push({name:'cursos', params:{id:this.curso}});
        },
        buscar: async function (){
          var result2 = await this.$http.post('/historia-consulta', {
                  "query": this.query,
                  "curso": this.curso,
                });
                 this.query = result2.data;
          this.query="";
        }
    },
    //Función que se ejecuta al cargar el componente
    created:function(){
        this.curso = document.URL.split("/")[4];
        this.getData();
    }
  }
</script>