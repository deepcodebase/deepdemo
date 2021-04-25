module.exports = {
  chainWebpack: (config) => {
    config
      .plugin('html')
      .tap((args) => {
        args[0].title = 'DeepDemo';
        args[0].description = 'A demo template powered by vue and flask.';
        return args;
      });
  },
}