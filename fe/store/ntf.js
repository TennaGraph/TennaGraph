import {uuid} from 'vue-uuid'

const SET_NOTIFICATIONS = 'SET_NOTIFICATIONS';
const CLEAR_NOTIFICATIONS = 'CLEAR_NOTIFICATIONS';
const CLOSE_NOTIFICATION = 'CLOSE_NOTIFICATION';

export const state = () => ({
  notifications: [],
});

export const getters = {
  notifications: state => {
    return state.notifications;
  }
};

export const mutations = {
  [SET_NOTIFICATIONS](state, notifications) {
    state.notifications = notifications;
  },
  [CLEAR_NOTIFICATIONS](state) {
    state.notifications = [];
  },
  [CLOSE_NOTIFICATION](state, identifier) {
    const notifications = state.notifications.filter((notification) => notification.identifier != identifier);
    state.notifications = notifications;
  }
};

export const actions = {
  displayNotifications({commit}, titles) {
    const notifications = titles.map((title) => {
      return {
        message: title,
        dismissible: true,
        identifier: uuid.v1(),
      }
    });
    commit(SET_NOTIFICATIONS, notifications);
  },
  clearNotifications({commit}) {
    commit(CLEAR_NOTIFICATIONS);
  },
  closeNotification({commit}, identifier) {
    commit(CLOSE_NOTIFICATION, identifier);
  },
};
