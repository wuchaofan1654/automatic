<template> 
  <div class="app-container">
    <el-tabs v-model="activeName" @tab-click="handleTabClick">
      <el-tab-pane label="环境管理" name="first">
        <el-card class="config-boxed-card">
          <div slot="header">
            <span><i class="el-icon-setting"></i> 环境配置</span>
            <el-button
              :size="configDict.size"
              icon="el-icon-edit"
              type="success"
              style="float: right; margin: 0 20px 10px 0"
              @click="addSlave">
              添加slave
            </el-button>
          </div>
            <el-row :gutter="22">
              <el-col :span="8">
                  <el-input value="127.0.0.1" :size="configDict.size" style="width: 70%; margin-right: 5px">
                    <div slot="prepend">
                      <span>master</span>
                    </div>
                  </el-input>
                  <el-input
                    :value="configDict.port"
                    :size="configDict.size"
                    placeholder="端口"
                    style="width: 25%">
                    <div slot="append">
                      <el-button icon="el-icon-plus" @click.prevent="addSlave(slave)" />
                    </div>
                  </el-input>
              </el-col>
                <el-col :span="4">
                  <el-input value="500" :size="configDict.size">
                    <div slot="prepend">
                      <span>max_wait</span>
                    </div>
                    <div slot="append">
                      <span>ms</span>
                    </div>
                  </el-input>
                </el-col>
                <el-col :span="4">
                  <el-input value="100" :size="configDict.size">
                    <div slot="prepend">
                      <span>min_wait</span>
                    </div>
                    <div slot="append">
                      <span>ms</span>
                    </div>
                  </el-input>
                </el-col>
              <el-col
                :span="8"
                v-for="(slave, index) in dynamicValidateForm.slaves">
                <div style="margin-top: 10px">
                    <el-input
                      style="width: 70%; margin-right: 5px"
                      :value="slave.value"
                      placeholder="请输入IP"
                      :size="configDict.size">
                      <div slot="prepend">
                        <span>slave{{ index + 1 }}</span>
                      </div>
                    </el-input>
                    <el-input
                      :value="slave.port"
                      :size="configDict.size"
                      placeholder="端口"
                      style="width: 25%">
                      <div slot="append">
                        <el-button icon="el-icon-delete" @click.prevent="removeSlave(slave)"/>
                      </div>
                    </el-input>
                </div>
              </el-col>
            </el-row>
        </el-card>
        <el-card class="config-boxed-card">
          <div slot="header">
            <span><i class="el-icon-menu"></i> 全局变量配置</span>
            <el-button :size="configDict.size" icon="el-icon-plus" type="text" @click="addGlobalVariable" />
          </div>
          <div class="variable-config">
            <el-row class="variable-config-header">
              <el-col class="variable-config-header-title" :span="6">变量名称</el-col>
              <el-col class="variable-config-header-title" :span="3">类型</el-col>
              <el-col class="variable-config-header-title" :span="8">值（value)</el-col>
            </el-row>
            <el-row
              class="variable-config-body"
              :gutter="22"
              v-for="(item, index) in dynamicValidateForm.globalVariables"
              :key="item.name"
              :prop="'globalVariables.' + index + '.value'">
              <el-col :span="6">
                <el-input :size="configDict.size"></el-input>
              </el-col>
              <el-col :span="3">
                <el-select :size="configDict.size" v-model="item.type" placeholder="请选择">
                  <el-option key="1" label="string" value="string"/>
                  <el-option key="2" label="int" value="int"/>
                  <el-option key="3" label="file" value="file"/>
                </el-select>
              </el-col>
              <el-col :span="8">
                <el-input :size="configDict.size" :value="item.value"></el-input>
              </el-col>
              <el-col :span="2">
                <el-button :size="configDict.size" icon="el-icon-delete" @click="removeGlobalVariable(item)" />
              </el-col>
            </el-row>
          </div>
        </el-card>
        <el-card class="config-boxed-card">
          <div slot="header">
            <span><i class="el-icon-coin"></i> csv变量配置</span>
            <el-button :size="configDict.size" icon="el-icon-plus" type="text" @click="addCsvVariable" />
          </div>
          <div class="variable-config">
            <el-row class="variable-config-header">
              <el-col class="variable-config-header-title" :span="11">变量列表</el-col>
              <el-col class="variable-config-header-title" :span="6">文件路径</el-col>
            </el-row>
            <el-row
              class="variable-config-body"
              :gutter="22"
              v-for="(item, index) in dynamicValidateForm.csvVariables"
              :key="item.name + index"
              :prop="'csvVariables.' + index + '.value'">
              <el-col :span="8">
                <el-input :size="configDict.size" :value="item.name"></el-input>
              </el-col>
              <el-col :span="6">
                <el-upload
                  :on-success="handleAvatarSuccess"
                  action="https://jsonplaceholder.typicode.com/posts/"
                  :show-file-list="false">
                  <span v-if="item.filePath" :value="item.filePath" class="avatar" />
                  <i v-else class="el-icon-plus avatar-uploader-icon">添加文件</i>
                </el-upload>
              </el-col>
              <el-col :span="2">
                <el-button :size="configDict.size" icon="el-icon-delete" @click="removeCsvVariable(item)" />
              </el-col>
            </el-row>
          </div>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="接口管理" name="second">
        <el-table v-loading="configDict.loading" :data="apiList" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55" align="center"/>
          <el-table-column label="编号" prop="id" width="80"/>
          <el-table-column label="接口名称" prop="name" :show-overflow-tooltip="true"/>
          <el-table-column label="请求url" prop="url" :show-overflow-tooltip="true"/>
          <el-table-column label="权重" prop="weight" width="100" :show-overflow-tooltip="true"/>
          <el-table-column label="状态" align="center" width="100" sortable>
            <template slot-scope="scope">
              <el-switch
                v-model="scope.row.status.toString()"
                active-value="1"
                inactive-value="0"
                disabled
                @change="handleStatusChange(scope.row)"
              />
            </template>
          </el-table-column>
          <el-table-column
            label="操作"
            align="center"
            class-name="small-padding fixed-width"
          >
            <template slot-scope="scope">
              <el-button
                v-hasPermission="['permission:role:{id}:delete']"
                size="mini"
                type="text"
                icon="el-icon-delete"
                @click="handleDelete(scope.row)"
              >删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="报告管理" name="third">
        <el-table v-loading="configDict.loading" :data="reportList" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55" align="center"/>
          <el-table-column label="编号" prop="id" width="80"/>
          <el-table-column label="报告名称" prop="name" :show-overflow-tooltip="true"/>
          <el-table-column label="状态" prop="url" :show-overflow-tooltip="true"/>
          <el-table-column label="创建时间" prop="weight" width="100" :show-overflow-tooltip="true"/>
          <el-table-column
            label="操作"
            align="center"
            class-name="small-padding fixed-width">
            <template slot-scope="scope">
              <el-button
                v-hasPermission="['permission:role:{id}:delete']"
                :size="configDict.size"
                type="text"
                icon="el-icon-delete"
                @click="handleDelete(scope.row)"
              >删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import {getApi} from '@/api/api/api'

const defaultConfig = {
  size: 'mini',
  loading: false
}

const defaultQueryParams = {
  name: null,
  owner: null,
  key_yn: null,
  status: null,
  pageNum: 1,
  pageSize: 20
};

export default {
  name: "index",
  data() {
    return {
      activeName: 'first',
      dynamicValidateForm: {
        slaves: [
          {
            key: '',
            value: ''
          }
        ],
        globalVariables: [
          {
            name: '',
            type: '',
            value: ''
          }
        ],
        csvVariables: [
          {
            name: '',
            filePath: '',
          }
        ]
      },
      apiList: [],
      reportList: [],
      queryParams: Object.assign({}, defaultQueryParams),
      configDict: Object.assign({}, defaultConfig),
    }
  },
  created() {
    this.getList();
  },
  methods: {
    handleAvatarSuccess(res, file) {
        this.dynamicValidateForm.csvVariables[0].filePath = file.name;
      },
    getList() {
      this.loading = true;
      getApi(this.queryParams).then(response => {
        this.loading = false;
        this.apiList = response.data.results;
        this.total = response.data.count
      });
    },
    /** 搜索按钮点击 */
    handleQuery() {
      this.getList()
    },
    pTypeFormat(row, column) {
      return row.key_yn === 1 ? '事件' : '页面'
    },
    // 埋点是否核心字典翻译
    keyYnFormat(row, column) {
      return row.key_yn === 1 ? '是' : '否'
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.dateRange = [];
      this.resetForm("queryForm");
      this.handleQuery();
    },
    handleSizeChange(val) {
      this.queryParams.pageNum = 1;
      this.queryParams.pageSize = val;
      this.getList();
    },
    handleCurrentChange(val) {
      this.queryParams.pageNum = val;
      this.getList();
    },
    handleStatusChange() {
      this.$router.push({path: '/apis/addApi'});
    },
    handleAdd() {

    },
    handleDelete() {

    },
    handleUpdate() {
    },
    handleDataScope() {
    },
    handleExport() {
    },
    handleSelectionChange() {
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    handleTabClick(event) {
      console.log(event)
    },
    addSlave() {
      this.dynamicValidateForm.slaves.push({
        value: '',
        key: Date.now()
      });
    },
    removeSlave(item) {
      let index = this.dynamicValidateForm.slaves.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.slaves.splice(index, 1)
      }
    },
    addGlobalVariable() {
      this.dynamicValidateForm.globalVariables.push(
        {
          name: '',
          type: '',
          value: ''
      });
    },
    removeGlobalVariable(item) {
      let index = this.dynamicValidateForm.globalVariables.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.globalVariables.splice(index, 1)
      }
    },
    addCsvVariable() {
      this.dynamicValidateForm.csvVariables.push(
        {
          name: '',
          value: ''
        }
      );
    },
    removeCsvVariable(item) {
      let index = this.dynamicValidateForm.csvVariables.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.csvVariables.splice(index, 1)
      }
    },
    uploadSucceed(response, file, fileList) {
      console.log(this.dynamicValidateForm.csvVariables)
    }
  }
}
</script>
<style>
.config-boxed-card {
  margin: 10px 0 20px 0;
}

.variable-config-header {
  font-size: 12px;
  color: #909399;
  text-align: left;
}

.variable-config-header-title {
  font-size: 12px;
  color: #909399;
  text-align: left;
  padding-left: 10px;
}

.variable-config-body {
  text-align: left;
  margin-top: 10px;
}
</style>


