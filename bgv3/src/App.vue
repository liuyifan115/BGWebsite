<template>
  <div class="app">
    <BasicLayout class="layout"></BasicLayout>
  </div>
</template>

<style></style>
<script setup lang="ts">
import BasicLayout from "@/layouts/BasicLayout.vue";
import {useLoginUserStore} from "@/store/useLoginUserStore";
const loginUserStore = useLoginUserStore();
loginUserStore.fetchLoginUser();
</script>
