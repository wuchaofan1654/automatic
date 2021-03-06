<template>
  <div class="app-container">
    <el-form
      ref="queryForm"
      :model="queryParams"
      :inline="true"
      style="float: right"
      label-width="68px">
      <el-form-item label="" prop="version">
        <el-input
          v-model="queryParams.version"
          placeholder="支持输入版本号过滤～"
          size="mini"
          clearable
          @keyup.enter.native="getList"/>
      </el-form-item>
      <el-form-item label="" prop="">
        <el-select
          size="mini"
          style="width: 200px"
          v-model="queryParams.module_name"
          filterable
          clearable
          placeholder="选定组件可查看趋势图～"
          @change="getList">
          <el-option
            v-for="item in moduleNameOptions"
            :key="item.id"
            :label="item.name"
            :value="item.name"/>
        </el-select>
      </el-form-item>
      <el-form-item label="" prop="">
        <el-button
          v-if="queryParams.module_name"
          size="mini"
          type="primary"
          @click="showExtend">
          查看走势图
        </el-button>
      </el-form-item>
    </el-form>
    <el-table
      :data="modules">
      <el-table-column label="组件名" align="center" sortable :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span>{{ scope.row.module_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="版本号" align="center" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <el-tag size="mini" type="info">{{ scope.row.publish.version }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="组件大小" align="center" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.module_size > 1024 * 1024" size="mini" type="danger">
            {{ dataFormat(scope.row.module_size) }}
          </el-tag>
          <el-tag v-else-if="scope.row.module_size > 0.2 * 1024" size="mini" type="warning">
            {{ dataFormat(scope.row.module_size) }}
          </el-tag>
          <el-tag v-else size="mini">{{ dataFormat(scope.row.module_size) }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="build No." align="center" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <el-tag size="mini" type="primary">{{ scope.row.publish.build_no }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" align="center" :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <span size="mini" style="color: #606266; font-size: 12px">
             <i class="el-icon-time"/>
            {{ scope.row.create_datetime }}
          </span>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      :title="title"
      :visible.sync="dialogVisible"
      width="60%"
      center>
      <line-chart v-if="dialogVisible" :x-axis="xAxis" :y-axis="yAxis"/>
      <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible=false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible=false">确 定</el-button>
        </span>
    </el-dialog>
    <el-pagination
      style="text-align: center; margin: 20px"
      :total="total"
      :page-size="queryParams.pageSize"
      :current-page="queryParams.pageNum"
      :page-sizes="pageSizes"
      :background="true"
      layout="total, sizes, prev, pager, next, jumper"
      @size-change="handleSizeChange"
      @current-change="handleCurrentPageChange"
    />
  </div>
</template>

<script>
import {listModule, get_module_options} from "@/api/performance/module"
import LineChart from "../../dashboard/LineChart";

export default {
  components: {
    LineChart,
  },
  name: "index",
  data() {
    return {
      title: '模块各版本大小',
      total: 0,
      moduleNameOptions: [],
      pageSizes: [10, 20, 50, 100],
      queryParams: {
        pageNum: 1,
        pageSize: 20,
        module_name: '',
        version: ''
      },
      xAxis: [],
      yAxis: {},
      modules: [],
      dialogVisible: false,
      chart_title: '走势图'
    }
  },
  watch: {},
  created() {
    this.queryParams.module_name = this.$route.query.module_name
    this.getModuleOptions()
    this.getList()
  },
  methods: {
    getStatus(value) {
      return value > 0 ? 'danger' : 'success'
    },
    getList() {
      listModule(this.queryParams).then(res => {
        if (res.code === 200) {
          this.modules = res.data.results
          this.total = res.data.count
        } else {
          this.modules = []
          this.$message.error('接口数据异常，请稍后再试～')
        }
      })
    },
    dataFormat(data) {
      if (Math.abs(data) > 1024 * 1024) {
        return (data / (1024 * 1024)).toFixed(1) + ' mb'
      } else {
        if (Math.abs(data) > 1024) {
          return (data / 1024).toFixed(1) + ' kb'
        } else {
          return data + ' b'
        }
      }
    },
    getModuleOptions() {
      get_module_options().then(
        res => {
          if (res.code === 200) {
            this.moduleNameOptions = res.data
            this.total = res.data.count
          } else {
            this.moduleNameOptions = []
          }
        })
    },
    showExtend() {
      this.dialogVisible = true
      let module_sizes = []
      this.xAxis = []
      this.yAxis = {}
      this.modules.forEach(module => {
        this.xAxis.unshift(module.publish.version)
        module_sizes.unshift(module.module_size)
      })
      this.yAxis.module_size = module_sizes
    },
    handleSizeChange(value) {
      this.queryParams.pageSize = value
      this.publishes = this.getList()
    },
    handleCurrentPageChange(value) {
      this.queryParams.pageNum = value
      this.publishes = this.getList()
    },
  }
}
</script>

<style scoped>
</style>
