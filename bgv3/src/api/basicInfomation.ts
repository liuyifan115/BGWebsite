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
    method: "get",
  });
  return res;
};