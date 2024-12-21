import myAxios from "@/request";

export const userRegister = async (params: any) => {
  const res = await myAxios.request({
    url: "/api/user/register",
    method: "POST",
    data: params,
  });
  return res;
};

export const userLogin = async (params: any) => {
  const res = myAxios.request({
    url: "/api/user/login",
    method: "POST",
    data: params,
  });
  return res;
};

export const searchUsers = async (username: any) => {
  const res = await myAxios.request({
    url: "/api/user/search",
    method: "GET",
    params: {
      username,
    },
  });
  return res;
};

export const getCurrentUser = async () => {
  const res = await myAxios.request({
    url: "/api/user/current",
    method: "GET",
  });
  return res;
};
