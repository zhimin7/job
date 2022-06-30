<template>
  <div class="common-layout">
    <el-container>
      <el-header class="myheader"><Menu /></el-header>
      <el-main><router-view /></el-main>
    </el-container>
  </div>
</template>
<script setup>
import Menu from "@/components/DataView/Menu/menu.vue";
</script>
<style lang="scss">
.myheader {
  float: left;
  height: 60px;
  width: 100%;
  // background-color: skyblue;
}
.login_title {
  margin-top: 3px;
  font-size: 30px;
  font-weight: bold;
}
</style>
