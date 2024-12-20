<template>
  <div class="embedded-container">
    <iframe
      :src="url"
      width="100%"
      height="600px"
      title="Embedded Webpage"
    >
    </iframe>
  </div>
</template>

<script>
export default {
  data() {
    return {
      url: "https://map.baidu.com/", // 网页URL
    };
  },
};
</script>

<style scoped>
.embedded-container {
  text-align: center;
  padding: 20px;
}
iframe {
  border: none;
}
</style>
