<template>
  <div>
    <div class="py-16">
      <div class="mx-auto max-w-5xl px-5 flex justify-between">
        <div class="flex flex-col">
          <div class="flex mr-5 items-center">
            <p class="font-semibold pr-3 text-sm text-gray-600">Text 1</p>
            <input
              class="appearance-none bg-transparent border-b-2 border-blue-700 text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
              v-model="text1"
              type="text"
            />
          </div>
          <div class="flex mr-5 items-center">
            <p class="font-semibold pr-3 text-sm text-gray-600">Text 2</p>
            <input
              class="appearance-none bg-transparent border-b-2 border-blue-700 text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
              v-model="text2"
              type="text"
            />
          </div>
          <div
            class="mt-5 w-24 bg-white hover:bg-blue-700 border-blue-700 text-blue-800 hover:text-white text-sm border-2 py-1 px-3 rounded shadow cursor-pointer transition-all duration-100"
            @click="get_result"
          >
            Show
          </div>
          <div
            class="text-sm mt-10 text-left"
          >
          <p class="">Result</p>
          <p class="">Score: {{ result }}</p>
          <p class="">Text 1: {{ response.text1 }}</p>
          <p class="">Text 2: {{ response.text2 }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Home',
  data () {
    return {
      text1: '',
      text2: '',
      response: {},
      api: 'http://'+ window.location.hostname +':9000/api/',
    }
  },
  methods: {
    get_result: function () {
      var self = this;
      var query = this.api + 'score?t1=' + this.text1 + '&t2=' + this.text2;
      axios.get(query).then(function (response) {
        self.response = response.data;
      });
    }
  },
  computed: {
    result: function () {
      return this.response.score;
    }
  }
}
</script>
