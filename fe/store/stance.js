const GET_STANCES_LIST_PENDING = 'GET_STANCES_LIST_PENDING';
const GET_STANCES_LIST_SUCCESS = 'GET_STANCES_LIST_SUCCESS';
const GET_STANCES_LIST_FAILURE = 'GET_STANCES_LIST_FAILURE';


export const state = () => ({
  isStancesLoading: false,
  stancesList: []
});

export const getters = {
  isStancesLoading: state => {
    return state.isStancesLoading;
  },
  stancesList: state => {
    return state.stancesList;
  },
};

export const mutations = {
  [GET_STANCES_LIST_PENDING](state) {
    state.isStancesLoading = true;
  },
  [GET_STANCES_LIST_SUCCESS](state, payload) {
    state.stancesList = payload;
    state.isStancesLoading = false;
  },
  [GET_STANCES_LIST_FAILURE](state, payload) {
    state.isStancesLoading = false;
  },
};

export const actions = {
  async loadStances({commit}) {
    commit(GET_STANCES_LIST_PENDING); // show spinner
    try {
      const endpoint = 'stance/';
      const data = await this.$axios.$get(endpoint);
      commit(GET_STANCES_LIST_SUCCESS, data);
      return data;
    } catch (e) {
      console.error(e); // 💩
      commit(GET_STANCES_LIST_FAILURE, 'failed fetching list stances');
      throw e;
    }
  },

  async createStance({commit}, payload) {
    try {
      const endpoint = 'stance/';
      const data = await this.$axios.post(endpoint, payload);
      return data;
    } catch (e) {
      console.error(e); // 💩
      throw e;
    }
  },
};
