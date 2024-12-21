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

// export const postFile = async (params: any) => {
//   const res = await myAxios.request({
//     url: "/api/postFile",
//     method: "POST",
//     data: params,
//   });
//   return res;
// };

export const postFile = async (params: any) => {
  const formData = new FormData();

  // 假设 params 中有一个 'files' 字段，它是一个文件数组
  if (params) {
    params.forEach((file: File, index: number) => {
      formData.append(`file_${index}`, file); // 将文件添加到 FormData 对象中，file_0, file_1, ...
    });
  }

  // 使用 myAxios 发送 POST 请求
  const res = await myAxios.request({
    url: "/api/postFile", // 文件上传接口
    method: "POST", // 使用 POST 方法
    data: formData, // 请求体是 FormData
    // headers: {
    //   "Content-Type": "multipart/form-data", // 设置请求头，指定上传文件
    // },
  });

  return res; // 返回响应数据
};
