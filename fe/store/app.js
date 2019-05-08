
const SETTINGS_LOAD_PENDING = 'SETTINGS_LOAD_PENDING';
const SETTINGS_LOAD_SUCCESS = 'SETTINGS_LOAD_SUCCESS';
const SETTINGS_LOAD_FAILURE = 'SETTINGS_LOAD_FAILURE';

const SET_NETWORK_STATUS = 'SET_NETWORK_STATUS';
const CLOSE_ABOUT_PROJECT_ALERT = 'CLOSE_ABOUT_PROJECT_ALERT';

export const state = () => ({
  isAppSettingsLoaded: false,
  pending: false,
  isOnline: false,
  appState: {
    'isAboutProjectAlertClosed': localStorage.getItem('isAboutProjectAlertClosed') || false,
  },

  settings: {
    'isMaintenance': localStorage.getItem('isMaintenance'),
    'supportEmail': localStorage.getItem('supportEmail'),
    'contractVotingManagerAddress': localStorage.getItem('contractVotingManagerAddress'),
  },
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
  isMaintenance: state => {
    return state.settings.isMaintenance;
  },
  supportEmail: state => {
    return state.settings.supportEmail;
  },
  contractVotingManagerAddress: state => {
    return state.settings.contractVotingManagerAddress;
  },
  isAboutProjectAlertClosed: state => {
    return state.appState.isAboutProjectAlertClosed;
  }
};

export const mutations = {
  [SETTINGS_LOAD_PENDING](state) {
    state.pending = true;
  },
  [SETTINGS_LOAD_SUCCESS](state, value) {
    const isMaintenance = value.is_maintenance;
    const supportEmail = value.support_email;
    const contractVotingManagerAddress = value.contract_vot_manager_address;

    // cache vars
    localStorage.setItem('isMaintenance', isMaintenance);
    localStorage.setItem('supportEmail', supportEmail);
    localStorage.setItem('contractVotingManagerAddress', contractVotingManagerAddress);

    state.settings = {
      isMaintenance: isMaintenance,
      supportEmail: supportEmail,
      contractVotingManagerAddress: contractVotingManagerAddress,
    };

    state.isAppSettingsLoaded = true;
    state.pending = false;
  },
  [SETTINGS_LOAD_FAILURE](state, payload) {
    state.isAppSettingsLoaded = false;
    state.pending = false;
  },

  [SET_NETWORK_STATUS](state, networkStatus) {
    state.isOnline = networkStatus === 'online';
  },

  [CLOSE_ABOUT_PROJECT_ALERT](state) {
    let isClosed = true;

    state.appState.isAboutProjectAlertClosed = isClosed;
    localStorage.setItem('isAboutProjectAlertClosed', isClosed);
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
  closeAlertAboutProject({commit}) {
    commit(CLOSE_ABOUT_PROJECT_ALERT);
  },
};
