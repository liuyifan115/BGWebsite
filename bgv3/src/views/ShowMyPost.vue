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
        <span class="data-item-title">活动地点：</span>
        <span class="data-item-content">{{ item.address }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动摘要：</span>
        <span class="data-item-content">{{ item.tags }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动详情：</span>
        <span class="data-item-title">{{ item.detail_title }}</span>
        <span class="data-item-content">{{ item.detail_text }}</span>
      </div>
      <div class="data-item-row">
        <span class="data-item-title">活动摘要：</span>
        <span class="data-item-content">{{ item.tags }}</span>
      </div>
      <div v-if="item.photo" class="data-item-row">
        <span class="data-item-title">活动图片：</span>
        <div class="image-gallery">
          <img
            v-for="image in imagesArray"
            :src="'http://127.0.0.1:8000/api/user/GetImage?path=' + image"
            alt="活动图片"
            class="image-item"
            :width="400"
            :height="400"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch } from "vue";
import { message } from "ant-design-vue";
import { defineProps } from "vue";
import { GetImage, GetMyInfo } from "@/api/GetMyInfo";

// const GetImage_ = async ({ path }: { path: string }) => {
//   const reg = await GetImage(path);
//   return reg;
// }

// 假设这是远端接口返回的 `data` 数据
const data = ref([]);
var imagesArray = [];
const pgoto_blob = ref([]);

onMounted(async () => {
  await Promise.all(
    imagesArray.map(async (image) => {
      const url = await fetchPhoto(image);
      imageUrls.value.push(url);
    })
  );
});

// const fetchData = async () => {
//   const res = await getBasicInformation();
//   if (res.data.success === "1") {
//     data.value = res.data.data;
//   } else {
//     message.error("获取数据失败");
//   }
// };

const fetchPhoto = async (id) => {
  await Promise.all();
  const imageData = await GetImage({ path: id });
  console.log(imageData.data);
  var photo_blob = new Blob([imageData.data], { type: "image/png" });
  const url = URL.createObjectURL(photo_blob);
  console.log(url);
  return url;
};

const fetchData = async (props) => {
  const res = await GetMyInfo({ id: props.id });
  if (res.data.success === "1") {
    data.value = res.data.data;
    imagesArray = JSON.parse(
      JSON.parse(JSON.stringify(data.value))[0]["photo"].replace(/'/g, '"')
    );
  } else {
    message.error("获取数据失败");
  }
};
const trans = async () => {
  imagesArray.value = ref(JSON.parse(data.value.photo.replace(/'/g, '"')));
};

const props = defineProps({
  id: {
    type: String,
    required: true,
  },
});
fetchData(props);
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
