<template>
  <div>
    <div class="py-16">
      <div class="mx-auto max-w-5xl px-5 flex justify-between">
        <div class="flex flex-col sm:flex-row">
          <div class="mx-auto sm:mx-0">
            <img
              class="w-32 h-32 rounded-lg shadow-lg cursor-pointer hover:shadow-2xl transition duration-300 ease-in-out"
              :src="api + 'image?name=sample.jpg'"
              alt=""
            />
          </div>
          <div class="mt-5 sm:ml-10">
            <div class="flex">
              <div class="flex mr-5 items-center">
                <p class="text-sm text-gray-600">
                  <font-awesome-icon :icon="['far', 'edit']" />
                </p>
                <input
                  class="ml-3 appearance-none bg-transparent border-b-2 border-blue-700 text-gray-700 py-1 px-2 leading-tight focus:outline-none"
                  v-model="text"
                  type="text"
                />
              </div>
              <div class="flex">
                <div
                  class="mt-2 bg-white hover:bg-blue-700 border-blue-700 text-blue-800 hover:text-white text-sm border-2 px-3 rounded shadow cursor-pointer transition-all duration-100"
                  @click="get_response"
                >
                  Send
                </div>
              </div>
            </div>
            <div class="text-sm mt-3 flex">
              <p><font-awesome-icon :icon="['fas', 'bullhorn']" /></p>
              <p class="ml-3">{{ response }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash"; // https://lodash.com/docs

export default {
  name: "Home",
  data() {
    return {
      text: "",
      response: "",
      api:
        "http://" +
        window.location.hostname +
        ":" +
        process.env.VUE_APP_API_PORT +
        "/api/",
    };
  },
  mounted: function () {
    console.log("API server: " + this.api);
    let arr = [1, 2, 3, 4, 5];
    console.log("Shuffled array", _.shuffle(arr));
  },
  methods: {
    get_response: function () {
      var query = this.api + "text?text=" + this.text;
      axios.get(query).then((response) => {
        this.response = response.data.text;
      });
    },
  },
  computed: {},
};
</script>
