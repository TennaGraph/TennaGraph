const GET_STANCES_LIST_PENDING = 'GET_STANCES_LIST_PENDING';
const GET_STANCES_LIST_SUCCESS = 'GET_STANCES_LIST_SUCCESS';
const GET_STANCES_LIST_FAILURE = 'GET_STANCES_LIST_FAILURE';


export const state = () => ({
});

export const getters = {

};

export const mutations = {

};

export const actions = {
  async loadStances({commit}, eipId) {
    try {
      const endpoint = 'stance?eip_id='+eipId
      const data = await this.$axios.$get(endpoint, {eip_id: eipId});
      return data;
    } catch (e) {
      console.error(e); // 💩
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
