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
      { rel: 'stylesheet', type: 'text/css', href: 'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3)", href: 'theme/splashes/apple-launch-1242x2208.png' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)", href: 'theme/splashes/apple-launch-640x1136.png' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)", href: 'theme/splashes/apple-launch-750x1334.png' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)", href: 'theme/splashes/apple-launch-1125x2436.png' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)", href: 'theme/splashes/apple-launch-1536x2048.png' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)", href: 'theme/splashes/apple-launch-1668x2224.png' },
      { rel: 'apple-touch-startup-image', media: "(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)", href: 'theme/splashes/apple-launch-2048x2732.png' },
    ],
    script: [
      { src: 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js' },
      { src: "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js" }
    ]
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
  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
    'nuxt-material-design-icons',
    // Doc: https://github.com/nuxt-community/axios-module#usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
  ],
  /*
  ** Axios module configuration
  */
  axios: {
    baseURL: process.env.API_BASE_URL || "http://localhost:7000/"
  },

  workbox: {
    runtimeCaching: [
      /*** CDN APIes ***/
      {
        urlPattern: 'https://fonts.googleapis.com/.*',
        handler: 'cacheFirst',
        method: 'GET',
        strategyOptions: {
          cacheName: 'static-cache',
          cacheableResponse: {
            statuses: [0, 200]
          }
        }
      },
      {
        urlPattern: 'https://cdnjs.cloudflare.com/.*',
        handler: 'cacheFirst',
        method: 'GET',
        strategyOptions: {
          cacheName: 'static-cache',
          cacheableResponse: {
            statuses: [0, 200]
          }
        }
      },
      {
        urlPattern: 'https://ajax.googleapis.com/.*',
        handler: 'cacheFirst',
        method: 'GET',
        strategyOptions: {
          cacheName: 'static-cache',
          cacheableResponse: {
            statuses: [0, 200]
          }
        }
      },
      /*** Dashboard ***/
      {
        urlPattern: process.env.API_BASE_URL + ".*",
        handler: 'networkFirst',
        method: 'GET',
        strategyOptions: {
          cacheName: 'api-cache',
          cacheableResponse: {
            headers: { 'X-Is-Cacheable': 'true'},
            statuses: [0, 200]
          }
        }
      },
      {
        urlPattern: "https://" + process.env.AWS_BUCKET + ".s3.amazonaws.com/.*",
        handler: 'networkFirst',
        method: 'GET',
        strategyOptions: {
          cacheName: 'static-cache',
          cacheableResponse: {
            headers: { 'X-Is-Cacheable': 'true'},
            statuses: [0, 200]
          }
        }
      }
    ],
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
  }
};
