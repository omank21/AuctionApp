<template>

  <nav class="navbar bg-dark sticky-top navbar-expand-lg navbar-dark pt-2 pb-1 border-bottom border-light">
      <div class="container">
            <a class="navbar-brand">
              <router-link to="/"><img id='logo' width="100" class="me-2 pb-2" src="logoicon.png"></router-link>
                <span class='fonttype' style="font-size: 120%;">
                  ONN Auctions           
                </span>
            </a>

            <div class="navbar-nav">
                <router-link to="/ProfilePage"><h5 class="m-3 text-light">Profile Page</h5></router-link>
                <router-link to="/ActiveListings"><h5 class="m-3 text-light">Active Listings</h5></router-link>
                <router-link to="/CreateListing"><h5 class="m-3 text-light">Create Listing</h5></router-link>
            </div>
          
            <a @click="logout" class="btn btn-outline-light">
              <i class="fas fa-sign-out-alt"></i>
              Log Out
            </a>
      </div>
  </nav>
  </template>


<script>

export default {
      methods: {
          async logout() {
            window.location.href="http://127.0.0.1:8000/logout"
        }
      }
}

</script>
