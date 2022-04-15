import request from "@/utils/request";

// 查询埋点列表
export function listPoint(query) {
  return request({
    url: "/point/point/",
    method: "get",
    params: query
  });
}

// 查询埋点列表
export function getPoint(pk) {
  return request({
    url: "/point/point/" + pk + "/",
    method: "get",
  });
}

// 新增埋点
export function addPoint(query) {
  return request({
    url: "/point/point/",
    method: "post",
    params: query
  });
}

// 修改埋点
export function updatePoint(query) {
  return request({
    url: "/point/point/",
    method: "put",
    params: query
  });
}

// 删除埋点
export function deletePoint(pk) {
  return request({
    url: "/point/point/" + pk + '/',
    method: "delete",
  });
}

// 查询埋点集合列表
export function listPointSuite(query) {
  return request({
    url: "/point/suite/",
    method: "get",
    params: query
  });
}
