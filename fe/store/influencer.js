const GET_INFLUENCERS_LIST_PENDING = 'GET_INFLUENCERS_LIST_PENDING';
const GET_INFLUENCERS_LIST_SUCCESS = 'GET_INFLUENCERS_LIST_SUCCESS';
const GET_INFLUENCERS_LIST_FAILURE = 'GET_INFLUENCERS_LIST_FAILURE';


export const state = () => ({
  isInfluencersLoading: false,
  influencersList: [],
  cachedMapPositions: {}
});

export const getters = {
  isInfluencersLoading: state => {
    return state.isInfluencersLoading;
  },
  influencersList: state => {
    return state.influencersList;
  },
  cachedMapPositions: state => {
    return state.cachedMapPositions;
  },
};

export const mutations = {
  [GET_INFLUENCERS_LIST_PENDING](state) {
    state.isInfluencersLoading = true;
  },
  [GET_INFLUENCERS_LIST_SUCCESS](state, payload) {
    state.cachedMapPositions = {};
    for(let i=0; i<payload.length; i++) {
      const item = payload[i];
      state.cachedMapPositions[item.id] = i;
    }
    state.influencersList = payload;
    state.isInfluencersLoading = false;
  },
  [GET_INFLUENCERS_LIST_FAILURE](state, payload) {
    state.isInfluencersLoading = false;
  },
};

export const actions = {
  async loadInfluencers({commit}) {
    commit(GET_INFLUENCERS_LIST_PENDING); // show spinner
    try {
      const endpoint = 'influencer/';
      const data = await this.$axios.$get(endpoint);
      commit(GET_INFLUENCERS_LIST_SUCCESS, data);
      return data;
    } catch (e) {
      console.error(e); // 💩
      commit(GET_INFLUENCERS_LIST_FAILURE, 'failed fetching list of influencers');
      throw e;
    }
  },
};
