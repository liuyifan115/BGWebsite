import axios from "axios";

const myAxios = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  // headers: { "X-Custom-Header": "foobar" },
});

export default myAxios;

// 添加响应拦截器
axios.interceptors.response.use(
  function (response){
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    console.log(response);

    const { data } = response;
    console.log(data);
    // 未登录
    // if (data.code === 0) {}
    return response;
  },
  function (error) {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    return Promise.reject(error);
  }
);
