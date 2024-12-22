<template>
  <div id="globalHeader">
    <a-row :wrap="false">
      <a-col flex="200px">
        <div class="title-bar">
          <img class="logo" src="../assets/资料库.png" alt="logo" />
          <div class="title">人类学家资料库</div>
        </div>
      </a-col>
      <a-col flex="auto">
        <a-menu
          v-model:selectedKeys="current"
          mode="horizontal"
          :items="items"
          @click="doMenuClick"
        />
      </a-col>
      <a-col flex="80px">
        <div class="user-login-status">
          <div v-if="loginUserStore.loginUser.username.current_user != ''">
            {{ loginUserStore.loginUser.username.current_user }}
          </div>
          <div v-else>
            <a-button type="primary" href="/user/login">登录</a-button>
          </div>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script lang="ts" setup>
import { h, ref } from "vue";
import {
  HomeOutlined,
  AppstoreOutlined,
  BookOutlined,
  SettingOutlined,
  HeatMapOutlined,
} from "@ant-design/icons-vue";
import { MenuProps } from "ant-design-vue";
import { useRouter } from "vue-router";
import { useLoginUserStore } from "@/store/useLoginUserStore";

const loginUserStore = useLoginUserStore();
const router = useRouter();

const doMenuClick = ({ key }: { key: string }) => {
  router.push({ path: key });
};

const current = ref<string[]>(["mail"]);
router.afterEach((to, from, failure) => {
  current.value = [to.path];
});

const items = ref<MenuProps["items"]>([
  {
    key: "/",
    icon: () => h(HomeOutlined),
    label: "服务中心",
    title: "服务中心",
  },
  {
    key: "/user/documentCenter",
    icon: () => h(AppstoreOutlined),
    label: "档案库",
    title: "档案库",
  },
  {
    key: "/user/post_post",
    icon: () => h(BookOutlined),
    label: "见闻记录",
    title: "见闻记录",
  },
  {
    key: "userManage",
    icon: () => h(SettingOutlined),
    label: "用户管理",
    title: "用户管理",
    children: [
      {
        key: "/user/login",
        label: "用户登录",
      },
      {
        key: "/user/register",
        label: "用户注册",
      },
    ],
  },
  {
    key: "/map_service",
    icon: () => h(HeatMapOutlined),
    label: "地图服务",
  },
]);
</script>

<style scoped>
.title-bar {
  display: flex;
  align-items: center;
}

.title {
  color: black;
  font-size: 18px;
  margin-left: 16px;
}

.logo {
  height: 32px;
}
</style>
