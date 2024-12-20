<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
const backgroundColor = ref("yellow");
const doMenuClick = ({ key }: { key: string }) => {
  router.push({ path: key });
};
const router = useRouter();
const onMouseOver = () => {
  backgroundColor.value = "green";
};

const onMouseLeave = () => {
  backgroundColor.value = "yellow";
};
</script>

<template>
  <div id="home-page">
    <a-row>
      <a-col :span="8">
        <div class="leftPart">
          <a-layout>
            <a-layout-content class="middleContent">
              <img
                class="main_png"
                src="../assets/survey.png"
                alt="home.page"
              />
            </a-layout-content>
            <a-layout-content class="content inContent">
              <h2 class="indent" style="color: green">
                欢迎来到人类学家资料库！这份资料库可以有效帮助您组织、存储和检索日常调查中收集的丰富数据。在探索自然景观、村落和文化遗迹的过程中，
                有效帮助记录大量的信息和文化遗产，并高效地管理各种格式的数据资源。
              </h2>
            </a-layout-content>
            <a-layout-footer
              class="footer"
              :style="{ background: backgroundColor, cursor: 'pointer' }"
              @mouseover="onMouseOver"
              @mouseleave="onMouseLeave"
              @click="doMenuClick({ key: '/user/post_post' })"
            >
              <h1>*开始你的创作吧！*</h1>
            </a-layout-footer>
          </a-layout>
        </div>
      </a-col>
      <a-col :span="16">
        <div class="rightPart">
          <a-layout>
            <a-layout-header class="header">推荐内容</a-layout-header>
            <a-layout-content class="rContent">
              <div>
                <a-row :wrap="false">
                  <a-col flex="100px">
                    <img class="logo" src="../assets/西藏.png" alt="logo" />
                  </a-col>
                  <a-col
                    flex="auto"
                    class="indent"
                    @click="doMenuClick({ key: '/_posts/posts' })"
                  >
                    西藏游记：我去了离天最近的地方三（拉萨）
                  </a-col>
                </a-row>
              </div>
            </a-layout-content>
            <!--            <a-layout-content class="rContent">-->
            <!--              <div>-->
            <!--                <a-row :wrap="false">-->
            <!--                  <a-col flex="100px">-->
            <!--                    <img class="logo" src="../assets/logo.png" alt="logo" />-->
            <!--                  </a-col>-->
            <!--                  <a-col flex="auto" class="indent">-->
            <!--                    欢迎来到人类学家资料库！这份资料库可以有效帮助您-->
            <!--                    组织、存储和检索日常调查中收集的丰富数据。在探索自然景观、村落和文化遗迹的过程中，-->
            <!--                    有效帮助记录大量的信息和文化遗产，并高效地管理各种格式的数据资源，包括图像（如-->
            <!--                    JPG 或 PNG 文件）、音频访谈（如 MP3 或 MP4-->
            <!--                    文件）、以及数字化的文献。-->
            <!--                  </a-col>-->
            <!--                </a-row>-->
            <!--              </div>-->
            <!--            </a-layout-content>-->
            <!--            <a-layout-content class="rContent">-->
            <!--              <div>-->
            <!--                <a-row :wrap="false">-->
            <!--                  <a-col flex="100px">-->
            <!--                    <img class="logo" src="../assets/logo.png" alt="logo" />-->
            <!--                  </a-col>-->
            <!--                  <a-col flex="auto" class="indent">-->
            <!--                    欢迎来到人类学家资料库！这份资料库可以有效帮助您-->
            <!--                    组织、存储和检索日常调查中收集的丰富数据。在探索自然景观、村落和文化遗迹的过程中，-->
            <!--                    有效帮助记录大量的信息和文化遗产，并高效地管理各种格式的数据资源，包括图像（如-->
            <!--                    JPG 或 PNG 文件）、音频访谈（如 MP3 或 MP4-->
            <!--                    文件）、以及数字化的文献。-->
            <!--                  </a-col>-->
            <!--                </a-row>-->
            <!--              </div>-->
            <!--            </a-layout-content>-->
          </a-layout>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<style scoped>
.rContent {
  display: flex;
  padding: 20px;
  border: 1px solid black;
  border-radius: 10px;
  margin: 5px;
}

.middleContent {
  background: #78d318;
  padding: 10px;
  display: flex;
  justify-content: center; /* 水平居中 */
  height: 100%; /* 如果需要全高度居中，确保父容器有高度 */
  border-radius: 10px;
  margin: 5px;
}
.inContent {
  background: #8af31d;
}

.main_png {
  max-width: 100%; /* 限制图片宽度避免超出容器 */
  height: auto; /* 保持图片比例 */
}

.leftPart {
  display: flex;
  background: #78d318;
  border-radius: 10px;
}
.rightPart {
  margin-left: 30px;
  padding-left: 20px;
  border-radius: 10px;
}
.header {
  background: #8e9aaf;
  margin-top: 5px;
  border-radius: 10px;
}
.content {
  display: flex;
  height: 100%;
  padding: 20px;
  background: linear-gradient(
    to right bottom,
    rgba(131, 243, 54, 0.14),
    #f6f647
  );
  border-radius: 10px;
  margin: 5px;
}

.footer {
  border-radius: 10px;
}

.indent {
  text-indent: 2em; /* 缩进两个字符 */
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;
  font: 14px "Microsoft Yahei", sans-serif;
}
.logo {
  height: 100px;
}
</style>
