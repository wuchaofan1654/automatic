<template>
  <div class="app-container">
    <el-form>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
      <el-form-item></el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "detail",
  data() {
    return {
      formData: {
        url: '',
        name: '',
        method: '',
        key_yn: '',
        status: 1,
        params: [],
        validators: [],
        extractors: []
      }
    }
  }
}
</script>

<style scoped>

</style>
