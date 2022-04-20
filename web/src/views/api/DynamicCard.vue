<template>
  <el-card>
    <div slot="header">
      <span>{{title}}</span>
      <el-button
        type="text"
        style="float: right"
        @click="formDataYn=!formDataYn">FormData</el-button>
    </div>
    <el-row>
      <el-col v-for="item in form" :span="item.span" class="dynamic-title">
      </el-col>
    </el-row>

  </el-card>
</template>

<script>
export default {
  name: "DynamicCard",
  props: ['title', 'form', 'formDataYn']
}
</script>

<style scoped>

</style>
