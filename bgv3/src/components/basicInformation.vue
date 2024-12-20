<template>
  <div id="basic-information">
    <a-form
      :label-col="labelCol"
      :wrapper-col="wrapperCol"
      layout="horizontal"
      style="max-width: 900px"
    >
      <a-form-item label="活动主题">
        <a-textarea :rows="1" />
      </a-form-item>
      <a-form-item label="活动时间">
        <a-date-picker />
      </a-form-item>
      <a-form-item label="活动周期">
        <a-range-picker />
      </a-form-item>
      <a-form-item label="活动地点">
        <a-textarea :rows="1" />
      </a-form-item>
      <a-form-item label="调查人">
        <a-textarea :rows="1" />
      </a-form-item>
      <a-form-item label="活动简述">
        <a-textarea :rows="3" />
      </a-form-item>
    </a-form>
    <div style="margin-top: 20px; display: flex; justify-content: center">
      <a-button type="primary">保存</a-button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive } from "vue";
// 表单布局配置
const labelCol = reactive({ span: 10 });
const wrapperCol = reactive({ span: 14 });
</script>
