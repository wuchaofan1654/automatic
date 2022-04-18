import request from "@/utils/request";

// 查询模块列表
export function listModule(query) {
  return request({
    url: "/permission/module/",
    method: "get",
    params: query
  });
}

// 查询模块列表（排除节点）
export function listModuleExcludeChild(moduleId) {
  return request({
    url: "/permission/module/exclude/" + moduleId + "/",
    method: "get"
  });
}

// 查询模块详细
export function getModule(moduleId) {
  return request({
    url: "/permission/module/" + moduleId + "/",
    method: "get"
  });
}

// 查询模块下拉树结构
export function treeselect() {
  return request({
    url: "/permission/module/treeselect/?status=1",
    method: "get"
  });
}

// 新增模块
export function addModule(data) {
  return request({
    url: "/permission/module/",
    method: "post",
    data: data
  });
}

// 修改模块
export function updateModule(data) {
  return request({
    url: "/permission/module/" + data.id + "/",
    method: "put",
    data: data
  });
}

// 删除模块
export function delModule(ModuleId) {
  return request({
    url: "/permission/module/" + ModuleId + "",
    method: "delete"
  });
}
