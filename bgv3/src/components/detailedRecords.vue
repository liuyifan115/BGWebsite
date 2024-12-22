<template>
  <div>
    <a-input
      placeholder="输入你的标题"
      allow-clear
      v-model:value="Text_.title"
    />
    <br />
    <br />
    <a-textarea
      :rows="10"
      v-model:value="Text_.mainText"
      placeholder="输入你的正文"
      allow-clear
    />
    <div style="margin-top: 20px; display: flex; justify-content: center">
      <a-button type="primary" @click="postText">保存</a-button>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { postDetails } from "@/api/basicInfomation";
import { message } from "ant-design-vue";
const Text_ = ref<text_>({
  title: "",
  mainText: "",
});
interface text_ {
  title: string;
  mainText: string;
}
const postText = async () => {
  const res = await postDetails(Text_.value);
  if (res.data.success === "1") {
    message.success("保存成功");
  } else {
    message.error("保存失败");
  }
};
</script>
