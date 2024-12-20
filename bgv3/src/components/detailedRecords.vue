<template>
  <div>
    <a-input v-model:value="value1" placeholder="输入你的标题" allow-clear />
    <br />
    <br />
    <a-textarea
      :rows="10"
      v-model:value="value2"
      placeholder="输入你的正文"
      allow-clear
    />
    <div style="margin-top: 20px; display: flex; justify-content: center">
      <a-button type="primary">保存</a-button>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
const value1 = ref<string>("");
const value2 = ref<string>("");
</script>
