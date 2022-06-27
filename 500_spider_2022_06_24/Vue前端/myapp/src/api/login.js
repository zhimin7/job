import request from "./request";

export const login = (params) => {
  return request({
    url: "http://175.178.14.211:9000/login",
    params,
  });
};
