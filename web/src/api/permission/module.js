import request from "@/utils/request";

// 查询部门列表
export function listModule(query) {
  return request({
    url: "/permission/module/",
    method: "get",
    params: query
  });
}
