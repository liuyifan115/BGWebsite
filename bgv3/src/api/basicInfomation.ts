import myAxios from "@/request";

export const postBasicInformation = async (params: any) => {
  const res = await myAxios.request({
    url: "/api/postBasicInfo",
    method: "POST",
    data: params,
  });
  return res;
};

export const getBasicInformation = async () => {
  const res = await myAxios.request({
    url: "/api/getBasicInfo",
    method: "GET",
  });
  return res;
};

export const postDetails = async (params: any) => {
  const res = await myAxios.request({
    url: "/api/postDetails",
    method: "POST",
    data: params,
  });
  return res;
};

export const postOver = async () => {
  const params = { over: 1 };
  const res = await myAxios.request({
    url: "/api/postOver",
    method: "POST",
    data: params,
  });
  return res;
};

export const postFile = async (params: any) => {
  const res = await myAxios.request({
    url: "/api/postPng",
    method: "POST",
    data: params,
  });
  return res;
};
