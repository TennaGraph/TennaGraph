import Vue from 'vue'
import VueAnalytics from "vue-analytics";

export default function ({ route, app }) {
  let isProd = process.env.appEnv === 'production';
  let googleAnalyticsId = process.env.googleAnalyticsId;
  let router = app.router;

  Vue.use(VueAnalytics, {
    id: googleAnalyticsId,
    router,
    autoTracking: {
      screenview: false
    },
    debug: {
      enabled: !isProd,
      sendHitTask: isProd
    }
  });

}
