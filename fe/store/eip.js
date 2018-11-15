const GET_EIP_LIST_PENDING = 'GET_EIP_LIST_PENDING';
const GET_EIP_LIST_SUCCESS = 'GET_EIP_LIST_SUCCESS';
const GET_EIP_LIST_FAILURE = 'GET_EIP_LIST_FAILURE';


export const state = () => ({
  isEIPsLoading: false,
  EIPsList: []
});

export const getters = {
  isEIPsLoading: state => {
    return state.isEIPsLoading;
  },
  EIPsList: state => {
    return state.EIPsList;
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
};
