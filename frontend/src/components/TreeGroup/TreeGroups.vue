<template>
  <div class="container" id="app-harvest">

    <form @submit.prevent="submitForm">
      <div class="form-group row" style="padding-left:9em;">
        <input type="text" class="form-control col-2 mx-2" placeholder="Nome" v-model="tree_group.name">
        <input type="text" class="form-control col-2 mx-2" placeholder="Descrição" v-model="tree_group.description">
        <select multiple class="form-control col-3 mx-2" id="tree" name="tree" v-model="tree_group.trees">
          <option value="" selected>Árvores</option>
          <option value="None">------------</option>
          <option v-for="tree in trees" v-bind:key="tree.id" :value="tree.id">
            <option v-if="tree === null">{{ tree }}</option>
            <option v-else>{{ tree.description }}</option></option>
        </select>

        <button class="btn btn-success col-3 mx-2">Adicionar</button>
      </div>
    </form>


    <table class="table">
      <thead>
        <th>Nome</th>
        <th>Descrição</th>
        <th>Árvores</th>
      </thead>
      <tbody>
        <tr v-for="group in tree_groups" :key="group.id" @dblclick="$data.tree_group = group">
          <td>{{ group.name }}</td>
          <td>{{ group.description }}</td>
          <td>
            <ul v-for="tree in group.trees" :key="tree.id">
              <li style="list-style-type:none">{{ tree.description }}</li>
            </ul>
          </td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="removeTreeGroup(group)">x</button>
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
      tree_group: {},
      tree_groups: [],
      trees: []
    }
  },
  async created() {
    this.getData();
  },
  methods: {
    async getData() {
      var response_trees = await fetch('http://localhost:8000/api/tree/');
      var response_tree_groups = await fetch('http://localhost:8000/api/tree-group/');
      this.trees = await response_trees.json();
      this.tree_groups = await response_tree_groups.json();
    },

    submitForm() {
      if (this.tree.id === undefined) {
        this.createTreeGroup();
      } else {
        this.editTreeGroup();
      }      
    },

    async createTreeGroup() {
      await this.getData();
      await fetch('http://localhost:8000/api/tree-group/new/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.tree_group)
      });
      await this.getData();
    },
    
    async editTreeGroup() {
      await this.getData();
      await fetch(`http://localhost:8000/api/tree-group/new/${this.tree_group.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.tree_group)
      });
      await this.getData();
      this.tree_group = {};
    },

    async removeTreeGroup(group) {
      await this.getData()
      
      await fetch(`http://localhost:8000/api/tree-group/${group.id}/`, {
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
