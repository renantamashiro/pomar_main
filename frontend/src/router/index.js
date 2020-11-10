import Vue from 'vue'
import Router from 'vue-router'
import Species from '@/components/Specie/Species'
import Trees from '@/components/Tree/Trees'
import TreeGroups from '@/components/TreeGroup/TreeGroups'
import Harvests from '@/components/Harvest/Harvests'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/trees',
      name: 'tree',
      component: Trees
    },
    {
      path: '/species',
      name: 'species',
      component: Species
    },
    {
      path: '/tree-groups',
      name: 'tree-group',
      component: TreeGroups
    },
    {
      path: '/',
      name: 'harvests',
      component: Harvests
    }
  ]
})
