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
  async loadStances({commit}, eipNum) {
    try {
      const endpoint = 'stance?eip_num='+eipNum
      const data = await this.$axios.$get(endpoint, {eip_num: eipNum});
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
