<template>
  <div class="app-container">
    <el-button
      type="success"
      icon="el-icon-plus"
      @click="dialogVisible=!dialogVisible">
      新建</el-button>
    <el-table :data="projects" style="width: 30%">
      <el-table-column prop="name"></el-table-column>
      <el-table-column prop="type"></el-table-column>
    </el-table>
    <el-dialog
      title="新建项目"
      :visible="dialogVisible">
      <el-form :model="form" :inline="true">
        <el-form-item label="项目名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="项目类型">
          <el-input v-model="form.type"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </span>
    </el-dialog>
  </div>

</template>

<script>

import {listProject, addProject} from '@/api/project/project'

export default {
  name: "index",
  data() {
    return {
      projects: [],
      dialogVisible: false,
      form: {}
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      listProject().then(res => {
        this.projects = res.data.results
      })
    },
    submit() {
      addProject(this.form).then(res => {
        this.$message.success('新建成功～')
      })
    }
  }
}
</script>

<style scoped>

</style>
