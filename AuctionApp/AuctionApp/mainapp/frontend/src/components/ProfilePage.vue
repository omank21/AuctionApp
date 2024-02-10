<template>

  <h1 class="text-center m-2 p-2 text-light">Profile Page</h1>
  <div class="page-holder bg-gray-100">
        <div class="container-fluid px-lg-4 px-xl-5 contentDiv">
              <div class="page-header mb-4">
              </div>
          <section>
            <div class="row">
              <div class="col">
                <form class="card mb-4">
                  <div class="card-header">
                    <h4 class="card-heading text-center">My Profile</h4>
                  </div>
                  <div class="row">
                    <div class="card-body">

                      <div class="col text-center align-items-center"><img class="p-1" src="users.image.url" alt="Profile Picture" style="height:200px;"></div>
                        <div class="row m-2">
                          <div class="col ">
                            <div class="mb-2">
                              <label class="form-label">Username:</label>
                              {{users.username}}
                            </div>
                          </div>
                          <div class="col">
                            <div class="mb-2">
                              <label class="form-label">Email address:</label>
                              {{users.email}}
                            </div>
                          </div>
                        </div>

                        <div class="row m-2">
                          <div class="col ">
                            <div class="mb-4">
                              <label class="form-label">City:</label>
                              {{users.city}}
                            </div>
                          </div>
                          <div class="col">
                            <div class="mb-4">
                              <label class="form-label">Date of Birth:</label>
                              {{users.date_of_birth}}
                            </div>
                          </div>
                        </div>

                      </div>
                    </div>
                </form>
              </div>
              <div class="col">
                <form class="card mb-4">
                  <div class="card-header">
                    <h4 class="card-heading text-center">Edit Profile</h4>
                  </div>
                  <div class="card-body">
                    <div class="row">
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Username:</label>
                          <input class="form-control" type="text" placeholder="Username" v-model="updated_username">
                        </div>
                      </div>
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Email address:</label>
                          <input class="form-control" type="email" placeholder="Email" v-model="updated_email">
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">City:</label>
                          <input class="form-control" type="text" placeholder="City" v-model="updated_city">
                        </div>
                      </div>
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Date of Birth:</label>
                          <input class="form-control" type="text" placeholder="YYYY-MM-DD" v-model="updated_date_of_birth">
                        </div>
                      </div>
                    </div>
                    <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Profile Picture:</label>
                          <input type="file" class="form-control-file m-2" @change="onChange()">
                        </div>
                      </div>
                  </div>
                  <div class="card-footer text-center">
                    <button class="btn btn-primary" @click="updateUsers">Update Profile</button>
                  </div>
                </form>
              </div>
            </div>
          </section>
        </div>
      </div>




</template>
  
  
<script>
  export default {
      data() {
          return {
              users : [],
              updated_username: "",
              updated_email: "",
              updated_city: "",
              updated_date_of_birth: null,
          }
      },
      async created() {
              this.fetchUsers()
          },

      methods: {

            async fetchUsers() {
              // Perform Ajax request to fetch users
              let response = await fetch("http://127.0.0.1:8000/users/", {
                  "credentials": "include",
              })
              let data = await response.json()
              this.users = data.users
            },
            async updateUsers() {
              // Perform Ajax request to update users
              let response = await fetch("http://127.0.0.1:8000/users/", {
                  "credentials": "include",
                  headers : { "X-CSRFToken" : csrftoken },
                  method: "PUT",
                  body: JSON.stringify({
                    updated_username : this.updated_username,
                    updated_email : this.updated_email,
                    updated_city : this.updated_city,
                    updated_date_of_birth : this.updated_date_of_birth,
                })
              })
              let new_response = await fetch("http://127.0.0.1:8000/users/", {
                  "credentials": "include", 
              })
              let data = await new_response.json()
              this.users = data.users
              return response.json();
            },
            async fetchProfile() {
              // Perform Ajax request to fetch profile
              let response = await fetch("http://127.0.0.1:8000/profile/", {
                  "credentials": "include",
              })
              let data = await response.json()
              this.profiles = data.profiles
            },

            onChange(event) {
              console.log(event)
              console.log("Something!")
            }
          }
}
  </script>
