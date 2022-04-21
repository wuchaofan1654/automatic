<template>
  <div>
    <editor height="300" />
    <mindmap
    v-model="data"
    style="min-height: 600px"
    :strokeWidth="1"/>
  </div>

</template>

<script>
import mindmap from '@hellowuxin/mindmap'
import Editor from "@/components/Editor/index";

export default {
  components: {Editor, mindmap },
  data: () => ({
    data: [{
      "name":"如何学习D3",
      "children": [
        {
          "name":"预备知识",
          "children": [
            { "name":"HTML & CSS" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"JavaScript" },
            { "name":"HTML & CSS" },
            { "name":"JavaScript" },
            { "name":"HTML & CSS" },
            { "name":"JavaScript" },
            { "name":"HTML & CSS" },
            { "name":"JavaScript" },
            { "name":"HTML & CSS" },
            { "name":"JavaScript" },
            { "name":"HTML & CSS" },
            { "name":"JavaScript" },
          ]
        },
        {
          "name":"安装",
          "_children": [
            { "name": "折叠节点" }
          ]
        },
        {
          "name":"进阶",
          "left": false
        },
      ]
    }]
  })
}
</script>
