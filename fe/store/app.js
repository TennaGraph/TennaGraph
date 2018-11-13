
const SETTINGS_LOAD_PENDING = 'SETTINGS_LOAD_PENDING';
const SETTINGS_LOAD_SUCCESS = 'SETTINGS_LOAD_SUCCESS';
const SETTINGS_LOAD_FAILURE = 'SETTINGS_LOAD_FAILURE';

const SET_NETWORK_STATUS = 'SET_NETWORK_STATUS';

export const state = () => ({
  isAppSettingsLoaded: false,
  pending: false,
  isOnline: false,

  settings: {},
});

export const getters = {
  isAppSettingsLoaded: state => {
    return state.isAppSettingsLoaded;
  },
  isPending: state => {
    return state.pending;
  },
  isOnline: state => {
    return state.isOnline;
  },
};

export const mutations = {
  [SETTINGS_LOAD_PENDING](state) {
    state.pending = true;
  },
  [SETTINGS_LOAD_SUCCESS](state, value) {
    state.isAppSettingsLoaded = true;
    state.pending = false;
  },
  [SETTINGS_LOAD_FAILURE](state, payload) {
    state.isAppSettingsLoaded = false;
    state.pending = false;
  },

  [SET_NETWORK_STATUS](state, networkStatus) {
    state.isOnline = networkStatus === 'online';
  }
};

export const actions = {
  async loadAppSettings({commit}) {
    commit(SETTINGS_LOAD_PENDING);
    try {
      const config = { headers: { 'Authorization': '' } };
      const endpoint = '/system/settings/';
      const data = await this.$axios.$get(endpoint, config);
      commit(SETTINGS_LOAD_SUCCESS, data);
      return data;
    } catch (e) {
      console.error(e); // 💩
      commit(SETTINGS_LOAD_FAILURE, 'load withdrawal transactions failed');
      throw e;
    }
  },
  changeNetworkStatus({commit}, networkStatus) {
    commit(SET_NETWORK_STATUS, networkStatus);
  },
};
