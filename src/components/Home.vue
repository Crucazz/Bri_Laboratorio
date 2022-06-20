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
        <center> <p> ¿En que curso estás? </p> </center>
    </v-col>
    </v-row>

    <v-row
      class="fill-height"
      align="center"
      justify="center"
    >
      <v-col cols="6"
          sm="6" >
          <div  @click="toTercero"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="300"
              class=" mx-auto text-center secondary text-no-wrap rounded-xl"
            >
              <v-img
                src="../assets/tercero.png"
              >
              </v-img>
            </v-card>
          
          </div>
            
      </v-col>
      <v-col cols="6"
          sm="6" >
          <div  @click="toCuarto"  class=" mx-auto text-center secondary text-no-wrap rounded-xl">
            <v-card
            max-width="300"
              class=" mx-auto text-center secondary text-no-wrap rounded-xl"
            >
              <v-img
                src="../assets/cuarto.png"
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
		name: 'Home',
		
	methods: {
		toTercero () {	
			this.$router.push({name:'cursos', params:{id:"3"}});
		},
		toCuarto () {	
			this.$router.push({name:'cursos', params:{id:"4"}});
		}
	}
		
	}
</script>

<style lang="sass" scoped>
.v-card.on-hover.theme--dark
  background-color: rgba(#FFF, 0.8)
  >.v-card__text
    color: #000
</style>