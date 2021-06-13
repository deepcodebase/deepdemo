<template>
  <div>
    <div class="py-16">
      <div class="mx-auto max-w-6xl">
        <div class="">
          <div class="flex">
            <div class="flex mr-5 items-center">
              <input
                class="
                  appearance-none
                  bg-transparent
                  border-b-2 border-blue-700
                  text-gray-700
                  py-1
                  px-2
                  leading-tight
                  focus:outline-none
                "
                v-model="video"
                type="text"
              />
            </div>
            <div class="flex">
              <div
                class="
                  mt-2
                  bg-white
                  hover:bg-blue-700
                  border-blue-700
                  text-blue-800
                  hover:text-white
                  text-sm
                  border-2
                  px-3
                  rounded
                  shadow
                  cursor-pointer
                  transition-all
                  duration-100
                "
                @click="random_video"
              >
                Random
              </div>
            </div>
          </div>
          <div class="text-sm mt-3">
            <p class="font-bold text-xl py-5 text-left">
              {{ video_detail.coin && video_detail.coin.class }}
            </p>
            <div class="flex justify-between">
              <video-player
                class="video-js"
                ref="videoPlayer"
                :options="playerOptions"
                :playsinline="true"
                customEventName="customstatechangedeventname"
                @timeupdate="on_time_update($event)"
              >
              </video-player>
              <div
                class="ml-5 flex flex-col items-center"
                v-if="video_detail.coin"
              >
                <p class="bg-gray-400 mb-2 rounded py-1 px-2 w-full">
                  {{ player && lodash.floor(current_time) }} /
                  {{ player && lodash.floor(video_detail.coin.duration) }}
                </p>
                <div
                  v-for="(clip, i) in video_detail.coin.annotation"
                  :key="i + clip"
                  class="flex"
                >
                  <p
                    class="
                      bg-gray-200
                      mb-2
                      rounded
                      py-1
                      px-2
                      w-12
                      flex
                      items-center
                      justify-center
                      mr-2
                    "
                  >
                    {{ clip.segment[0] }}
                  </p>
                  <p
                    class="
                      cursor-pointer
                      w-48
                      bg-gray-200
                      mb-2
                      rounded
                      py-1
                      px-2
                    "
                    v-bind:class="{
                      'bg-gray-500':
                        current_time >= clip.segment[0] &&
                        current_time <= clip.segment[1],
                    }"
                    @click="play_clip(clip.segment)"
                  >
                    {{ clip.label }}
                  </p>
                  <p
                    class="
                      bg-gray-200
                      mb-2
                      rounded
                      py-1
                      px-2
                      w-12
                      flex
                      items-center
                      justify-center
                      ml-2
                    "
                  >
                    {{ clip.segment[1] }}
                  </p>
                </div>
              </div>
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
      lodash: _,
      videos: [],
      video: "",
      video_detail: {},
      text: "",
      response: "",
      api:
        "http://" +
        window.location.hostname +
        ":" +
        process.env.VUE_APP_API_PORT +
        "/api/",
      current_time: 0,
      playerOptions: {
        // videojs options
        controls: true,
        muted: true,
        // language: "en",
        autoplay: false,
        playbackRates: [0.7, 1.0, 1.5, 2.0],
        sources: [],
        width: 720,
      },
    };
  },
  mounted: function () {
    console.log("API server: " + this.api);
    this.get_videos();
  },
  methods: {
    get_response: function () {
      var query = this.api + "text?text=" + this.text;
      axios.get(query).then((response) => {
        this.response = response.data.text;
      });
    },

    get_videos: function () {
      var query = this.api + "list";
      axios.get(query).then((response) => {
        this.videos = response.data.videos;
        this.random_video();
      });
    },

    random_video: function () {
      this.video = _.sample(this.videos);
    },

    play_clip: function (segment) {
      this.player.currentTime(segment[0]);
    },

    on_time_update: function (player) {
      this.current_time = player.currentTime();
    },
  },
  computed: {
    video_src: function () {
      if (this.video_detail.coin) {
        return this.api + "video_src/" + this.video_detail.name;
      } else {
        return "";
      }
    },
    player() {
      return this.$refs.videoPlayer.player;
    },
  },
  watch: {
    video: function () {
      if (_.includes(this.videos, this.video)) {
        var query = this.api + "video/" + this.video;
        axios.get(query).then((response) => {
          this.video_detail = response.data.data;
          this.playerOptions.sources = [
            {
              type: "video/mp4",
              src: this.video_src,
            },
          ];
        });
      }
    },
  },
};
</script>
