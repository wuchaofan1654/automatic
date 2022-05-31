<template>
  <div class="app-container">
    <el-col :span="6" v-for="item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]">
      <el-link
        :underline="false"
        @click="$message.error('00000000')"
      >
        <el-card class="demo-card" shadow="hover">
          <div slot="header">
            <span class="title">
              <i class="el-icon-video-play"></i>
              根据用户名称查找用户所有视频帖子根据用户名称查找用户所有视频帖子
            </span>
          </div>
          <p class="desc">小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体小字体</p>
        </el-card>
      </el-link>
    </el-col>
    <el-table></el-table>
  </div>
</template>

<script>
</script>
<style lang="scss" scoped>
.app-container{
  margin: 5px;

  p {
    font-size: 18px;
    color: #606266;
  }

  .demo-card {
    margin: 2px;

    .title {
      font-size: 16px;
      color: #409EFF;
      overflow: hidden;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 1;
    }

    .desc {
      font-size: 12px;
      overflow: hidden;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
    }
  }
}
</style>
