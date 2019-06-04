<template>
  <v-container class="dashboard">
    <v-layout row mt-2>
      <v-flex xs12>
        <v-layout class="d-block" px-2>
          <v-card-title class="title mb-4 mt-2 py-0 px-0">F.A.Q</v-card-title>
          <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">
            <v-card-text v-for="item in questions" :key="item.question">
              <label class="title font-weight-light" v-html="item.question"></label><br>
              <label class="body-2" v-html="item.answer"></label>
            </v-card-text>
          </v-card>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>

  export default {
    name: 'about',
    head() {
      return {
        title: "FAQ"
      }
    },
    data() {
      return {
        questions: [
          {
            question: "How Tennagraph was created / why?",
            answer: "Tennagraph is an app for creating and collecting network sentiment for better Ethereum governance.",
          },
          {
            question: "What is voting based on?",
            answer: "ETH Community members who will vote or basically anyone who will add their stance about EIP",
          },
          {
            question: "How to vote?",
            answer: "There are 3 eth addresses which belong to yay, nay and abstain. \n" +
              "Just make a transaction with 0 ETH to the eth address which you want to support.",
          },
          {
            question: "When or based on what vote ends?",
            answer: "ETH Magicians are deciding whether to add EIP into the Ethereum ecosystem or not. We are working with ETH Magicians to implement EIPs based on Tennagraph voting\n",
          },
          {
            question: "When does the voting on EIP finish?",
            answer: "When the EIP is in the chain or been accepted, voting is done. If it’s been denied voting stops.",
          },
          {
            question: "When EIP is added on Tennagraph?",
            answer: "Tennagraph automatically adds new EIPs and updates existing. You can find it in the search form and initiate voting by clicking \"Start Voting\"",
          },
          {
            question: "How can I create new proposal?",
            answer: "Create it on https://ethereum-magicians.org and then it will be added on Tennagraph",
          },
          {
            question: "How Tennagraph is updating stances?",
            answer: "We are working daily to update stances but you can easily add your stance by putting author username and a url to a post.",
          },
          {
            question: "How can I add my stance?",
            answer: "Find EIP on Tennagraph, post about it on twitter / reddit, add your username, link and stance - yat / nay / abstain.",
          },
        ]
      }
    }
  };
</script>

<style scoped>

</style>
