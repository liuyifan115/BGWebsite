<template>
  <div class="clearfix">
    <a-upload
      v-model:file-list="fileList"
      action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
      list-type="picture-card"
      @preview="handlePreview"
    >
      <div v-if="fileList.length < 8">
        <plus-outlined />
        <div style="margin-top: 8px">Upload</div>
      </div>
    </a-upload>
    <a-modal
      :open="previewVisible"
      :title="previewTitle"
      :footer="null"
      @cancel="handleCancel"
    >
      <img alt="example" style="width: 100%" :src="previewImage" />
    </a-modal>
  </div>
  <div class="button-class" >
    <div style="margin-top: 20px; display: flex; justify-content: center">
      <a-button type="primary">保存</a-button>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { PlusOutlined } from "@ant-design/icons-vue";
import { ref } from "vue";
import type { UploadProps } from "ant-design-vue";

function getBase64(file: File) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });
}

const previewVisible = ref(false);
const previewImage = ref("");
const previewTitle = ref("");

const fileList = ref<UploadProps["fileList"]>([
  {
    uid: "-1",
    name: "image.png",
    status: "done",
    url: "https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png",
  },
]);

const handleCancel = () => {
  previewVisible.value = false;
  previewTitle.value = "";
};
const handlePreview = async (file: UploadProps["fileList"][number]) => {
  if (!file.url && !file.preview) {
    file.preview = (await getBase64(file.originFileObj)) as string;
  }
  previewImage.value = file.url || file.preview;
  previewVisible.value = true;
  previewTitle.value =
    file.name || file.url.substring(file.url.lastIndexOf("/") + 1);
};
</script>
<style scoped>
/* you can make up upload button and sample style by using stylesheets */
.ant-upload-select-picture-card i {
  font-size: 32px;
  color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
.button-class {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: center; /* 水平居中排列子元素 */
  gap: 20px; /* 子元素之间的间距（可选） */
  position: absolute; /* 或者使用 position: relative; 取决于父容器的定位 */
  bottom: 50px; /* 距离底部固定 30px */
  left: 60%; /* 水平定位到父容器的 50% */
}
</style>
