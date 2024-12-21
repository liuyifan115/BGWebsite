<template>
  <div id="postLayout">
    <a-layout>
      <a-layout>
        <a-layout-sider width="200" style="background: #fff; height: 650px">
          <a-menu
            v-model:selectedKeys="selectedKeys2"
            v-model:openKeys="openKeys"
            mode="inline"
            :style="{ height: '100%', borderRight: 0 }"
          >
            <a-menu-item key="1"> 活动概览 </a-menu-item>
            <a-menu-item key="2"> 活动记录 </a-menu-item>
            <a-menu-item key="3"> 影像资料 </a-menu-item>
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
            <a-layout>
              <show-my-post />
            </a-layout>
          </a-layout-content>
        </a-layout>
      </a-layout>
    </a-layout>
  </div>
</template>

<script lang="ts" setup>
import ShowMyPost from "@/views/ShowMyPost.vue";
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
