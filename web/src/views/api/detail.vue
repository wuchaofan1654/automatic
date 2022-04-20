<template>
  <div class="app-container">
    <el-form ref="detailForm" :model="form" label-width="80px">
      <el-card class="box-card">
        <div slot="header" style="height: 32px">
          基础信息
          <div style="float: right">
            <el-button
              type="warning"
              @click="resetForm">重置
            </el-button>
            <el-button
              type="success"
              @click="submitForm">保存
            </el-button>
          </div>
        </div>
        <el-row>
          <el-col :span="8">
            <el-form-item label="接口名称">
              <el-input
                v-model="form.name"
                placeholder="请输入接口名称"
                clearable
                size="small"
                @keyup.enter.native="checkIsApiNameUnique"/>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-form-item label="接口url">
              <el-input
                v-model="form.url"
                placeholder="请输入接口url"
                clearable
                size="small"/>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="5">
            <el-form-item label="所属团队">
              <el-select v-model="form.dept" placeholder="请选择">
                <el-option v-for="item in deptOptions" :label="item.deptName" :value="item.id"/>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="所属模块">
              <el-select v-model="form.module" placeholder="请选择">
                <el-option v-for="item in moduleOptions" :label="item.moduleName" :value="item.id"/>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="接口状态">
              <el-radio-group
                v-model="form.status">
                <el-radio v-for="item in statusOptions" :label="item.value">{{item.label}}</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="核心接口">
              <el-radio-group
                v-model="form.key_yn">
                <el-radio v-for="item in keyYnOptions" :label="item.value">{{item.label}}</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
      </el-card>
      <el-card class="box-card">
        <div slot="header">
          参数数据
          <el-button icon="el-icon-plus" type="text" @click="addParam">新增</el-button>
          <el-radio-group
            size="mini"
            style="float: right"
            v-model="paramsFormDataYn">
            <el-radio :label="false">key-value</el-radio>
            <el-radio :label="true">form-data</el-radio>
          </el-radio-group>
        </div>
        <div v-if="!paramsFormDataYn">
          <el-row>
            <el-col :span="4" class="dynamic-title">
              <span>参数类型</span>
            </el-col>
            <el-col :span="6" class="dynamic-title">
              <span>参数key</span>
            </el-col>
            <el-col :span="6" class="dynamic-title">
              <span>参数value</span>
            </el-col>
          </el-row>
          <el-row v-for="param in form.params">
            <el-col :span="4" class="dynamic-body">
              <el-select v-model="param.type">
                <el-option v-for="item in paramTypeOptions" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-col>
            <el-col :span="6" class="dynamic-body">
              <el-input v-model="param.key"></el-input>
            </el-col>
            <el-col :span="6" class="dynamic-body" style="text-align: center">
              <el-input v-if="param.type !== 5" v-model="param.value"></el-input>
              <FileUpload @input="updateParamValue"></FileUpload>
            </el-col>
            <el-col :span="4" class="dynamic-body">
              <el-button-group>
                <el-button type="text" icon="el-icon-plus" @click="addParam"></el-button>
                <el-button type="text" icon="el-icon-delete" @click="removeParam(param)"></el-button>
              </el-button-group>
            </el-col>
          </el-row>
        </div>
        <el-input v-else type="textarea" v-model="form.params" :rows="6"/>
      </el-card>
      <el-card class="box-card">
        <div slot="header">
          验证器参数
          <el-button icon="el-icon-plus" type="text" @click="addValidator">新增</el-button>
          <el-radio-group
            style="float: right"
            v-model="validatorsFormDataYn">
            <el-radio :label="false">key-value</el-radio>
            <el-radio :label="true">form-data</el-radio>
          </el-radio-group>
        </div>
        <div v-if="!validatorsFormDataYn">
          <el-row>
            <el-col :span="4" class="dynamic-title">
              <span>表达式类型</span>
            </el-col>
            <el-col :span="4" class="dynamic-title">
              <span class="dynamic-title">表达式</span>
            </el-col>
            <el-col :span="4" class="dynamic-title">
              <span class="dynamic-title">比较符</span>
            </el-col>
            <el-col :span="4" class="dynamic-title">
              <span class="dynamic-title">期望值</span>
            </el-col>
          </el-row>
          <el-row v-for="validator in form.validators">
            <el-col :span="4" class="dynamic-body">
              <el-select v-model="validator.expression_type">
                <el-option v-for="item in expressionTypeOptions" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-col>
            <el-col :span="4" class="dynamic-body">
              <el-input v-model="validator.expression"></el-input>
            </el-col>
            <el-col :span="4" class="dynamic-body">
              <el-select v-model="validator.symbol">
                <el-option v-for="item in symbolOptions" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-col>
            <el-col :span="4" class="dynamic-body">
              <el-input v-model="validator.excepted"></el-input>
            </el-col>
            <el-col :span="4" class="dynamic-body">
              <el-button-group>
                <el-button type="text" icon="el-icon-plus" @click="addValidator"></el-button>
                <el-button type="text" icon="el-icon-delete" @click="removeValidator(validator)"></el-button>
              </el-button-group>
            </el-col>
          </el-row>
        </div>
        <el-input v-else type="textarea" v-model="form.validators" :rows="6"/>
      </el-card>
      <el-card class="box-card">
        <div slot="header">
          提取器参数
          <el-button icon="el-icon-plus" type="text" @click="addExtractor">新增</el-button>
          <el-radio-group
            style="float: right"
            v-model="extractorsFormDataYn">
            <el-radio :label="false">key-value</el-radio>
            <el-radio :label="true">form-data</el-radio>
          </el-radio-group>
        </div>
        <div v-if="!extractorsFormDataYn">
          <el-row>
            <el-col :span="4" class="dynamic-title">
              <span>表达式类型</span>
            </el-col>
            <el-col :span="6" class="dynamic-title">
              <span>表达式</span>
            </el-col>
            <el-col :span="6" class="dynamic-title">
              <span>赋值参数</span>
            </el-col>
          </el-row>
          <el-row v-for="extractor in form.extractors">
            <el-col :span="4" class="dynamic-body">
              <el-select v-model="extractor.expression_type">
                <el-option v-for="item in expressionTypeOptions" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-col>
            <el-col :span="6" class="dynamic-body">
              <el-input v-model="extractor.variable"></el-input>
            </el-col>
            <el-col :span="6" class="dynamic-body">
              <el-input v-model="extractor.expression"></el-input>
            </el-col>
            <el-col :span="4" class="dynamic-body">
              <el-button-group>
                <el-button type="text" icon="el-icon-plus" @click="addExtractor"></el-button>
                <el-button type="text" icon="el-icon-delete" @click="removeExtractor(extractor)"></el-button>
              </el-button-group>
            </el-col>
          </el-row>
        </div>
        <div v-else>
          <el-input v-model="form.extractors" type="textarea" :rows="6"></el-input>
        </div>
      </el-card>
    </el-form>
  </div>
</template>

<script>

import {getApiDetail} from "@/api/api/api";
import {listDept} from "@/api/permission/dept"
import {listModule} from "@/api/permission/module"
import FileUpload from "@/components/FileUpload/index";

const defaultForm = {
  name: '',
  url: '',
  method: 'GET',
  key_yn: 0,
  status: 1,
  dept: '',
  module: '',
  params: [],
  validators: [],
  extractors: []
}
export default {
  name: "detail",
  components: {FileUpload},
  data() {
    return {
      id: this.$route.query.id,
      form: Object.assign(defaultForm),
      paramsFormDataYn: false,
      validatorsFormDataYn: false,
      extractorsFormDataYn: false,
      paramTypeOptions: [
        {label: '字符串', value: 1},
        {label: '文件', value: 5}
      ],
      deptOptions: [],
      moduleOptions: [],
      symbolOptions: [
        {label: 'equals', value: '='},
        {label: 'equals as str', value: 'str='},
        {label: 'equals as int', value: 'int='},
        {label: 'in', value: 'in'},
        {label: 'not in', value: 'not in'},
        {label: 'contains', value: 'contains'},
        {label: 'not contains', value: 'not contains'},
        {label: 'is null', value: 'is null'},
        {label: 'not null', value: 'not null'},
      ],
      expressionTypeOptions: [
        {label: 'Json 路径', value: 1},
        {label: '正则表达式', value: 2},
        {label: 'Mysql表达式', value: 3}
      ],
      statusOptions: [{label: '正常', value: 1}, {label: '禁用', value: 0}],
      keyYnOptions: [{label: '是', value: 1}, {label: '否', value: 0}]
    }
  },
  created() {
    this.getDetail()
    this.getDept()
    this.getModule()
  },
  methods: {
    updateParamValue(data){
      console.log(data)
    },
    getDetail() {
      if (this.id) {
        getApiDetail(this.id).then(res => {
          this.form = res.data
          this.form.dept = res.data.dept.id
          this.form.module = res.data.module.id
        })
      }
    },
    getDept() {
      listDept().then(res => {
        this.deptOptions = res.data.results
      })
    },
    getModule() {
      listModule().then(res => {
        this.moduleOptions = res.data.results
      })
    },
    checkIsApiNameUnique() {
      return false
    },
    getApiStatusOptions() {

    },
    removeParam(item) {
      let index = this.form.params.indexOf(item)
      if (index !== -1) {
        this.form.params.splice(index, 1)
      }
    },
    addParam() {
      this.form.params.push({
        key: '',
        type: '',
        value: ''
      });
    },
    removeValidator(item) {
      let index = this.form.validators.indexOf(item)
      if (index !== -1) {
        this.form.params.splice(index, 1)
      }
    },
    addValidator() {
      this.form.validators.push({
        expression: '',
        expression_type: '',
        symbol: '',
        excepted: ''
      });
    },
    removeExtractor(item) {
      let index = this.form.extractors.indexOf(item)
      if (index !== -1) {
        this.form.params.splice(index, 1)
      }
    },
    addExtractor() {
      this.form.extractors.push({
        expression: '',
        expression_type: '',
        variable: ''
      });
    },
    submitForm() {
      console.log(this.form)
    },
    resetForm() {
      this.$confirm('此操作将清空已填写数据, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.form = Object.assign(defaultForm)
        this.$message({
          type: 'success',
          message: '已清空!'
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消'
        });
      });
    }
  }
}
</script>

<style scoped>
.box-card {
  margin: 5px;
}

.dynamic-title {
  font-size: 12px;
  text-align: center;
  color: gray;
}

.dynamic-body {
  margin: 3px;
}
</style>
