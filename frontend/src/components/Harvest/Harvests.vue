<template>
  <div class="container" id="app-harvest">

    <button class="btn btn-primary col-3 mx-2"><router-link style="text-decoration:none; color:white;" class="nav-link" to="/trees">Nova Árvore</router-link></button>
    <button class="btn btn-primary col-3 mx-2"><router-link style="text-decoration:none; color:white;" class="nav-link" to="/tree-groups">Novo Grupo de Árvore</router-link></button>
    <button class="btn btn-primary col-3 mx-2"><router-link style="text-decoration:none; color:white;" class="nav-link" to="/species">Nova Espécie</router-link></button>

    </br>
    <form @submit.prevent="submitForm">
      <div class="form-group row" style="padding-left:9em;padding-top:3em;">
        <input type="date" class="form-control col-3 mx-2" placeholder="Data" v-model="harvest.harvest_date">
        <input type="text" class="form-control col-3 mx-2" placeholder="Informações" v-model="harvest.info">
        <select class="form-control col-3 mx-2" id="tree" name="tree" v-model="harvest.tree">
          <option value="" selected>Árvore</option>
          <option value="None">------------</option>
          <option v-for="tree in trees" v-bind:key="tree.id" :value="tree.id">
            <option v-if="tree === null">{{ tree }}</option>
            <option v-else>{{ tree.description }}</option></option>
        </select>

        <select class="form-control col-3 mx-2" id="tree-group" name="tree-group" v-model="harvest.tree_group">
          <option value="" disabled selected>Grupo de árvore</option>
          <option value="">------------</option>
          <option v-for="group in tree_groups" v-bind:key="group.id" :value="group.id">{{ group.name }}</option>
        </select>
        <input type="number" class="form-control col-3 mx-2" placeholder="Peso Bruto" v-model.number="harvest.gross_weight">
        <button class="btn btn-success col-3 mx-2">Adicionar</button>
      </div>
    </form>
    <form @submit.prevent="filterHarvest" style="padding:1em;">
      <div class="form-group row" style="padding-left:7em;">
        <input type="text" class="form-control col-2 mx-2" placeholder="Informações" v-model="harvest_filter.info">       
        <input type="date" class="form-control col-2 mx-2" placeholder="Data" v-model="harvest_filter.harvest_date">
        <select class="form-control col-2 mx-2" id="tree" name="tree" v-model="harvest_filter.tree">
          <option value="" disabled selected>Árvore</option>
          <option value="">------------</option>
          <option v-for="tree in trees" v-bind:key="tree.id" :value="tree.id">
            <option v-if="tree === null">{{ tree }}</option>
            <option v-else>{{ tree.description }}</option></option>
        </select>
        <select class="form-control col-2 mx-2" id="tree-group" name="tree-group" v-model="harvest_filter.tree_group">
          <option value="" disabled selected>Grupo de árvore</option>
          <option value="">------------</option>
          <option v-for="group in tree_groups" v-bind:key="group.id" :value="group.id">{{ group.name }}</option>
        </select>       
        <button class="btn btn-primary col-1 mx-2">Filtrar</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Data</th>
        <th>Informações</th>
        <th>Árvore</th>
        <th>Espécie</th>
        <th>Grupo de árvores</th>
        <th>Peso bruto</th>
        <th>Excluir</th>
      </thead>
      <tbody>
        <tr v-for="harvest in harvests" :key="harvest.id" @dblclick="$data.harvest = harvest">
          <td>{{ harvest.harvest_date }}</td>
          <td>{{ harvest.info }}</td>
          <td v-if="harvest.tree === null">{{ harvest.tree }}</td>
          <td v-else>{{ harvest.tree.description }}</td>
          <td v-if="harvest.tree === null"></td>
          <td v-else-if="harvest.tree.specie === null">{{ harvest.tree.specie }}</td>
          <td v-else>{{ harvest.tree.specie.description }}</td>
          <td v-if="harvest.tree_group === null">{{ harvest.tree_group }}</td>
          <td v-else>{{ harvest.tree_group.name }}</td>
          <td>{{ harvest.gross_weight }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="removeHarvest(harvest)">x</button>
          </td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>

export default {
  name: 'app-harvest',
  data() {
    return {
      harvest: {},
      harvests: [],
      trees: [],
      tree_groups: [],
      harvest_filter: {
        'info': '',
        'harvest_date': '',
        'tree': '',
        'tree_group': ''
      },
      harvest_removed: '',
    }
  },
  async created() {
    this.getData();
  },

  methods: {
    submitForm() {
      if (this.harvest.id === undefined) {
        this.createHarvest();
      } else {
        this.editHarvest();
      }
    },

    async getData() {
      var response_harvests = await fetch('http://localhost:8000/api/harvest/');
      var response_trees = await fetch('http://localhost:8000/api/tree/');
      var response_tree_groups = await fetch('http://localhost:8000/api/tree-group/');
      this.harvests = await response_harvests.json();
      this.trees = await response_trees.json();
      this.tree_groups = await response_tree_groups.json();
    },

    async createHarvest() {
      await this.getData();

      await fetch('http://localhost:8000/api/harvest/new/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.harvest)
      });

      await this.getData();
    },

    async editHarvest() {
      await this.getData();
      
      await fetch(`http://localhost:8000/api/harvest/${this.harvest.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.harvest)
      });
      await this.getData();

      this.harvest = {};
    },

    async filterHarvest() {
      var response = await fetch(
        'http://localhost:8000/api/harvest/?info='+ this.harvest_filter.info + '&harvest_date=' +
        this.harvest_filter.harvest_date + '&tree=' + this.harvest_filter.tree + '&tree_group=' +
        this.harvest_filter.tree_group)
      this.harvests = await response.json();
    },

    async removeHarvest(harvest) {
      await this.getData()
      
      await fetch(`http://localhost:8000/api/harvest/${harvest.id}/`, {
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
