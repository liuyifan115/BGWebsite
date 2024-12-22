import myAxios from "@/request";

export const GetMyInfo = async (id: any) => {
  const res = await myAxios.request({
    url: "/api/user/getMyInfo",
    method: "GET",
    params: id,
  });
  return res;
};

export const GetImage = async (id: any) => {
  const res = await myAxios.request({
    url: "/api/user/GetImage",
    method: "GET",
    params: id,
  });
  return res;
};
