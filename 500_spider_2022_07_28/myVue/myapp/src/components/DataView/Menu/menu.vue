<template>
  <el-menu
    :default-active="defaultActive"
    class="el-menu-demo"
    mode="horizontal"
    router
    unique-opened
  >
    <div class="login_title">500彩票数据</div>
    <el-menu-item index="/">历史数据</el-menu-item>
    <el-menu-item index="/manualspider">实时启动数据</el-menu-item>
    <el-menu-item index="/immediate">即时数据</el-menu-item>
    <el-menu-item index="/front30">30分钟数据</el-menu-item>
    <el-menu-item index="/front1">1小时数据</el-menu-item>
    <el-menu-item index="/front3">3小时数据</el-menu-item>
    <el-menu-item index="/front5">5小时数据</el-menu-item>
    <el-menu-item index="/endGame">比赛结束数据</el-menu-item>
  </el-menu>
</template>

<script setup>
import { ref } from "@vue/reactivity";
// 默认界面
const defaultActive = ref("/");
</script>

<style></style>
