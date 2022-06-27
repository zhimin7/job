import request from "./request";

// 查询定时爬虫数据
export const find_data = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_data",
    // 参数
    params,
  });
};

// 启动爬虫
export const startSpider = () => {
  return request({
    url: "http://175.178.14.211:9000/startspider",
  });
};

// 查询手动爬虫数据
export const find_Spider_data = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_spider_data",
    params,
  });
};

// 发送查询比赛即时数据请求
export const find_immediateData = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_immediateData",
    params,
  });
};

// 发送查询比赛前30分钟数据请求
export const find_front30 = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_front30Data",
    params,
  });
};

// 发送查询比赛前1小时数据请求
export const find_front1 = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_front1Data",
    params,
  });
};

// 发送查询比赛前3小时数据请求
export const find_front3 = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_front3Data",
    params,
  });
};

// 发送查询比赛前5小时数据请求
export const find_front5 = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_front5Data",
    params,
  });
};

// 发送查询比赛结束数据请求
export const find_end = (params) => {
  return request({
    url: "http://175.178.14.211:9000/find_endData",
    params,
  });
};
