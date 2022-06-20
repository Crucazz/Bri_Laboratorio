<template>
    <form @submit.prevent="handleSubmit">
        <error v-if="error" :error="error"/>
        <v-content>
            <v-card width="500" class="mx-auto mt-9">
                <v-card-title> Acceda a su cuenta </v-card-title>
                <v-card-text>
                    <v-text-field label="RUT" class="form-control" v-model="run" prepend-icon="mdi-account-circle"/>
                    <v-text-field label="Contraseña" class="form-control" v-model="password"  
                    :type="showPassword ? 'text' : 'password'" prepend-icon="mdi-lock" 
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" 
                    @click:append="showPassword = !showPassword"/>
                </v-card-text>

                <v-divider></v-divider>
                <v-card-actions>
                    <v-btn @click="handleSubmit" > Acceder </v-btn>
                </v-card-actions>
            </v-card>
        </v-content>
    </form>
</template>






<script>
    //import axios from 'axios';
    import Error from './Error.vue';
    //import reactive from 'vue';
    //import useRouter from "vue-router";

    export default {

        name: 'Login',
        components: {
            Error
        },
        
        data() {
            return{
                error: '',
                run: '',
                password: '',
                showPassword:false
            }
        },
        methods: {
            handleSubmit: async function() {
                try {
                    var result = await this.$http.post('/minManage/login', {
                        run: this.run,
                        password: this.password
                    });
                    let response = result.data; 
                    localStorage.setItem('token', response.jwt);
                    this.$cookies.set("tokken",response);
                    
                    var result2 = await this.$http.post('/minManage/user', response);
                    let response2 = result2.data; 
                    this.$store.dispatch('user', response2);
                    this.$router.push('/');
                } catch(e) {
                        this.error = 'Usuario/contraseña erroneosa'
                }
               
            }
        }
    }
</script>


