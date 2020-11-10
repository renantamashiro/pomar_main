<template>
  <div class="container" id="app-harvest">

    <form @submit.prevent="submitForm">
      <div class="form-group row" style="padding-left:9em;">
        <input type="text" class="form-control col-2 mx-2" placeholder="Descrição" v-model="tree.description">
        <input type="number" class="form-control col-2 mx-2" placeholder="Idade" v-model.number="tree.age">
        <select class="form-control col-2 mx-2" id="specie" name="specie" v-model="tree.specie">
          <option value="" selected>Espécie</option>
          <option value="None">------------</option>
          <option v-for="specie in species" v-bind:key="specie.id" :value="specie.id">
            <option v-if="specie === null">{{ specie }}</option>
            <option v-else>{{ specie.description }}</option></option>
        </select>
        <button class="btn btn-success col-2 mx-2">Adicionar</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Descrição</th>
        <th>Idade</th>
        <th>Espécie</th>
      </thead>
      <tbody>
        <tr v-for="tree in trees" :key="tree.id" @dblclick="$data.tree = tree">
          <td>{{ tree.description }}</td>
          <td>{{ tree.age }}</td>
          <td v-if="tree.specie === null">{{ tree.specie }}</td>
          <td v-else>{{ tree.specie.description }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="removeTree(tree)">x</button>
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
      tree: {},
      trees: [],
      species: [],
    }
  },
  async created() {
    this.getData();
  },

  methods: {
    
    submitForm() {
      if (this.tree.id === undefined) {
        this.createTree();
      } else {
        this.editTree();
      }
    },

    async getData() {
      var response_trees = await fetch('http://localhost:8000/api/tree/');
      var response_species = await fetch('http://localhost:8000/api/specie/');
      this.trees = await response_trees.json();
      this.species = await response_species.json()         
    },

    async createTree() {
      await this.getData();
      await fetch('http://localhost:8000/api/tree/new/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.tree)
      });
      await this.getData();
    },

    async editTree() {
      await this.getData();
      await fetch(`http://localhost:8000/api/tree/new/${this.tree.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.tree)
      });
      await this.getData();
      this.tree = {};
    },

    async removeTree(tree) {
      await this.getData()
      
      await fetch(`http://localhost:8000/api/tree/${tree.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      
      await this.getData();
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
