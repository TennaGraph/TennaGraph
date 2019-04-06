<template>
  <v-form ref="form" v-model="valid" @submit.prevent="addNewOpinion" lazy-validation>
    <v-layout row wrap justify-space-between>

        <v-flex xs12 sm4 class="px-2">
          <label for="" class="label--text body-1 mb-1 d-block">Author of the stance</label>
          <v-layout row wrap justify-space-between>
            <v-flex row xs3>
              <v-select
                class="elevation-0"
                label="Not being sorted"
                :items="authorSocialNetworks"
                v-model="authorFromSocial"
                item-text="text"
                solo
              >
                <template slot="selection" slot-scope="data">
                  <v-flex xs2>
                    <v-avatar size="25px">
                      <img :src="data.item.iconUrl"/>
                    </v-avatar>
                  </v-flex>
                </template>
                <template slot="item" slot-scope="data">
                  <v-list-tile-avatar>
                    <img :src="data.item.iconUrl" />
                  </v-list-tile-avatar>
                  <v-list-tile-content>
                    <v-list-tile-title v-html="data.item.text"></v-list-tile-title>
                  </v-list-tile-content>
                </template>
              </v-select>
            </v-flex>

            <v-flex row xs9 class="px-2">
              <v-text-field
                v-model="author"
                :rules="authorRules"
                :error-messages="formErrors.author"
                label="VitalikButerin"
                placeholder="VitalikButerin"
                prefix="@"
                single-line
                solo
                required
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex xs12 sm3 class="px-2">
          <label for="" class="label--text body-1 mb-1 d-block">Link to source</label>
          <v-text-field
            v-model="link"
            :rules="linkRules"
            :error-messages="formErrors.post_url"
            placeholder="https://..."
            single-line
            solo
            required
          ></v-text-field>
        </v-flex>

        <v-flex xs12 sm2 class="px-2">
          <label for="" class="label--text body-1 mb-1 d-block">Status</label>
          <v-select
              v-model="choice"
              :items="choiceOptions"
              :rules="choiceRules"
              :error-messages="formErrors.choice"
              placeholder="Status"
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
        authorFromSocial: 'TWITTER',
        authorRules: [
          v => !!v || 'Twitter username is required',
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

        authorSocialNetworks: [
          { text: 'Twitter', value: 'TWITTER', iconUrl: '/icons/twitter.png' },
          { text: 'Peepeth', value: 'PEEPETH', iconUrl: '/icons/peepeth.png' },
        ],
      }
    },
    methods: {
      async addNewOpinion() {
        if (!this.$refs.form.validate()) { return; }

        let data = {
          'author':    '@' + this.author,
          'proof_url': this.link,
          'author_from_social': this.authorFromSocial,
          'choice':    this.choice,
          'eip_num':    this.eipId,
        };

        this.isStanceSending = true;
        try {
          await this.$store.dispatch('stance/createStance', data);
          this.author = '';
          this.link = '';
          this.choice = '';
          this.$refs.form.resetValidation();
          this.setSuccessAlerts(["Your submission was successfully added for review"])
        } catch (e) {
          this.setResponseErrors(e, ['author', 'post_url', 'choice']);
        }
        this.isStanceSending = false;
      }
    },
  }
</script>

<style scoped>

</style>
