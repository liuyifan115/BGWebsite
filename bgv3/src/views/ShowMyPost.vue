<template>
  <div class="documentCenterPage" id="ShowMyPost">
    <div v-for="item in data" :key="item.key" class="data-item">
      <div class="data-item-row">
        <span class="data-item-title">活动名称：</span>
        <span class="data-item-content">{{ item.name }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">调查人：</span>
        <span class="data-item-content">{{ item.persons }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动时间：</span>
        <span class="data-item-content">{{ item.time }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">年龄：</span>
        <span class="data-item-content">{{ item.age }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动地点：</span>
        <span class="data-item-content">{{ item.address }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动摘要：</span>
        <span class="data-item-content">{{ item.tags }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动详情：</span>
        <span class="data-item-title">{{ item.text.title }}</span>
        <span class="data-item-content">{{ item.text.mainText }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动摘要：</span>
        <span class="data-item-content">{{ item.tags }}</span>
      </div>
      <div v-if="item.images && item.images.length > 0" class="data-item-row">
        <span class="data-item-title">活动图片：</span>
        <div class="image-gallery">
          <img
            v-for="(image, index) in item.images"
            :key="index"
            :src="image"
            alt="活动图片"
            class="image-item"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { message } from "ant-design-vue";
import { GetMyInfo } from "@/api/GetMyInfo";
import { defineProps } from "vue";

// 假设这是远端接口返回的 `data` 数据
const data = ref([]);
const fetchData = async (id) => {
  const res = await GetMyInfo(id);
  if (res.success === "1") {
    data.value = res.data.data;
  } else {
    message.error("获取数据失败");
  }
};
const props = defineProps({
  id: {
    type: String,
    required: true,
  },
});
fetchData(props.id);
</script>

<style scoped>
.documentCenterPage {
  padding: 20px;
}

.data-item {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.data-item-row {
  margin-bottom: 10px;
}

.data-item-title {
  font-weight: bold;
  margin-right: 10px;
}

.data-item-content {
  word-break: break-word;
}
</style>
