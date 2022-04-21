import request from "@/utils/request";

// 查询埋点列表
export function listProject(query) {
  return request({
    url: "/project/project/",
    method: "get",
    params: query
  });
}

// 查询埋点列表
export function getProject(pk) {
  return request({
    url: "/project/project/" + pk + "/",
    method: "get",
  });
}

// 新增埋点
export function addProject(query) {
  return request({
    url: "/project/project/",
    method: "post",
    params: query
  });
}

// 修改埋点
export function updateProject(query) {
  return request({
    url: "/project/project/",
    method: "put",
    params: query
  });
}

// 删除埋点
export function deleteProject(pk) {
  return request({
    url: "/project/project/" + pk + '/',
    method: "delete",
  });
}
