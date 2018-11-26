import Vue from 'vue'
import moment from 'moment';


// Filters

Vue.filter('formatDate', function (value) {
  if (!value) return '';
  return moment(String(value)).format('YYYY/MM/DD');
});

Vue.filter('formatDateTime', function (value) {
  if (!value) return '';
  return moment(String(value)).format('YYYY/MM/DD hh:mm');
});
