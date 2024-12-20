<script setup lang="ts">
import GlobalHeader from "@/components/GlobalHeader.vue";
</script>

<template>
  <div id="basic-layout">
    <a-layout>
      <a-layout-header class="header">
        <GlobalHeader />
      </a-layout-header>
      <a-layout-content class="content">
        <router-view />
      </a-layout-content>
      <a-layout-footer class="footer">
        <a href="https://bilibili.com/" target="_blank"> More About Us! </a>
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<style scoped>
#basic-layout .footer {
  background: rgba(198, 197, 198, 0.44);
  text-align: center;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 16px;
}

#basic-layout .content {
  //display: flex;
  margin-left: 100px;
  margin-right: 100px;
  height: 700px;
  margin-top: 10px;
  justify-content: center; /* 水平居中 */
  //align-items: center;
  //padding: 20px;
  margin-bottom: 20px;
  //background: linear-gradient(to right bottom, rgba(78, 68, 68, 0.14), #f6f4f4);
  background: rgba(255, 255, 255, 0.79);
}

#basic-layout .header {
  background: white;
  margin-bottom: 10px;
  padding-inline: 20px;
}
</style>
