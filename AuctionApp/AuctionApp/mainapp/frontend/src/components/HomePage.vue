<template>
<div class="text-center">
    <h1 class="text-center text-light  m-3 p-3 d-flex align-items-center justify-content-center ">Welcome to ONN Auctions!</h1>
    <h3 class="text-center text-light  m-3 p-3 d-flex align-items-center justify-content-center ">Hello {{users.username}}!</h3>
    <button class="btn btn-warning mt-4" @click="fetchMessages">View Messages</button>
</div>



<div class="row">
  <div class="col-lg-4 mx-auto mb-2 mt-4">
      <!-- List group-->
      <ul class="list-group shadow">
          <!-- list group item-->
          <li class="list-group-item">
              <!-- Custom content-->
              <div class="media align-items-lg-center flex-column flex-lg-row p-3">
                  <div class="media-body order-2 order-lg-1">
                      <h3 class="text-center">Reply to a message:</h3>
                      <div>
                          <label>Choose a user:</label>
                          <select name="users" class="m-2" v-model="receiver">
                              <option v-for="message in messages">{{ message.sender}}</option>
                          </select>
                      </div>
                      <div>
                          <label>Choose an message:</label>
                          <select name="messages" class="m-2">
                              <option v-for="message in messages">{{ message.text}}</option>
                          </select>
                      </div>
                      <div>
                          <label>Choose an item:</label>
                          <select name="items" class="m-2" v-model="listing_id">
                              <option v-for="message in messages">{{ message.listing_id}}</option>
                          </select>
                      </div>
                          <input class="form-control mt-1"  placeholder="Comment" v-model="text">                                             
                          <div class="text-center">
                              <button class="btn btn-warning mt-2 mb-1 " @click="postMessage">Reply</button>
                          </div>
                                                  
                      </div> 
              </div> <!-- End -->
          </li> <!-- End -->
      </ul> <!-- End -->
  </div>
</div>



<div class="container py-5">
<ul>
  <li v-for="message in messages">
    <div class="col-lg-8 mx-auto mb-4">
      <!-- List group-->
      <ul class="list-group shadow">
        <!-- list group item-->
        <li class="list-group-item">
          <!-- Custom content-->
          <div class="media align-items-lg-center flex-column flex-lg-row p-3">
            <div class="media-body order-2 order-lg-1">
              <h5 class="mt-0 font-weight-bold mb-2"> </h5>
              <p class="font-italic text-muted mb-0 small">   </p>
              <div >
                <h6 class="">{{ message.sender }} messaged on item: {{ message.listing_id }}</h6>
              </div>  
              <span class="text-primary fw-bold" >"{{ message.text }}"</span>  
                                                    
            </div> 
          </div> <!-- End -->
        </li> <!-- End -->
      </ul> <!-- End -->
    </div>

  </li>
</ul>
</div>

</template>
  
<script>
  export default {
  name: 'home',
  data () {
    return {
      users: [],
      username: "",
      messages: [],
      listing_id: "",
      sender: "",
      receiver: "",
    }
  },

  async created() {
              this.fetchUsers()
          },
        methods: {
          async fetchUsers(){
              // Perform Ajax request to fetch users
              let response = await fetch("http://127.0.0.1:8000/users/", {
                  "credentials": "include",
              })
              let data = await response.json()
              this.users = data.users
            },
          async fetchMessages(){
              // Perform Ajax request to fetch messages
              let response = await fetch("http://127.0.0.1:8000/message/", {
                  "credentials": "include",
              })
              let data = await response.json()
              this.messages = data.messages          
          },
          async postMessage() {
                // Perform Ajax request to post message
                let response = await fetch("http://127.0.0.1:8000/message/", {
                  "credentials": "include",
                headers : { "X-CSRFToken" : csrftoken },
                method: "POST",
                body: JSON.stringify({
                listing_id:this.listing_id,
                text : this.text,
                receiver: this.receiver
                })
            });
            return response.json(); 
            
            },
          

        }

  
}
</script>
  