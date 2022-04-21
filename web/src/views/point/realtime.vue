<template>
  <el-card style="height: 90vh; margin: 10px 20px 10px 20px">
    <el-row gutter="22" style="border-bottom: 2px solid #EBEEF5; padding-bottom: 10px">
      <el-col :span="6">
        <el-input
          prefix-icon="el-icon-search"
          placeholder="关键字过滤～"
          clearable
          size="mini"
          v-model="filterDict.text">
          <template slot="prepend">
            <el-select v-model="filterDict.type" placeholder="请选择埋点类型" style="width: 90px">
              <el-option
                v-for="item in typeOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </template>
          <el-button slot="append" icon="el-icon-delete" @click="resetPoints"/>
        </el-input>
      </el-col>
      <el-col :span="18">
        <div class="right-side-header">
          <el-input
            placeholder="端口"
            size="mini"
            style="width: 200px"
            v-model="properties.port">
            <template slot="prepend">
              <span style="font-size: 13px; color: gray">{{ currentIp }}</span>
            </template>
          </el-input>
          <el-divider direction="vertical"></el-divider>
          <el-button
            size="mini"
            :type="socketInfo.type"
            icon="el-icon-video-camera-solid"
            @click="changeWebsocketStatus">
            <span :class="socketInfo.color">{{ socketInfo.text }}</span>
          </el-button>
          <el-divider direction="vertical"></el-divider>

          <el-button size="mini" :type="editInfo.type" icon="el-icon-edit" @click="changeEditStatus">
            {{ editInfo.text }}
          </el-button>
          <el-divider direction="vertical"></el-divider>

          <el-button size="mini" :type="uploadInfo.type" :icon="uploadInfo.icon" @click="updatePoints">
            {{ uploadInfo.text }}
          </el-button>
          <el-divider direction="vertical"></el-divider>

          <el-button size="mini" type="primary" icon="el-icon-refresh" @click="changeFormat">
            {{ properties.format.text }}
          </el-button>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="22">
      <el-col :span="6" style="border-right: 1px solid #EBEEF5; height: 620px; margin: 10px 0">
        <el-tree
          class="filter-tree"
          :show-checkbox="editInfo.status"
          :data="points"
          :props="defaultProps"
          default-expand-all
          :filter-node-method="filterNode"
          ref="tree">
        <span class="custom-tree-node" slot-scope="{ node, data }">
          <el-link :underline="false" :type="data.status" @click="tapPointName(data)">
            <div class="left-side-point-title">
              <i class="el-icon-document" v-if="parseInt(data.type)===2"></i>
              <i class="el-icon-thumb" v-else></i>
              <span>{{ getPointName(data) }}</span>
            </div>
          </el-link>
        </span>
        </el-tree>
      </el-col>
      <el-col :span="18">
        <div class="right-side-main">
          <div v-loading="loading" class="class-result-tags">
          <span class="result-tag" v-for="result in selectedPoint.results" :key="result.message">
            <el-tag :type="mapResultStatus(result.status)" size="mini">
              {{ result.message }}
            </el-tag>
          </span>
          </div>
          <div class="main-compare">
            <el-col :span="24">
              <div v-if="selectedPoint.type" class="main-compare-realtime">
                <div class="main-compare-title">
                  <span><i class="el-icon-timer"></i>实时信息</span>
                </div>
                <json-viewer
                  :value="simplePoint(selectedPoint)"
                  :expand-depth="5"
                  copyable
                  sort/>
              </div>
            </el-col>
            <el-col :span="12">
              <div v-loading="loading" v-if="selectedPoint.type" class="main-compare-stander">
                <div class="main-compare-title">
                  <span><i class="el-icon-s-check"></i>入库信息</span>
                </div>
                <json-viewer
                  :value="simplePoint(selectedPoint)"
                  :expand-depth="5"
                  copyable
                  sort/>
              </div>
            </el-col>
          </div>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
import store from "@/store";

export default {
  data() {
    return {
      loading: false,
      editInfo: {
        status: false,
        text: "批量编辑",
        type: "primary"
      },
      uploadInfo: {
        text: "批量同步",
        icon: "el-icon-upload",
        type: "primary"
      },
      title: '埋点信息',
      filterDict: {
        text: '',
        type: 0,
      },
      points: [],
      defaultProps: {
        label: 'from_action',
        children: 'children'
      },
      currentIp: document.location.hostname,
      properties: {
        port: 9999,
        format: {simpleYn: false, text: "详细样式"},
        hosts: [{label: "测试", value: "testst3"}, {label: "线上", value: "st3"}]
      },
      socketInfo: {
        websocketTurnOn: false,
        text: "开始录制",
        type: "success"
      },
      typeOptions: [
        {label: "全部", value: 0},
        {label: "事件", value: 1},
        {label: "页面", value: 2}
      ],
      selectedPoint: {},
    };
  },
  created() {
  },
  watch: {
    "filterDict.text": {
      handler() {
        this.$refs.tree.filter(this.filterDict);
      }
    },
    "filterDict.type": {
      handler() {
        this.$refs.tree.filter(this.filterDict);
      }
    },
    // "points.length": {
    //   handler(newValue, oldValue) {
    //     this.$refs.tree.filter(this.filterDict);
    //   }
    // }
  },
  methods: {
    changeEditStatus() {
      this.editInfo.status = !this.editInfo.status
      this.editInfo.text = this.editInfo.status ? "全部取消" : "批量编辑"
      this.editInfo.type = this.editInfo.status ? "info" : "primary"
    },
    resetUploadInfo() {
      this.uploadInfo = {
        text: "批量同步",
        icon: "el-icon-upload",
        type: "primary"
      }
    },
    updateUploadLoading() {
      this.uploadInfo = {
        text: "同步中..",
        icon: "el-icon-loading",
        type: "primary"
      }
    },
    updateUploadDone() {
      this.uploadInfo = {
        text: "同步完成",
        icon: "el-icon-check",
        type: "success"
      }
    },
    updatePoints() {
      this.updateUploadLoading()
      setTimeout(this.updateUploadDone, 2000)
      setTimeout(this.resetUploadInfo, 4000)
      this.changeEditStatus()
    },
    initWebSocket() {
      const userId = store.getters.userId;
      const wsuri =
        "ws://127.0.0.1:8088" +
        "/point/catch/" +
        "u" + userId + "/" +
        "p" + this.properties.port + "/";
      this.websocket = new WebSocket(wsuri);
      this.websocket.onopen = this.websocketonopen;
      this.websocket.onerror = this.websocketonerror;
      this.websocket.onmessage = this.websocketonmessage;
      this.websocket.onclose = this.websocketclose;
    },
    closeWebsocket() {
      this.websocket.close();
    },
    websocketonopen() {
      this.$message.success("websocket通信启动成功～");
    },
    websocketonerror(e) {
      this.turnOffWebsocket()
      this.$message.error("websocket发生错误～" + e);
    },
    websocketonmessage(e) {
      const point = JSON.parse(e.data).message
      try {
        if (this.filterNode(this.filterDict, point)) {
          this.points.unshift(point)
        }
      } catch (e) {
      }
    },
    websocketclose(e) {
      this.$message.warning("websocket通信已关闭～");
    },
    filterNode(value, data) {
      if (!value) return true;
      return this.getPointName(data).indexOf(value.text) !== -1 && this.filterPointType(data);
    },
    getPointName(point) {
      return parseInt(point.type) === 1 ? point.from_action : point.curr_page;
    },
    filterPointType(point) {
      if (this.filterDict.type) {
        return parseInt(point.type) === this.filterDict.type
      }
      return true;
    },
    mapResultStatus(status) {
      return status === 1 ? "success" : status === 2 ? "warning" : status === 3 ? "danger" : "info";
    },
    changeFormat() {
      this.properties.format.simpleYn = !this.properties.format.simpleYn;
      this.properties.format.text = this.properties.format.simpleYn ? "精简样式" : "详细样式";
      this.simplePoint(this.selectedPoint)
    },
    changeWebsocketStatus() {
      this.socketInfo.websocketTurnOn = !this.socketInfo.websocketTurnOn
      if (this.socketInfo.websocketTurnOn) {
        this.turnOnWebsocket()
      } else {
        this.turnOffWebsocket()
      }
    },
    turnOnWebsocket() {
      if (this.socketInfo.websocketTurnOn) {
        this.socketInfo.text = "停止录制";
        this.socketInfo.type = "danger";
        this.initWebSocket();
      } else {
        this.$message.warning("websocket已处于开启状态～")
      }
    },
    turnOffWebsocket() {
      if (!this.socketInfo.websocketTurnOn) {
        this.socketInfo.text = "开始录制";
        this.socketInfo.type = "success";
        this.closeWebsocket();
      } else {
        this.$message.warning("websocket已处于关闭状态～")
      }
    },
    tapPointName(point) {
      this.selectedPoint = point;
      // this.selectedPoint.results = [
      //   {status: 2, message: "post_id缺失"},
      //   {status: 3, message: "post_type冗余"},
      //   ]
    },
    linkPointName(point) {
      return point.type === 1 ? point.from_action : point.curr_page
    },
    fetchPointCheckResult() {
      this.loading = true
    },
    getLeftSideEmptyTest() {
      if (this.socketInfo.websocketTurnOn) {
        return "无符合条件埋点～"
      } else {
        return "请先开始录制～"
      }
    },
    resetPoints() {
      this.selectedPoint = {};
      this.points = [];
      this.results = {};
    },
    simplePoint(point) {
      if (!point) {
        return {};
      } else if (!this.properties.format.simpleYn) {
        return point;
      } else {
        return {
          type: point.type,
          from_page: point.from_page,
          curr_page: point.curr_page,
          curr_page_ext: point.curr_page_ext,
          from_action: point.from_action,
          from_action_ext: point.from_action_ext
        };
      }
    },
    resetFilterWords() {
      this.$message.info('已清空～');
    },
  }
};
</script>
<style slot-scope="scope">

.left-side-point-title {
  width: 300px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.right-side-header {
  width: 100%;
  text-align: right;
  position: sticky;
  top: 0;
  z-index: 2;
  background: #fff;
}

.right-side-main {
  margin: 10px 5px 10px 5px;
}

.class-result-tags {
  padding: 10px 5px 10px 5px;
}

.result-tag {
  padding: 5px 2px 5px 2px;
}

.main-compare {
}

.main-compare-title {
  padding: 0 10px 0 10px;
  font-size: 18px;
  color: #726e6e;
}

.main-compare-realtime {
  overflow: scroll;
  border-right: 2px solid #e3e3e3;
}

.main-compare-stander::-webkit-scrollbar {
  display: none;
}

.main-compare-stander {
  overflow: scroll;
}

.main-compare-stander::-webkit-scrollbar {
  display: none;
}
</style>
