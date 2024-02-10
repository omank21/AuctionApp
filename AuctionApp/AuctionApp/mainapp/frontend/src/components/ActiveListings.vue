<template>



  <div class="container py-5">
    <div class="row text-center text-white mb-5">
          <div class="col-lg-7 mx-auto">
              <h1 class="text-center m-2 p-2 text-light">Active Listings</h1>
          </div>  
    </div>





    <div class="input-group mb-4">
        <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search" aria-describedby="search-addon" v-model="searchListing" />
        <button type="button" class="btn btn-dark" @click="search">Search</button>
    </div>
    


    <div class="row">
                    <div class="col-lg-4 mx-auto mb-4">
                        <!-- List group-->
                        <ul class="list-group shadow">
                            <!-- list group item-->
                            <li class="list-group-item">
                                <!-- Custom content-->
                                <div class="media align-items-lg-center flex-column flex-lg-row p-3">
                                    <div class="media-body order-2 order-lg-1">
                                        <h3 class="text-center">Bid for an Item:</h3>
                                        <div>
                                            <label>Choose an item:</label>
                                            <select class="m-2" name="items" v-model="listing_id">
                                                <option v-for="listing in listings">{{ listing.title}}</option>
                                            </select>
                                        </div>
                                        <div class="row">
                                            <div class="col offset-md-2">
                                                <input type="number" step="1" min="0" class="form-control mt-3 mb-3" placeholder="0" v-model="new_price">
                                            </div>
                                            <div class="col offset-md-2">
                                                <button class="btn btn-danger mt-3 mb-3" @click="makeBid">Bid</button> 
                                            </div>
                                            <div>
                                            <label>Owner:</label>
                                            <select class="m-2" name="owners" v-model="receiver">
                                                <option v-for="listing in listings">{{ listing.owner}}</option>
                                            </select>
                                        </div>
                                        </div>
                                            <input class="form-control mt-1"  placeholder="Comment" v-model="text">                                             
                                            <div class="text-center">
                                                <button class="btn btn-warning mt-2 mb-1 " @click="postMessage">Message seller</button>
                                            </div>
                                                                    
                                        </div> 
                                </div> <!-- End -->
                            </li> <!-- End -->
                        </ul> <!-- End -->
                    </div>
    </div>


      <ul>
        <li v-for="listing in listings">
                <div class="row" v-if="listing.open">
                    <div class="col-lg-8 mx-auto mb-4">
                        <!-- List group-->
                        <ul class="list-group shadow">
                            <!-- list group item-->
                            <li class="list-group-item">
                                <!-- Custom content-->
                                <div class="media align-items-lg-center flex-column flex-lg-row p-3">
                                    <div class="media-body order-2 order-lg-1">
                                            <h5 class="mt-0 font-weight-bold mb-2">  {{  listing.title  }}  </h5>
                                            <p class="font-italic text-muted mb-0 small">  {{  listing.description  }}  </p>
                                            <div class="d-flex align-items-center justify-content-between mt-1">
                                                <h6 class="">Base price: <span class="font-weight-bold my-2">£{{  listing.price  }}</span>  </h6>
                                            </div>
                                            <div class="d-flex align-items-center justify-content-between mt-1">
                                                <h6>Bids : <span v-for="bid in bids"><span class="font-weight-bold my-2"  v-if="(bid.listing_id === listing.id)">£{{  bid.new_price  }} ({{  bid.user_id  }})</span></span></h6>
                                            </div>
                                            <p class="font-italic text-muted mb-0 small">Owner : <span class="fw-bold">{{ listing.owner }}</span></p>
                                                                    
                                        </div> 
                                        
                                </div> <!-- End -->
                      </li> <!-- End -->
                  </ul> <!-- End -->
              </div>
                </div>
            </li>

  </ul>
</div>




</template>

<script>
export default {
      data() {
          return {
              listings : [],
              id: "",
              title: "",
              description: "",
              price: "",
              bids: [],
              listing_id: "",
              new_price: "",
              messages: [],
              text: "",
              search: "",
          }
      },
          async created() {
              this.fetchLists()
              this.fetchBids()
              
          },
          methods: {

            async fetchLists() {
                // Perform Ajax request to fetch listings
              let response = await fetch("http://127.0.0.1:8000/listings/", {
                  "credentials": "include",
              })
              let data = await response.json()
              this.listings = data.listings
            },
            async fetchBids() {
                // Perform Ajax request to fetch bids
              let response = await fetch("http://127.0.0.1:8000/bids/", {
                  "credentials": "include",
              })
              let data = await response.json()
              this.bids = data.bids
              console.log(this.bids)
              const bids_val = Object.values(this.bids)
              console.log(bids_val)
              const max = Math.max(bids_val)
              console.log(max)
            },
            async makeBid() {
                // Perform Ajax request to post bid
              let response = await fetch("http://127.0.0.1:8000/bids/", {
                  "credentials": "include",
                headers : { "X-CSRFToken" : csrftoken },
                method: "POST",
                body: JSON.stringify({
                listing_id: this.listing_id,
                user_id : this.user_id,
                new_price : this.new_price,})
            });
            let response2 = await fetch("http://127.0.0.1:8000/bids/", {
                  "credentials": "include",
              })
            let data = await response2.json()
            this.bids = data.bids
            return response.json();
            },
            async postMessage() {
                // Perform Ajax request to post message
                let response = await fetch("http://127.0.0.1:8000/message/", {
                  "credentials": "include",
                headers : { "X-CSRFToken" : csrftoken },
                method: "POST",
                body: JSON.stringify({
                listing_id: this.listing_id,
                receiver: this.receiver,
                text : this.text,
                })
            });
            return response.json(); 
            
            },
            async search() {
                // Perform Ajax request to search
                let response = await fetch("http://127.0.0.1:8000/listings/", {
                  "credentials": "include",
                headers : { "X-CSRFToken" : csrftoken },
                method: "POST",
                body: JSON.stringify({
                searchListing: this.searchListing,})
                })
              let data = await response.json()
              this.listings = data.listings
              data.listings.filter(this.search)
            return response.json(); 
            
            }


          }
}
</script>
