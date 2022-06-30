import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  // 首页
  {
    path: "/",
    name: "/",
    component: () => import("../views/IndexView.vue"),
    children: [
      // 定时启动爬虫界面
      {
        path: "/",
        name: "/",
        component: () =>
          import("@/components/DataView/Content/TimingSpiderDataView.vue"),
      },
      // 手动启动爬虫界面
      {
        path: "/manualspider",
        name: "manualspider",
        component: () =>
          import("@/components/DataView/Content/ManualSpiderDataView.vue"),
      },
      // 即时比赛数据展示界面
      {
        path: "/immediate",
        name: "immediate",
        component: () =>
          import("@/components/DataView/Content/ImmediateDataView.vue"),
      },
      // 比赛前30分钟数据展示界面
      {
        path: "/front30",
        name: "front30",
        component: () =>
          import("@/components/DataView/Content/Front30DataView.vue"),
      },
      // 比赛前1小时数据展示界面
      {
        path: "/front1",
        name: "front1",
        component: () =>
          import("@/components/DataView/Content/Front1DataView.vue"),
      },
      // 比赛前3小时数据展示界面
      {
        path: "/front3",
        name: "front3",
        component: () =>
          import("@/components/DataView/Content/Front3DataView.vue"),
      },
      // 比赛前5小时数据展示界面
      {
        path: "/front5",
        name: "front5",
        component: () =>
          import("@/components/DataView/Content/Front5DataView.vue"),
      },
      // 比赛结束数据展示界面
      {
        path: "/endGame",
        name: "endGame",
        component: () =>
          import("@/components/DataView/Content/EndDataView.vue"),
      },
    ],
  },

  // 登录页
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
