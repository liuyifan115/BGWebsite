<template>
  <div id="basic-information">
    <a-form
      :label-col="labelCol"
      :wrapper-col="wrapperCol"
      layout="horizontal"
      style="max-width: 900px"
    >
      <a-form-item label="活动主题">
        <a-textarea :rows="1" v-model:value="basicInformation.theme" />
      </a-form-item>
      <a-form-item label="活动时间">
        <a-date-picker v-model:value="basicInformation.time" />
      </a-form-item>
      <a-form-item label="活动周期">
        <a-range-picker v-model:value="basicInformation.cycle" />
      </a-form-item>
      <a-form-item label="活动地点">
        <a-textarea :rows="1" v-model:value="basicInformation.address" />
      </a-form-item>
      <a-form-item label="调查人">
        <a-textarea :rows="1" v-model:value="basicInformation.persons" />
      </a-form-item>
      <a-form-item label="年龄">
        <a-input-number v-model:value="basicInformation.age" />
      </a-form-item>
      <a-form-item label="活动简述">
        <a-textarea :rows="3" v-model:value="basicInformation.tags" />
      </a-form-item>
    </a-form>
    <div style="margin-top: 20px; display: flex; justify-content: center">
      <a-button type="primary" @click="postAllBasic">保存</a-button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from "vue";
import { postBasicInformation } from "@/api/basicInfomation";
import { message } from "ant-design-vue";
// 表单布局配置
const labelCol = reactive({ span: 10 });
const wrapperCol = reactive({ span: 14 });
interface basicInfo {
  theme: string;
  time: string;
  cycle: string;
  address: string;
  persons: string;
  age: string;
  tags: string;
}
const basicInformation = ref<basicInfo>({
  theme: "",
  time: "",
  cycle: "",
  address: "",
  persons: "",
  age: "",
  tags: "",
});

const postAllBasic = async () => {
  const res = await postBasicInformation(basicInformation.value);
  if (res.data.code === 0) {
    message.success("保存成功");
  } else {
    message.error("保存失败");
  }
};
</script>
