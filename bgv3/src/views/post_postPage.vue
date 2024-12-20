<template>
  <a-layout>
    <a-layout>
      <a-layout-sider width="200" style="background: #fff; height: 650px">
        <a-menu
          v-model:selectedKeys="selectedKeys2"
          v-model:openKeys="openKeys"
          mode="inline"
          :style="{ height: '100%', borderRight: 0 }"
        >
          <a-sub-menu key="sub1" @click="loadComponent('basicInformation')">
            <template #title>
              <span>
                <message-outlined />
                基本信息
              </span>
            </template>
            <a-menu-item key="1">活动主题</a-menu-item>
            <a-menu-item key="2">活动时间</a-menu-item>
            <a-menu-item key="3">活动地点</a-menu-item>
            <a-menu-item key="4">调查人</a-menu-item>
            <a-menu-item key="5">活动概要</a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="sub2">
            <template #title>
              <span>
                <notification-outlined />
                详细记录
              </span>
            </template>
            <a-menu-item key="6" @click="loadComponent('detailedRecords')"
              >活动详情</a-menu-item
            >
          </a-sub-menu>
          <a-sub-menu key="sub3">
            <template #title>
              <span>
                <play-square-outlined />
                影像资料
              </span>
            </template>
            <a-menu-item key="10" @click="loadComponent('docuPic')"
              >图片</a-menu-item
            >
            <a-menu-item key="9" @click="loadComponent('docuVideo')"
              >视频</a-menu-item
            >
          </a-sub-menu>
        </a-menu>
      </a-layout-sider>
      <a-layout style="padding: 0 24px 24px">
        <a-layout-content
          :style="{
            background: '#fff',
            padding: '24px',
            margin: 0,
            minHeight: '280px',
          }"
        >
          <!-- 动态渲染组件 -->
          <!-- <component :is="detailedRecords" />-->
          <component :is="currentComponent" />
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>

<script lang="ts" setup>
import { ref, defineAsyncComponent } from "vue";
import nothing from "@/components/nothing.vue";
import {
  PlaySquareOutlined,
  NotificationOutlined,
  MessageOutlined,
} from "@ant-design/icons-vue";
// 按需导入组件（懒加载）
// 定义当前显示的组件（默认显示 basicInformation）
const currentComponent = ref<unknown>(nothing);

const basicInformation = defineAsyncComponent(
  () => import("@/components/basicInformation.vue")
);
const detailedRecords = defineAsyncComponent(
  () => import("@/components/detailedRecords.vue")
);
const docuPic = defineAsyncComponent(() => import("@/components/docuPic.vue"));
const docuVideo = defineAsyncComponent(
  () => import("@/components/docuVideo.vue")
);
// const nothing = defineAsyncComponent(() => import("@/components/nothing.vue"));

// 定义菜单选中状态
const selectedKeys2 = ref<string[]>(["1"]);
const openKeys = ref<string[]>(["sub1"]);

// 切换组件的方法
function loadComponent(componentName: string) {
  if (componentName === "basicInformation") {
    currentComponent.value = basicInformation;
  } else if (componentName === "detailedRecords") {
    currentComponent.value = detailedRecords;
  } else if (componentName === "docuPic") {
    currentComponent.value = docuPic;
  } else if (componentName === "docuVideo") {
    currentComponent.value = docuVideo;
  }
}
</script>

<style scoped>
#components-layout-demo-top-side-2 .logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
}

.ant-row-rtl #components-layout-demo-top-side-2 .logo {
  float: right;
  margin: 16px 0 16px 24px;
}
</style>
