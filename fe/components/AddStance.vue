<template>
  <v-form ref="form" v-model="valid" @submit.prevent="addNewOpinion" lazy-validation>
    <v-layout row wrap>
        <v-flex xs3 class="px-2">
          <span>Influencer stance</span>
        </v-flex>
        <v-flex xs3 class="px-2">
          <span>Link to source</span>
        </v-flex>
        <v-flex xs3 class="px-2">
          <span>Status</span>
        </v-flex>
        <v-flex xs3 class="px-2">
          <span></span>
        </v-flex>

        <v-flex xs3 class="px-2">
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
        <v-flex xs3 class="px-2">
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
        <v-flex xs3 class="px-2">
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
        <v-flex xs3>
          <v-btn class="mx-2" color="primary" @click="addNewOpinion">Add</v-btn>
        </v-flex>
    </v-layout>
  </v-form>
</template>

<script>

  import commonErrorsMixin from "~/mixins/commonErrorsMixin";

  export default {
    name: "add-stance",
    mixins: [
      commonErrorsMixin,
    ],
    data() {
      return {
        valid: false,
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
        this.$refs.form.reset();
        if (!this.$refs.form.validate()) { return; }

        let data = {
          'author':   this.author,
          'post_url': this.link,
          'choice':   this.choice,
        };

        try {
          await this.$store.dispatch('stance/createStance', data)
        } catch (e) {
          this.setResponseErrors(e, ['author', 'post_url', 'choice']);
        }

      }
    }
  }
</script>

<style scoped>

</style>
