import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/HomePage.vue'
import ActiveListings from'./components/ActiveListings.vue'
import CreateListing from'./components/CreateListing.vue'
import ProfilePage from'./components/ProfilePage.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomePage,
    },
    {
        path: '/ProfilePage',
        name: 'ProfilePage',
        component: ProfilePage,
      },
    {
        path: '/ActiveListings',
        name: 'ActiveListings',
        component: ActiveListings,
      },
      {
        path: '/CreateListing',
        name: 'CreateListing',
        component: CreateListing,
      },
  ]
})