// 查询埋点列表
import request from "@/utils/request";

export function listModule(query) {
  return request({
    url: "/package/module/",
    method: "get",
    params: query
  });
}

export function get_module_options() {
  return request({
    url: "/package/module/moduleOptions/",
    method: "get",
  });
}
