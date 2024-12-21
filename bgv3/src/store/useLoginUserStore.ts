import { defineStore } from "pinia";
import { getCurrentUser } from "@/api/user";
import { ref } from "vue";

export const useLoginUserStore = defineStore("loginUser", () => {
  const loginUser = ref<any>({
    username: "未登录",
  });

  // 远程获取用户登录信息
  async function fetchLoginUser() {
    const res = await getCurrentUser();
    if (res.data) {
      loginUser.value.username = res.data;
    }
    // else {
    //   setTimeout(() => {
    //     loginUser.value = { username: "小黑子", id: 1 };
    //   },3000);
    // }
  }

  // 单独设置信息
  function setLoginUser(newLoginUser: any) {
    loginUser.value = newLoginUser;
  }
  return { loginUser, fetchLoginUser, setLoginUser };
});
