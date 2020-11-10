<template>
  <div class="container" id="app-harvest">

    <form @submit.prevent="submitForm">
      <div class="form-group row" style="padding-left:9em;">
        <input type="text" class="form-control col-3 mx-2" placeholder="Descrição" v-model="specie.description">
        <button class="btn btn-success col-3 mx-2">Adicionar</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Id</th>
        <th>Descrição</th>
      </thead>
      <tbody>
        <tr v-for="specie in species" :key="specie.id" @dblclick="$data.specie = specie">
          <td>{{ specie.id }}</td>
          <td>{{ specie.description }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="removeSpecie(specie)">x</button>
          </td>
        </tr>
      </tbody>
    </table>

    <button class="btn btn-primary col-3 mx-2"><router-link style="text-decoration:none; color:white;" class="nav-link" to="/">Voltar</router-link></button>
  </div>
</template>

<script>

export default {
  name: 'app-harvest',
  data() {
    return {
      specie: {},
      species: []
    }
  },

  async created() {
    this.getData();
  },

  methods: {

    submitForm() {
      if (this.specie.id === undefined) {
        this.createSpecie();
      } else {
        this.editSpecie();
      }
    },

    async createSpecie() {
      await this.getData();
      await fetch('http://localhost:8000/api/specie/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.specie)
      });
      await this.getData();
    },
    
    async editSpecie() {
      await this.getData();
      await fetch(`http://localhost:8000/api/specie/${this.specie.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.specie)
      });
      await this.getData();
      this.specie = {};
    },

    async removeSpecie(specie) {
      await this.getData()
      
      await fetch(`http://localhost:8000/api/specie/${specie.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      
      await this.getData();
    },

    async getData() {
      var response = await fetch('http://localhost:8000/api/specie/');
      this.species = await response.json();
    }
  }
}
</script>

<style>
#app-harvest {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
