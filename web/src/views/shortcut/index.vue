<template>
  <div class="app-container">
    <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
      <el-form-item label="名称" prop="title">
        <el-input
          v-model="queryParams.title"
          placeholder="请输入名称"
          clearable
          size="small"
          style="width: 240px"
          @keyup.enter.native="handleQuery"/>
      </el-form-item>
      <el-form-item label="状态" prop="status">
        <el-select v-model="queryParams.status" placeholder="状态" clearable size="small">
          <el-option
            v-for="dict in PointStatusOptions"
            :key="dict.dictValue"
            :label="dict.dictLabel"
            :value="dict.dictValue"/>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-radio-group v-model="count">
          <el-radio-button label="1个"></el-radio-button>
          <el-radio-button label="2个"></el-radio-button>
          <el-radio-button label="3个"></el-radio-button>
          <el-radio-button label="4个"></el-radio-button>
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>
    <el-row class="class-shortcut-cards">
      <el-col :span="24/count" v-for="shortcut in shortcuts">
        <el-card class="class-shortcut-card" shadow="hover">
          <div slot="header" class="clearfix">
            <el-col :span="20">
              <div class="class-shortcut-card-title">
                <span style="">{{ shortcut.name }}</span>
              </div>
            </el-col>
            <el-col :span="4">
              <div class="class-shortcut-card-execute-bnt">
                <el-button
                  type="text"
                  @click="openCodeEditor(shortcut)"
                  icon="el-icon-video-play" />
              </div>
            </el-col>
          </div>

          <div class="class-shortcut-card-desc">
            <span style="color: gray;">{{ shortcut.desc }}</span>
          </div>

          <div class="class-shortcut-card-footer">
            <el-container>
              <span><i class="el-icon-time">{{ shortcut.create_datetime }}</i></span>
              <el-divider direction="vertical" />
              <i class="el-icon-lock"/> {{ shortcut.count }}
            </el-container>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-drawer
      title="我是标题"
      size="60%"
      :center="true"
      :withHeader="false"
      :visible.sync="dialogVisible"
      :before-close="handleClose">
      <code-editor v-model="command" />
    </el-drawer>
  </div>
</template>

<script>

import CodeEditor from "@/components/CodeEditor/index";

export default {
  name: "index",
  components: {CodeEditor},
  data() {
    return {
      command: 'not found',
      count: 3,
      showSearch: true,
      dialogVisible: false,
      queryParams: {},
      shortcuts: [
        {
          name: '描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3',
          id: 1,
          desc: '描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3',
          create_datetime: '2022-04-13 12:45:36',
          count: 10000,
          command: 'select * from db_tagbbs.tb_post limit 10'
        },
        {name: 'shortcut2', id: 2, desc: '描述2', create_datetime: '2022-04-13 12:45:36'},
        {
          name: 'shortcut3',
          id: 3,
          desc: '描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3',
          create_datetime: '2022-04-13 12:45:36',
          count: 10000,
          command: 'select * from db_tagbbs.tb_post limit 10'
        },
        {name: 'shortcut4', id: 4, desc: '描述4', create_datetime: '2022-04-13 12:45:36'},
        {name: 'shortcut5', id: 5, desc: '描述5', create_datetime: '2022-04-13 12:45:36'},
        {
          name: 'shortcut6',
          id: 6,
          desc: '描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3描述3',
          create_datetime: '2022-04-13 12:45:36',
          count: 10000,
          command: 'select * from db_tagbbs.tb_post limit 10'
        },
      ]
    }
  },
  methods: {
    openCodeEditor(shortcut) {
      this.dialogVisible = true
      this.command = shortcut.command
    },
    handleClose() {
      this.submit()
      this.dialogVisible = false
    },
    submit() {
      console.log(this.command)
    }
  }
}
</script>

<style scoped>
.class-shortcut-card {
  margin: 5px;
}

.class-shortcut-card-title {
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.class-shortcut-card-desc {
  overflow: hidden;
  display: -webkit-box;
  font-size: 13px;
  height: 40px;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.class-shortcut-card-execute-bnt {
  float: right;
}

.class-shortcut-card-footer {
  font-size: 12px;
  color: grey;
  text-align: left;
  padding-top: 10px;
}
</style>
