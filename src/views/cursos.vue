<template>
    <v-container max-width="900"
    class="mx-auto">
     <v-row
      class="pa-2"
      align="center"
      justify="center"
    >
      <v-col >
        <v-card
          class="pa-2"
          outlined
          tile
        >
          <v-img
            max-height="425"
            
            src="../assets/logo.png"
            >
          </v-img>
        </v-card>
      </v-col>
    </v-row>
     <v-row
      class="pa-2"
      align="center"
      justify="center"
    >
      <v-col >
        <center> <p> ¿Que asigatura quieres estudiar?</p> </center>
    </v-col>
    </v-row>

    <v-row
      class="fill-height"
      align="center"
      justify="center"
    >
      <v-col cols="6"
          sm="6" >
          <div  @click="toHistoria"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="300"
              class=" mx-auto text-center secondary text-no-wrap rounded-xl"
            >
              <v-img
                src="../assets/historia.png"
              >
              </v-img>
            </v-card>
          
          </div>
            
      </v-col>
      <v-col cols="6"
          sm="6" >
          <div  @click="toMatematicas"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="300"
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


  </v-container>
</template>


<script>
	
	export default{
		name: 'cursos',
	methods: {
		toHistoria () {
      let valor = document.URL.split("/")[4]; 
      this.$router.push({name:'iniciohistoria', params:{id:valor}});
		},
		toMatematicas () {
      let valor = document.URL.split("/")[4]; 	
			this.$router.push({name:'iniciomatematicas', params:{id:valor}});
		}
	},
		
	}
</script>

<style lang="sass" scoped>
.v-card.on-hover.theme--dark
  background-color: rgba(#FFF, 0.8)
  >.v-card__text
    color: #000
</style>