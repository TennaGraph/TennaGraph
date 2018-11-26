<template>
  <v-form ref="form" v-model="valid" @submit.prevent="addNewOpinion" lazy-validation>
    <v-layout row wrap justify-space-between>

        <v-flex xs12 sm3 class="px-2">
          <label for="" class="label--text body-1 mb-1 d-block">Influencer stance</label>
          <v-text-field
            v-model="author"
            :rules="authorRules"
            :error-messages="formErrors.author"
            label="@vbuterin"
            single-line
            solo
            required
          ></v-text-field>
        </v-flex>

        <v-flex xs12 sm3 class="px-2">
          <label for="" class="label--text body-1 mb-1 d-block">Link to source</label>
          <v-text-field
            v-model="link"
            :rules="linkRules"
            :error-messages="formErrors.post_url"
            label="https://..."
            single-line
            solo
            required
          ></v-text-field>
        </v-flex>

        <v-flex xs12 sm3 class="px-2">
          <label for="" class="label--text body-1 mb-1 d-block">Status</label>
          <v-select
              v-model="choice"
              :items="choiceOptions"
              :rules="choiceRules"
              :error-messages="formErrors.choice"
              label="Status"
              solo
              required
            ></v-select>
        </v-flex>

        <v-flex xs12 sm3 class="px-2 pt-3">
          <v-btn class="mx-2 mt-3" dark color="buttonConfirm" :disabled="isStanceSending" @click="addNewOpinion">Add</v-btn>
        </v-flex>
    </v-layout>
  </v-form>
</template>

<script>

  import commonErrorsMixin from "~/mixins/commonErrorsMixin";
  import successAlertsMixin from "~/mixins/successAlertsMixin";

  export default {
    name: "add-stance",
    mixins: [
      commonErrorsMixin,
      successAlertsMixin,
    ],
    props: {
      eipId: {
        type: [String, Number],
        required: true
      },
    },
    data() {
      return {
        valid: false,
        isStanceSending: false,
        author: '',
        authorRules: [
          v => !!v || 'Twitter username is required',
          v => /@.+/.test(v) || 'Twitter username must be valid'
        ],

        link: '',
        linkRules: [
          v => !!v || 'Link to the post is required',
        ],

        choice: '',
        choiceRules: [
          v => !!v || 'Choosing the opinion is required',
        ],

        choiceOptions: [
          { text: 'Yay',     value: 'YAY'    },
          { text: 'Nay',     value: 'NAY'    },
          { text: 'Abstain', value: 'ABSTAIN'},
        ],
      }
    },
    methods: {
      async addNewOpinion() {
        if (!this.$refs.form.validate()) { return; }

        let data = {
          'author':    this.author,
          'proof_url': this.link,
          'choice':    this.choice,
          'eip_id':    this.eipId,
        };
        this.isStanceSending = true;
        try {
          await this.$store.dispatch('stance/createStance', data);
          this.$refs.form.reset();
          this.setSuccessAlerts(["The stance was successfully added on review!"])
        } catch (e) {
          this.setResponseErrors(e, ['author', 'post_url', 'choice']);
        }
        this.isStanceSending = false;
      }
    }
  }
</script>

<style scoped>

</style>
