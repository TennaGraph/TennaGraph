export default function ({ $axios, redirect, store, app }) {

  $axios.onError(error => {

    // if(error && error.response && error.response.status === 401) {
    //   // Clean current expired session
    //   store.dispatch('user/logout');
    //   store.dispatch('kyc/cleanKYCData');
    //
    //   // const loginPath = app.localePath('login');
    //   // return redirect(loginPath)
    // }
  })
}
