<template>



  <h1 class="text-center m-2 p-2 text-light">Create A Listing</h1>
  <div class="page-holder bg-gray-100">
        <div class="container-fluid px-lg-4 px-xl-5 contentDiv">
              <div class="page-header mb-4">
              </div>
          <section>
            <div class="row">
              <div class="col">
                <form class="card mb-4">
                  <div class="card-body">
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Title:</label>
                          <input class="form-control" type="text" placeholder="Listing Title"  v-model="title">
                        </div>
                      </div>
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Description:</label>
                          <input class="form-control" type="text" placeholder="Listing Description" v-model="description">
                        </div>
                      </div>
                    <div class="row">
                      <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Price (£):</label>
                          <input type="number" step="1" min="0" class="form-control" placeholder="0" v-model="price">
                        </div>
                        <div class="mb-4">
                          <label class="form-label">Closing time:</label>
                          <input type="time" class="m-2" v-model="closing_time">
                        </div>
                      </div>
                    </div>
                    <div class="col">
                        <div class="mb-4">
                          <label class="form-label">Item Image:</label>
                          <input type="file" class="form-control-file m-2">
                        </div>
                      </div>
                  </div>
                  <div class="card-footer text-center">
                    <button class="btn btn-primary" @click="saveNew">Post Listing</button>
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
              listings : [],
              title: "",
              description: "",
              price: "",
              closing_time: null,
          }
      },
      methods: {
          async saveNew() {
            let response = await fetch("http://127.0.0.1:8000/listings/", {
            credentials: "include",
            mode: "cors",
            referrerPolicy: "no-referrer",
            headers : { "X-CSRFToken" : csrftoken },
            method: "POST",
            body: JSON.stringify({
              title : this.title,
              description : this.description,
              price : this.price,
              closing_time: this.closing_time})
            });
            console.log(response)
            return response.json();
          },

        }
}
</script>
