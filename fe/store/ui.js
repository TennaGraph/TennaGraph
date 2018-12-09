const OPEN_USER_MENU = 'OPEN_USER_MENU';
const CLOSE_ALL_MENUS = 'CLOSE_ALL_MENUS';

const OPEN_QR_CODE_SIDEBAR = 'OPEN_QR_CODE_SIDEBAR';


export const state = () => ({
  isLangMenuOpened: false,
  isUserMenuOpened: false,

  isUserWalletsSidebarOpened: false,
  isProfileSidebarOpened: false,
  isQrCodeSidebarOpened: false,
  qrCode: {
    address: undefined,
    option: "Yay"
  }
});

export const getters = {
  isUserMenuOpened: state => {
    return state.isUserMenuOpened;
  },
  isSidebarOpened: state => {
    return state.isUserMenuOpened, state.isQrCodeSidebarOpened;
  },
  isQrCodeSidebarOpened: state => {
    return state.isQrCodeSidebarOpened;
  },
  qrCode: state => {
    return state.qrCode;
  }
};

export const mutations = {
  [OPEN_USER_MENU](state) {
    state.isUserMenuOpened = true;
  },
  [CLOSE_ALL_MENUS](state) {
    state.isUserMenuOpened = false;
    state.isQrCodeSidebarOpened = false;
  },
  [OPEN_QR_CODE_SIDEBAR](state, payload) {
    state.qrCode = payload;
    state.isQrCodeSidebarOpened = true;
  },
};

export const actions = {
  openUserMenu({commit}) {
    commit(OPEN_USER_MENU);
  },
  openQrCodeMenu({commit}, payload) {
    commit(OPEN_QR_CODE_SIDEBAR, payload);
  },
  closeAllMenus({commit}) {
    commit(CLOSE_ALL_MENUS);
  },
};
