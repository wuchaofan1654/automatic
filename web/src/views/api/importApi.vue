<template>
  <el-upload
    class="upload-demo"
    drag
    :limit="limit"
    :before-upload="handleBeforeUpload"
    :on-success="handleUploadSuccess"
    :on-exceed="handleExceed"
    :on-error="handleUploadError"
    :on-remove="handleDelete"
    :action="uploadFileUrl"
    :headers="headers"
    multiple>
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    <div class="el-upload__tip" slot="tip">只能上传harfile/json文件，且不超过{{fileSize}}M</div>
  </el-upload>
</template>

<script>
import {getToken} from "@/utils/auth";

export default {
  name: "importApi",
  props: {
    fileSize: {
      type: Number,
      default: 5
    },
    fileType: {
      type: Array,
      default: () => ["harfile", "json"]
    },
    limit: {
      type: Number,
      default: 1
    },
    show_file_list: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      uploadFileUrl: process.env.VUE_APP_BASE_API + "/system/save_file/", // 上传的图片服务器地址
      headers: {
        Authorization: "Bearer " + getToken()
      },
      fileList: []
    };
  },
  methods: {
    // 上传前校检格式和大小
    handleBeforeUpload(file) {
      // 校检文件类型
      if (this.fileType && this.fileType[0] !== "ALL") {
        let fileExtension = "";
        if (file.name.lastIndexOf(".") > -1) {
          fileExtension = file.name.slice(file.name.lastIndexOf(".") + 1);
        }
        const isTypeOk = this.fileType.some((type) => {
          if (file.type.indexOf(type) > -1) return true;
          return !!(fileExtension && fileExtension.indexOf(type) > -1);

        });
        if (!isTypeOk) {
          this.$message.error(`文件格式不正确, 请上传${this.fileType.join("/")}格式文件!`);
          return false;
        }
      }
      // 校检文件大小
      if (this.fileSize) {
        const isLt = file.size / 1024 / 1024 < this.fileSize;
        if (!isLt) {
          this.$message.error(`上传文件大小不能超过 ${this.fileSize} MB!`);
          return false;
        }
      }
      return true;
    },
    // 文件个数超出
    handleExceed() {
      this.$message.error('只允许上传' + this.limit + '个文件');
    },
    // 上传失败
    handleUploadError() {
      this.$message.error("上传失败, 请重试");
    },
    // 上传成功回调
    handleUploadSuccess(res, file) {
      if (res.code === 200) {
        this.$message.success("上传成功");
        this.$emit("input", res.data.file);
      } else {
        this.$message.error(res.msg);
      }
    },
    // 删除文件
    handleDelete(index) {
      this.fileList.splice(index, 1);
      this.$emit("input", "");
    },
    // 获取文件名称
    getFileName(name) {
      if (name.lastIndexOf("/") > -1) {
        return name.slice(name.lastIndexOf("/") + 1).toLowerCase();
      } else {
        return "";
      }
    }
  }
}
</script>

<style scoped>
.upload-demo {
  margin: 20px;
}
</style>
