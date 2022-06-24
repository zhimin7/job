<template>
  <div>
    <el-card>
      <div>
        <label>历史数据展示：</label>
        <el-date-picker
          v-model="queryForm.value1"
          type="daterange"
          range-separator="To"
          start-placeholder="开始时间"
          end-placeholder="结束时间"
          unlink-panels
        />
        <el-button
          type="primary"
          :icon="Search"
          @click="initgetGamesDataList"
          class="date-picker"
          >查询</el-button
        >
        <el-button
          type="primary"
          :icon="Download"
          class="date-picker"
          @click="deriveExcel"
          >下载数据</el-button
        >

        <el-dropdown class="logout">
          <span class="el-dropdown-link">
            <el-avatar shape="square" :size="40" :src="squareUrl" />
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
      <el-table :data="tableData" height="430px" style="width: 100%" id="table">
        <el-table-column
          :width="item.width"
          :prop="item.prop"
          :label="item.label"
          v-for="(item, index) in options"
          :key="index"
          sortable
        >
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { options } from "../js/options";
import { ref, reactive } from "vue";
import { Search, Download } from "@element-plus/icons-vue";
import XLSX from "xlsx";
import ExportJsonExcel from "js-export-excel";
import { useStore } from "vuex";
import { find_data } from "@/api/getdata.js";

const store = useStore();
// 初始化表格数据
const tableData = ref([]);
const squareUrl = ref(
  "https://img0.baidu.com/it/u=1056811702,4111096278&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"
);
// 下载数据的文件名
const state = reactive({
  date: "",
  time: "",
  week: "",
  showIndex: 0,
});
const myDate = new Date();
let month = (myDate.getMonth() + 1).toString().padStart(2, "0");
let day = myDate.getDate().toString().padStart(2, "0");
let hour = myDate.getHours().toString().padStart(2, "0");
let minutes = myDate.getMinutes().toString().padStart(2, "0");
let seconed = myDate.getSeconds().toString().padStart(2, "0");
state.date = myDate.getFullYear() + "-" + month + "-" + day;
state.time = hour + "时" + minutes;

const deriveExcel = async () => {
  const res = await find_data(queryForm.value);
  const dataList = res.data;
  let option = {};
  let dataTable = [];
  if (dataList) {
    for (let i in dataList) {
      let obj = {
        gamestime: dataList[i].time,
        home_team: dataList[i].home_team,
        score: dataList[i].score,
        away_team: dataList[i].away_team,
        handicap: dataList[i].handicap,
        All_companies: dataList[i].All_companies,
        mainstream_companines_3: dataList[i].mainstream_companines_3,
        mainstream_companines_1: dataList[i].mainstream_companines_1,
        Exchange: dataList[i].Exchange,
        BiFa: dataList[i].BiFa,
        Matchbook: dataList[i].Matchbook,
        Leon: dataList[i].Leon,
        Betsson: dataList[i].Betsson,
      };
      dataTable.push(obj);
    }
  }
  const filename =
    "500彩票-比赛历史数据-" + state.date + " " + state.time + "分.xlsx";
  option.fileName = filename;
  option.datas = [
    {
      sheetData: dataTable,
      sheetName: "sheet",
      sheetHeader: [
        "gamestime",
        "home_team",
        "score",
        "away_team",
        "handicap",
        "All_companies",
        "mainstream_companines_3",
        "mainstream_companines_1",
        "Exchange",
        "BiFa",
        "Matchbook",
        "Leon",
        "Betsson",
      ],
      sheetFilter: [
        "gamestime",
        "home_team",
        "score",
        "away_team",
        "handicap",
        "All_companies",
        "mainstream_companines_3",
        "mainstream_companines_1",
        "Exchange",
        "BiFa",
        "Matchbook",
        "Leon",
        "Betsson",
      ],
    },
  ];
  let toExcel = new ExportJsonExcel(option);
  toExcel.saveExcel();
};

// 发送查询请求或下载请求的参数
const queryForm = ref({
  query: "",
  pagenum: 1,
  pagesize: 2,
  value1: "",
});

// 查询数据
const initgetGamesDataList = async () => {
  const res = await find_data(queryForm.value);
  tableData.value = res.data;
};
initgetGamesDataList();
// 设置定时查询数据
// setInterval(initgetGamesDataList, 5000);

// 退出登录
const logout = () => {
  store.dispatch("app/logout");
};
</script>

<style lang="scss">
.date-picker {
  margin-bottom: 10px;
  margin-left: 20px;
}
.logout {
  margin-left: 500px;
}
</style>
