const GET_EIP_LIST_PENDING = 'GET_EIP_LIST_PENDING';
const GET_EIP_LIST_SUCCESS = 'GET_EIP_LIST_SUCCESS';
const GET_EIP_LIST_FAILURE = 'GET_EIP_LIST_FAILURE';

const SET_STATUS_FILTER = 'SET_STATUS_FILTER';
const SET_CATEGORY_FILTER = 'SET_CATEGORY_FILTER';


export const state = () => ({
  isEIPsLoading: false,
  EIPsList: [],
  filter: {
    status: {
      isEnabled: false,
      keys: []
    },
    category: {
      isEnabled: false,
      keys: []
    }
  }
});

export const getters = {
  isEIPsLoading: state => {
    return state.isEIPsLoading;
  },
  EIPsList: state => {
    return state.EIPsList;
  },
  statusFilter: state => {
    return state.filter.status;
  },
  categoryFilter: state => {
    return state.filter.category;
  },
};

export const mutations = {
  [GET_EIP_LIST_PENDING](state) {
    state.isEIPsLoading = true;
  },
  [GET_EIP_LIST_SUCCESS](state, payload) {
    state.EIPsList = payload;
    state.isEIPsLoading = false;
  },
  [GET_EIP_LIST_FAILURE](state, payload) {
    state.isEIPsLoading = false;
  },

  [SET_STATUS_FILTER](state, payload) {
    state.filter.status = payload;
  },
  [SET_CATEGORY_FILTER](state, payload) {
    state.filter.category = payload;
  },
};

export const actions = {
  async loadEIPs({commit}) {
    commit(GET_EIP_LIST_PENDING); // show spinner
    try {
      const endpoint = 'eip/';
      const data = await this.$axios.$get(endpoint);
      commit(GET_EIP_LIST_SUCCESS, data);
      return data;
    } catch (e) {
      console.error(e); // 💩
      commit(GET_EIP_LIST_FAILURE, 'failed fetching list of EIPs');
      throw e;
    }
  },

  async loadEIP({commit}, id) {
    try {
      const endpoint = 'eip/' + id + '/';
      const data = await this.$axios.$get(endpoint);
      return data;
    } catch (e) {
      console.error(e); // 💩
      throw e;
    }
  },

  setFilterStatuses({commit}, filter) {
    commit(SET_STATUS_FILTER, filter);
  },

  setFilterCategories({commit}, filter) {
    commit(SET_CATEGORY_FILTER, filter);
  },
};
