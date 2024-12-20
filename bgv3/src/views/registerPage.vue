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

function submitForm(action: string): void {
  if (
    action === "register" &&
    credentials.value.password !== confirmPassword.value
  ) {
    alert("密码和确认密码不匹配");
    return;
  }
  console.log({
    action,
    username: credentials.value.username,
    password: credentials.value.password,
  });
  // 实际应用中这里会有 AJAX 请求
  alert(`提交了${action}表单`);
}
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
