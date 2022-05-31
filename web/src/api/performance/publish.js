import request from "@/utils/request";

// 查询埋点列表
export function comparePublish(pk1, pk2) {
  return request({
    url: "/performance/package/publish/compare/" + pk1 + "/" + pk2 + "/",
    method: "get",
  });
}

// 查询埋点列表
export function listPublish(query) {
  return request({
    url: "/performance/package/publish/",
    method: "get",
    params: query
  });
}


// 查询版本列表
export function listBuildNo(query) {
  return request({
    url: "/performance/publish/options/build",
    method: "get",
    params: query
  });
}

// 通过json文件添加发布记录数据
export function addPublish(data) {
  return request({
    url: "/performance/publish/",
    method: "post",
    data: data
  });
}
