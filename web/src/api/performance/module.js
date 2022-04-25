// 查询埋点列表
import request from "@/utils/request";

export function listModule(query) {
  return request({
    url: "/performance/package/module/",
    method: "get",
    params: query
  });
}

export function get_module_options() {
  return request({
    url: "/performance/module/moduleOptions/",
    method: "get",
  });
}

export function get_module_stat() {
  return request({
    url: "/performance/module/stat/",
    method: "get",
  });
}
