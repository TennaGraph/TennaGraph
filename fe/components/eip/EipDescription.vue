<template>
  <v-layout column>
    <v-flex class="px-2">
      <vue-markdown :class="{ 'bottom-gradient': isCollapsed}" :style="isCollapsed ? collapsedStyles : {}">{{ eipDescription }}</vue-markdown>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js"></script>
    </v-flex>
    <v-flex class="mt-3">
      <v-btn dark color="grey" @click="isCollapsed = !isCollapsed">{{ isCollapsed ? 'EXPAND' : 'SHOW LESS' }}</v-btn>
      <v-btn dark color="grey" @click="openOnGithub">
        Open on GitHub
        <v-icon right dark>arrow_upward</v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
  import VueMarkdown from 'vue-markdown'

  export default {
    name: "EipDescription",
    components: {
      VueMarkdown
    },
    props: {
      eipDescription: {
        type: String,
        required: true
      },
      fileName: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        isCollapsed: true,
        collapsedStyles: {height: '250px', overflow: 'hidden'}
      }
    },
    methods: {
      openOnGithub() {
        window.open("https://github.com/ethereum/EIPs/blob/master/EIPS/" + this.fileName, "_blank");
      }
    }
  }
</script>

<style scoped>
  .bottom-gradient {
    -webkit-mask-image: -webkit-gradient(linear, left 30%, left bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)))
  }

  html {
    font-family: sans-serif;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%
  }

  body {
    margin: 0
  }

  [hidden], template {
    display: none
  }


  h1 {
    margin: .67em 0;
    font-size: 2em
  }

  mark {
    color: #000;
    background: #ff0
  }

  small {
    font-size: 80%
  }

  sub, sup {
    position: relative;
    font-size: 75%;
    line-height: 0;
    vertical-align: baseline
  }

  sup {
    top: -.5em
  }

  sub {
    bottom: -.25em
  }

  img {
    border: 0
  }

  svg:not(:root) {
    overflow: hidden
  }

  figure {
    margin: 1em 40px
  }

  hr {
    height: 0;
    -webkit-box-sizing: content-box;
    -moz-box-sizing: content-box;
    box-sizing: content-box
  }

  pre {
    overflow: auto
  }

  code, kbd, pre, samp {
    font-family: monospace, monospace;
    font-size: 1em
  }

  fieldset {
    padding: .35em .625em .75em;
    margin: 0 2px;
    border: 1px solid silver
  }

  legend {
    padding: 0;
    border: 0
  }

  textarea {
    overflow: auto
  }

  optgroup {
    font-weight: 700
  }

  table {
    border-spacing: 0;
    border-collapse: collapse
  }

  td, th {
    padding: 0
  }

  /*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
  @media print {
    *, :after, :before {
      color: #000 !important;
      text-shadow: none !important;
      background: 0 0 !important;
      -webkit-box-shadow: none !important;
      box-shadow: none !important
    }

    a, a:visited {
      text-decoration: underline
    }

    a[href]:after {
      content: " (" attr(href) ")"
    }

    abbr[title]:after {
      content: " (" attr(title) ")"
    }

    a[href^="javascript:"]:after, a[href^="#"]:after {
      content: ""
    }

    blockquote, pre {
      border: 1px solid #999;
      page-break-inside: avoid
    }

    thead {
      display: table-header-group
    }

    img, tr {
      page-break-inside: avoid
    }

    img {
      max-width: 100% !important
    }

    h2, h3, p {
      orphans: 3;
      widows: 3
    }

    h2, h3 {
      page-break-after: avoid
    }

    .navbar {
      display: none
    }

    .btn > .caret, .dropup > .btn > .caret {
      border-top-color: #000 !important
    }

    .label {
      border: 1px solid #000
    }

    .table {
      border-collapse: collapse !important
    }

    .table td, .table th {
      background-color: #fff !important
    }

    .table-bordered td, .table-bordered th {
      border: 1px solid #ddd !important
    }
  }

  * {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box
  }

  :after, :before {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box
  }

  html {
    font-size: 10px;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0)
  }

  body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    line-height: 1.42857143;
    color: #333;
    background-color: #fff
  }

  button, input, select, textarea {
    font-family: inherit;
    font-size: inherit;
    line-height: inherit
  }

  a {
    color: #337ab7;
    text-decoration: none
  }

  a:focus, a:hover {
    color: #23527c;
    text-decoration: underline
  }

  a:focus {
    outline: thin dotted;
    outline: 5px auto -webkit-focus-ring-color;
    outline-offset: -2px
  }

  figure {
    margin: 0
  }

  img {
    vertical-align: middle
  }

  .carousel-inner > .item > a > img, .carousel-inner > .item > img, .img-responsive,
  .thumbnail a > img, .thumbnail > img {
    display: block;
    max-width: 100%;
    height: auto
  }

  .img-rounded {
    border-radius: 6px
  }

  .img-thumbnail {
    display: inline-block;
    max-width: 100%;
    height: auto;
    padding: 4px;
    line-height: 1.42857143;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;
    -webkit-transition: all .2s ease-in-out;
    -o-transition: all .2s ease-in-out;
    transition: all .2s ease-in-out
  }

  .img-circle {
    border-radius: 50%
  }

  hr {
    margin-top: 20px;
    margin-bottom: 20px;
    border: 0;
    border-top: 1px solid #eee
  }

  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    border: 0
  }

  .sr-only-focusable:active, .sr-only-focusable:focus {
    position: static;
    width: auto;
    height: auto;
    margin: 0;
    overflow: visible;
    clip: auto
  }

  [role=button] {
    cursor: pointer
  }

  .h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6 {
    font-family: inherit;
    font-weight: 500;
    line-height: 1.1;
    color: inherit
  }

  .h1 .small, .h1 small, .h2 .small, .h2 small, .h3 .small, .h3 small, .h4 .small,
  .h4 small, .h5 .small, .h5 small, .h6 .small, .h6 small, h1 .small, h1 small,
  h2 .small, h2 small, h3 .small, h3 small, h4 .small, h4 small, h5 .small, h5 small,
  h6 .small, h6 small {
    font-weight: 400;
    line-height: 1;
    color: #777
  }

  .h1, .h2, .h3, h1, h2, h3 {
    margin-top: 20px;
    margin-bottom: 10px
  }

  .h1 .small, .h1 small, .h2 .small, .h2 small, .h3 .small, .h3 small, h1 .small,
  h1 small, h2 .small, h2 small, h3 .small, h3 small {
    font-size: 65%
  }

  .h4, .h5, .h6, h4, h5, h6 {
    margin-top: 10px;
    margin-bottom: 10px
  }

  .h4 .small, .h4 small, .h5 .small, .h5 small, .h6 .small, .h6 small, h4 .small,
  h4 small, h5 .small, h5 small, h6 .small, h6 small {
    font-size: 75%
  }

  .h1, h1 {
    font-size: 36px
  }

  .h2, h2 {
    font-size: 30px
  }

  .h3, h3 {
    font-size: 24px
  }

  .h4, h4 {
    font-size: 18px
  }

  .h5, h5 {
    font-size: 14px
  }

  .h6, h6 {
    font-size: 12px
  }

  p {
    margin: 0 0 10px
  }

  .lead {
    margin-bottom: 20px;
    font-size: 16px;
    font-weight: 300;
    line-height: 1.4
  }

  @media (min-width: 768px) {
    .lead {
      font-size: 21px
    }
  }


  table {
    background-color: transparent
  }

  caption {
    padding-top: 8px;
    padding-bottom: 8px;
    color: #777;
    text-align: left
  }

  th {
    text-align: left
  }

  .table {
    width: 100%;
    max-width: 100%;
    margin-bottom: 20px
  }

  .table > tbody > tr > td, .table > tbody > tr > th, .table > tfoot > tr > td, .table > tfoot > tr > th,
  .table > thead > tr > td, .table > thead > tr > th {
    padding: 8px;
    line-height: 1.42857143;
    vertical-align: top;
    border-top: 1px solid #ddd
  }

  .table > thead > tr > th {
    vertical-align: bottom;
    border-bottom: 2px solid #ddd
  }

  .table > caption + thead > tr:first-child > td, .table > caption + thead > tr:first-child > th,
  .table > colgroup + thead > tr:first-child > td, .table > colgroup + thead > tr:first-child > th,
  .table > thead:first-child > tr:first-child > td, .table > thead:first-child > tr:first-child > th {
    border-top: 0
  }

  .table > tbody + tbody {
    border-top: 2px solid #ddd
  }

  .table .table {
    background-color: #fff
  }

  .table-condensed > tbody > tr > td, .table-condensed > tbody > tr > th, .table-condensed > tfoot > tr > td,
  .table-condensed > tfoot > tr > th, .table-condensed > thead > tr > td, .table-condensed > thead > tr > th {
    padding: 5px
  }

  .table-bordered {
    border: 1px solid #ddd
  }

  .table-bordered > tbody > tr > td, .table-bordered > tbody > tr > th, .table-bordered > tfoot > tr > td,
  .table-bordered > tfoot > tr > th, .table-bordered > thead > tr > td, .table-bordered > thead > tr > th {
    border: 1px solid #ddd
  }

  .table-bordered > thead > tr > td, .table-bordered > thead > tr > th {
    border-bottom-width: 2px
  }

  .table-striped > tbody > tr:nth-of-type(odd) {
    background-color: #f9f9f9
  }

  .table-hover > tbody > tr:hover {
    background-color: #f5f5f5
  }

  table col[class *

  =
  col-

  ]
  {
    position: static
  ;
    display: table-column
  ;
    float: none
  }

  table td[class *

  =
  col-

  ]
  ,
  table th[class *

  =
  col-

  ]
  {
    position: static
  ;
    display: table-cell
  ;
    float: none
  }

  .table > tbody > tr.active > td, .table > tbody > tr.active > th, .table > tbody > tr > td.active,
  .table > tbody > tr > th.active, .table > tfoot > tr.active > td, .table > tfoot > tr.active > th,
  .table > tfoot > tr > td.active, .table > tfoot > tr > th.active, .table > thead > tr.active > td,
  .table > thead > tr.active > th, .table > thead > tr > td.active, .table > thead > tr > th.active {
    background-color: #f5f5f5
  }

  .table-hover > tbody > tr.active:hover > td, .table-hover > tbody > tr.active:hover > th,
  .table-hover > tbody > tr:hover > .active, .table-hover > tbody > tr > td.active:hover,
  .table-hover > tbody > tr > th.active:hover {
    background-color: #e8e8e8
  }

  .table > tbody > tr.success > td, .table > tbody > tr.success > th, .table > tbody > tr > td.success,
  .table > tbody > tr > th.success, .table > tfoot > tr.success > td, .table > tfoot > tr.success > th,
  .table > tfoot > tr > td.success, .table > tfoot > tr > th.success, .table > thead > tr.success > td,
  .table > thead > tr.success > th, .table > thead > tr > td.success, .table > thead > tr > th.success {
    background-color: #dff0d8
  }

  .table-hover > tbody > tr.success:hover > td, .table-hover > tbody > tr.success:hover > th,
  .table-hover > tbody > tr:hover > .success, .table-hover > tbody > tr > td.success:hover,
  .table-hover > tbody > tr > th.success:hover {
    background-color: #d0e9c6
  }

  .table > tbody > tr.info > td, .table > tbody > tr.info > th, .table > tbody > tr > td.info,
  .table > tbody > tr > th.info, .table > tfoot > tr.info > td, .table > tfoot > tr.info > th,
  .table > tfoot > tr > td.info, .table > tfoot > tr > th.info, .table > thead > tr.info > td,
  .table > thead > tr.info > th, .table > thead > tr > td.info, .table > thead > tr > th.info {
    background-color: #d9edf7
  }

  .table-hover > tbody > tr.info:hover > td, .table-hover > tbody > tr.info:hover > th,
  .table-hover > tbody > tr:hover > .info, .table-hover > tbody > tr > td.info:hover,
  .table-hover > tbody > tr > th.info:hover {
    background-color: #c4e3f3
  }

  .table > tbody > tr.warning > td, .table > tbody > tr.warning > th, .table > tbody > tr > td.warning,
  .table > tbody > tr > th.warning, .table > tfoot > tr.warning > td, .table > tfoot > tr.warning > th,
  .table > tfoot > tr > td.warning, .table > tfoot > tr > th.warning, .table > thead > tr.warning > td,
  .table > thead > tr.warning > th, .table > thead > tr > td.warning, .table > thead > tr > th.warning {
    background-color: #fcf8e3
  }

  .table-hover > tbody > tr.warning:hover > td, .table-hover > tbody > tr.warning:hover > th,
  .table-hover > tbody > tr:hover > .warning, .table-hover > tbody > tr > td.warning:hover,
  .table-hover > tbody > tr > th.warning:hover {
    background-color: #faf2cc
  }

  .table > tbody > tr.danger > td, .table > tbody > tr.danger > th, .table > tbody > tr > td.danger,
  .table > tbody > tr > th.danger, .table > tfoot > tr.danger > td, .table > tfoot > tr.danger > th,
  .table > tfoot > tr > td.danger, .table > tfoot > tr > th.danger, .table > thead > tr.danger > td,
  .table > thead > tr.danger > th, .table > thead > tr > td.danger, .table > thead > tr > th.danger {
    background-color: #f2dede
  }

  .table-hover > tbody > tr.danger:hover > td, .table-hover > tbody > tr.danger:hover > th,
  .table-hover > tbody > tr:hover > .danger, .table-hover > tbody > tr > td.danger:hover,
  .table-hover > tbody > tr > th.danger:hover {
    background-color: #ebcccc
  }

  .table-responsive {
    min-height: .01%;
    overflow-x: auto
  }

</style>
