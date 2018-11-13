const OPEN_USER_MENU = 'OPEN_USER_MENU';
const CLOSE_ALL_MENUS = 'CLOSE_ALL_MENUS';
const OPEN_USER_WALLETS_SIDEBAR = 'OPEN_USER_WALLETS_SIDEBAR';


export const state = () => ({
  isLangMenuOpened: false,
  isUserMenuOpened: false,

  isUserWalletsSidebarOpened: false,
  isProfileSidebarOpened: false,
});

export const getters = {
  isUserMenuOpened: state => {
    return state.isUserMenuOpened;
  },
  isSidebarOpened: state => {
    return  state.isUserMenuOpened;
  },
};

export const mutations = {
  [OPEN_USER_MENU](state) {
    state.isUserMenuOpened = true;
  },
  [CLOSE_ALL_MENUS](state) {
    state.isUserMenuOpened = false;
  },
  [OPEN_USER_WALLETS_SIDEBAR](state) {
    state.isUserWalletsSidebarOpened = true;
  },
};

export const actions = {
  openUserMenu({commit}) {
    commit(OPEN_USER_MENU);
  },
  closeAllMenus({commit}) {
    commit(CLOSE_ALL_MENUS);
  },
};
