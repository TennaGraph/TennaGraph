const pkg = require('./package');
const path = require('path');

const nodeExternals = require('webpack-node-externals');

module.exports = {
  // mode: 'universal',
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: process.env.HEAD_TITLE,
    meta: [
      { charset: 'utf-8' },
      { name: 'apple-mobile-web-app-capable', content: 'yes' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/theme/favicon.png' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons' },
    ],
  },

  meta: {
    name: process.env.HEAD_TITLE,
    description: process.env.HEAD_DESCRIPTION,
    nativeUI: true,
  },

  manifest: {
    name: process.env.HEAD_TITLE,
    short_name: process.env.HEAD_TITLE,
    description: process.env.HEAD_DESCRIPTION,
  },

  /*
  ** This module automatically generates app icons and favicon with different sizes
   */
  icon: {
   iconSrc: path.resolve('static', 'theme', 'icon.png')
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#FFFFFF' },

  /*
  ** Global CSS
  */
  css: [
    'vuetify/src/stylus/main.styl',
    'material-design-icons/iconfont/material-icons.css',
    '@/assets/common.css',
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '@/plugins/vuetify',
    '@/plugins/axios.js',
    '@/plugins/networkChecker.js',
    '@/plugins/utils.js',
    '@/plugins/apexcharts',
  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
    'nuxt-material-design-icons',
    // Doc: https://github.com/nuxt-community/axios-module#usage
    '@nuxtjs/axios',
  ],
  /*
  ** Axios module configuration
  */
  axios: {
    baseURL: process.env.API_BASE_URL || "http://localhost:7000/"
  },

  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
      if (ctx.isServer) {
        config.externals = [
          nodeExternals({
            whitelist: [/^vuetify/]
          })
        ]
      }
    },
    vendor: ['vuetify'],
  },

  render: {
    bundleRenderer: {
      shouldPreload: (file, type) => {
        return ['style'].includes(type)
      }
    }
  },

  router: {
    middleware: [
      'app_settings',
    ]
  },

  env: {
    baseUrl: process.env.API_BASE_URL,
    appEnv: process.env.APP_ENV,
    isMainNet: process.env.IS_MAIN_NET,
    web3ProviderUrl: process.env.WEB3_PROVIDER_URL,
    web3NetworkId: process.env.WEB3_NETWORK_ID,
    etherscanUrl: process.env.ETHERSCAN_URL,
  }
};
