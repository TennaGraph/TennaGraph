

<script>

  export default {
    name: "Zendesk",
    props: {
      zendeskKey: {
        type: String,
        required: true,
      },
    },
    data() {
        return {}
    },
    created() {
      if (!this.zendeskKey) {
        return;
      }
      /*<![CDATA[*/window.zE||(function(e,t,s){var n=window.zE=window.zEmbed=function(){n._.push(arguments)}, a=n.s=e.createElement(t),r=e.getElementsByTagName(t)[0];n.set=function(e){ n.set._.push(e)},n._=[],n.set._=[],a.async=true,a.setAttribute("charset","utf-8"), a.src="https://static.zdassets.com/ekr/asset_composer.js?key="+s, n.t=+new Date,a.type="text/javascript",r.parentNode.insertBefore(a,r)})(document,"script",this.zendeskKey);/*]]>*/
    },
  }
</script>

<style scoped>

</style>
