const successAlertMixin = {
  data: () => ({
    successAlerts: [],
  }),
  created: function () {

  },
  methods: {
    setSuccessAlerts(messages) {
      if (Array.isArray(messages)) {
        this.successAlerts = messages;
      } else {
        this.successAlerts = [messages];
      }
      this.$store.dispatch("ntf/displayNotifications", this.successAlerts);
    },
    cleanSuccessAlerts() {
      this.successAlerts = [];
    },
  }
};

export default successAlertMixin
