# Client Side

## Steps from scratch

### Install nodejs, yarn

```
conda install nodejs
npm install -g yarn
yarn global add yrm
echo 'export PATH=~/.yarn/bin:$PATH' >> ~/.bashrc
. ~/.bashrc
yrm use taobao
```


### Create a vue app

```
yarn global add @vue/cli
vue create client
# vue 2, yarn
cd client
```

### Install CSS framework (Tailwind CSS)

https://tailwindcss.com/docs/installation

```
# tailwindcss>=2.0 requires node>=12.13.0
yarn add tailwindcss@1.9.0 postcss@7 autoprefixer@9
```

add new file under `client/`
```
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  }
}
```

create tailwindcss configuration file

```
npx tailwindcss init
```

import tailwindcss

```
mkdir src/styles
// src/styles/index.css
@tailwind base;
@tailwind components;
@tailwind utilities;
// add this line to `src/main.js`
import './assets/styles/index.css';
```

### Multiple pages

```
vue add router
```

define page (`src/views/*.vue`) mappings in `src/routerindex.js`


### Launch client

```
yarn serve
```

### Modify Home.vue

- reference: https://tailwindcss.com/docs

You need some basic knowledge about html, css and javascript. Learn them in https://www.w3school.com.cn/

### Interact with server (APIs)

```
yarn add axios
```

the port of `api` must be matched with the port of server (Flask's `app.run`)

```js
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
```
