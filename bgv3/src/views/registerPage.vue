<template>
  <div class="registerPage">
    <div class="container">
      <div class="background-div"></div>
      <div class="form-box" :style="{ transform: formBoxTransform }">
        <div v-show="isLogin" class="login-box">
          <h1>login</h1>
          <form @submit.prevent="submitForm('login')">
            <input
              v-model="credentials.username"
              type="text"
              placeholder="用户名"
              required
            />
            <input
              v-model="credentials.password"
              type="password"
              placeholder="密码"
              required
            />
            <button type="submit">登录</button>
          </form>
        </div>
        <div v-show="!isLogin" class="register-box">
          <h1>register</h1>
          <form @submit.prevent="submitForm('register')">
            <input
              v-model="credentials.username"
              type="text"
              placeholder="用户名"
              required
            />
            <input
              v-model="credentials.password"
              type="password"
              placeholder="密码"
              required
            />
            <input
              v-model="confirmPassword"
              type="password"
              placeholder="确认密码"
              required
            />
            <button type="submit">注册</button>
          </form>
        </div>
      </div>
      <div class="con-box left" @click="toggleForm(true)">
        <h2>欢迎来到<br /><span>人类学家资料库</span></h2>
        <p>已有账号</p>
        <button>去登录</button>
      </div>
      <div class="con-box right" @click="toggleForm(false)">
        <h2>欢迎来到<br /><span>人类学家资料库</span></h2>
        <p>没有账号？</p>
        <button>去注册</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from "vue";
import { userLogin, userRegister } from "@/api/user";
import { useLoginUserStore } from "@/store/useLoginUserStore";
import { message } from "ant-design-vue";
import { useRouter } from "vue-router";

interface Credentials {
  username: string;
  password: string;
}

const isLogin = ref(false);
const credentials = ref<Credentials>({ username: "", password: "" });
const confirmPassword = ref("");
const formBoxTransform = computed(() =>
  isLogin.value ? "translateX(0%)" : "translateX(95%)"
);

function toggleForm(showLogin: boolean): void {
  isLogin.value = showLogin;
  credentials.value = { username: "", password: "" };
  confirmPassword.value = "";
}

const loginUserStore = useLoginUserStore();
const router = useRouter();
// 提交表单
const submitForm = async (action: string) => {
  if (action === "login") {
    const res = await userLogin(credentials.value);
    //登陆成功
    if (res.data.success === "1") {
      await loginUserStore.fetchLoginUser();
      message.success("登陆成功");
      router.push({
        path: "/",
        replace: true,
      });
    } else {
      message.error("登陆失败");
    }
    console.log("success:", credentials.value);
  } else if (action === "register") {
    const res = await userRegister(credentials.value);
    //注册成功
    if (res.data.success === "1") {
      message.success("注册成功");
      router.push({
        path: "/user/login",
        replace: true,
      });
    } else {
      message.error("注册失败");
    }
  }
};
</script>

<style scoped>
@import "../assets/css/login.css";

.background-div {
  width: 100vw; /* 视口宽度100% */
  height: 100vh; /* 视口高度100% */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  //background-image: url("");
  background-size: cover; /* 覆盖整个元素区域 */
  background-position: center; /* 图片居中显示 */
  background-repeat: no-repeat; /* 不重复显示背景图片 */
  z-index: 0;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.form-box {
  display: flex;
  justify-content: space-between;
  width: 300px;
  transition: transform 0.3s;
}

.con-box {
  cursor: pointer;
  text-align: center;
}
</style>
