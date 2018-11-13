
export default async function ({ isHMR, app, store, route, params, error, redirect }) {
    const isLoaded = store.getters['app/isAppSettingsLoaded'];
    if(isLoaded) { return }
    await store.dispatch("app/loadAppSettings")
}
