import request from "./request";

export const login = (params) => {
  return request({
    url: "http://123.207.28.67:9000/login",
    params,
  });
};
