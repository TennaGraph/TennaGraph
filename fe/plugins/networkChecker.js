export default ({store}) => {
  function updateOnlineStatus(event) {
    let networkStatus = navigator.onLine ? "online" : "offline";
    store.dispatch('app/changeNetworkStatus', networkStatus);
  }
  updateOnlineStatus();
  window.addEventListener('online',  updateOnlineStatus);
  window.addEventListener('offline', updateOnlineStatus);
}
