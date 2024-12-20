<template>
  <div id="posts">
    <a-layout>
      <a-layout>
        <a-layout-sider width="200" style="background: #fff; height: 650px">
          <a-menu
            v-model:selectedKeys="selectedKeys2"
            v-model:openKeys="openKeys"
            mode="inline"
            :style="{ height: '100%', borderRight: 0 }"
          >
            <a-menu-item key="1"> 活动概览 </a-menu-item>
            <a-menu-item key="2"> 活动记录 </a-menu-item>
            <a-menu-item key="3"> 影像资料 </a-menu-item>
          </a-menu>
        </a-layout-sider>
        <a-layout style="padding: 0 24px 24px">
          <a-layout-content
            :style="{
              background: '#fff',
              padding: '24px',
              margin: 0,
              minHeight: '280px',
            }"
          >
            <a-layout>
              <a-layout-content>
                <div class="detail_box">
                  <div class="maintitle">
                    西藏游记：我去了离天最近的地方三（拉萨）
                  </div>
                  <div class="detail_source">
                    来源：星辰文旅 |
                    <span style="display: inline-block" class="author_span"
                      >编辑:李觅之</span
                    ><!--作者：李觅之-->
                    | 2017-09-18
                  </div>
                  <div class="article_content">
                    <div id="tempNewsContentDiv">
                      <p style="text-align: center">到了拉萨市</p>
                      <h3 style="text-align: center">
                        <p style="text-align: center">
                          <img
                            src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf32e52b383.jpg"
                            class="slideImg"
                          />
                        </p>
                        <p style="text-align: center"></p>
                        <p></p>
                        <p style="text-align: center"></p>
                        <p>
                          随处可见做礼拜的人们<br />那份执着和信仰<br />足以让任何经过的路人心生敬畏
                        </p>
                        <img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf33876e9f9.jpg"
                          class="slideImg"
                        />
                        <p></p>
                        <p></p>
                        <p></p>
                      </h3>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>藏式宗教的千古典范</span>
                      </p>
                      <p style="text-align: center">
                        <span>庄严的大昭寺</span>
                      </p>
                      <p style="text-align: center">
                        <span>没有经过历史上的任何破坏</span>
                      </p>
                      <p style="text-align: center"><span>保存完整</span></p>
                      <p>
                        <img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf339c48dac.jpg"
                          class="slideImg"
                          style="
                            display: block;
                            margin-left: auto;
                            margin-right: auto;
                          "
                        />
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf33b0c4705.jpg"
                          class="slideImg"
                        />
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>这是八廓街的经幡柱</span>
                      </p>
                      <p style="text-align: center">
                        <span>藏历新年到来之时</span>
                      </p>
                      <p style="text-align: center">
                        <span>众多教徒将把写有祈愿的经幡系在经杆上</span>
                      </p>
                      <p style="text-align: center">
                        <span
                          ><img
                            src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf33d0b9d3a.jpg"
                            class="slideImg"
                        /></span>
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center"><span>主角登场</span></p>
                      <p style="text-align: center">
                        <span>布达拉宫<br /></span>
                      </p>
                      <p style="text-align: center">
                        <span>布达拉又译作“普陀罗”意指观世音菩萨所居之岛</span>
                      </p>
                      <p style="text-align: center">
                        <span>俗称第二普陀山</span>
                      </p>
                      <p style="text-align: center">
                        <span
                          ><img
                            src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf33e7729ec.jpg"
                            class="slideImg"
                        /></span>
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>布达拉宫广场上<br /></span>
                      </p>
                      <p style="text-align: center">
                        <span>拍照的绝佳场所</span>
                      </p>
                      <p style="text-align: center">
                        <span
                          ><img
                            src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf33fbbd1f8.jpg"
                            class="slideImg"
                        /></span>
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>进宫坡道迂回曲折</span>
                      </p>
                      <p style="text-align: center">
                        <span>此道又名圆满汇集道</span>
                      </p>
                      <p style="text-align: center">
                        <span>爬完了这九百多级的阶梯</span>
                      </p>
                      <p style="text-align: center">
                        <span>所有的圆满也就汇聚在你身上了</span>
                      </p>
                      <p style="text-align: center">
                        <span></span
                        ><img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf340e72cfe.jpg"
                          class="slideImg"
                        />
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>在布达拉宫上面往下遥望</span>
                      </p>
                      <p style="text-align: center">
                        <span></span
                        ><img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf34268aab0.jpg"
                          class="slideImg"
                        />
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>前方是布达拉宫广场</span>
                      </p>
                      <p style="text-align: center">
                        <span>号称是全世界海拔最高的广场</span>
                      </p>
                      <p style="text-align: center">
                        <span
                          ><img
                            src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf3440a70e3.jpg"
                            class="slideImg"
                        /></span>
                      </p>
                      <p style="text-align: center"></p>
                      <p style="text-align: center">
                        <span>当最后一抹红霞褪去</span>
                      </p>
                      <p style="text-align: center">
                        <span
                          >数十个玉兰花似的花灯一齐把整个布达拉宫广场照得如同白昼</span
                        >
                      </p>
                      <p style="text-align: center">
                        <span>布达拉宫也被灯光披上了一层更加神秘的色彩</span>
                      </p>
                      <p style="text-align: center">
                        <span></span
                        ><img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf345f51eab.jpg"
                          class="slideImg"
                        />
                      </p>
                      <p style="text-align: center">
                        <img
                          src="https://res.changsha.cn/upload/12/document_news/110486/20170918/document_news_content_59bf347222a7c.jpg"
                          class="slideImg"
                        />
                      </p>
                      <p style="text-align: right">
                        作者：李觅之&emsp;&emsp;&emsp;
                      </p>
                    </div>
                  </div>
                </div>
              </a-layout-content>
              <a-layout-footer class="footer">
                <a-input-group compact>
                  <a-input
                    placeholder="发表你的评论吧"
                    v-model:value="value1"
                    style="width: calc(100% - 100px); color: black"
                  />
                  <a-button type="primary">Submit</a-button>
                </a-input-group>
              </a-layout-footer>
            </a-layout>
          </a-layout-content>
        </a-layout>
      </a-layout>
    </a-layout>
  </div>
</template>

<script lang="ts" setup></script>

<style scoped>
#components-layout-demo-top-side-2 .logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
}

.ant-row-rtl #components-layout-demo-top-side-2 .logo {
  float: right;
  margin: 16px 0 16px 24px;
}
.footer {
  margin-top: 48px;
}
.slideImg {
  max-width: 90%;
}
.maintitle {
  font: 14px "Microsoft Yahei", sans-serif;
  width: 100%;
  margin: 0px auto;
  font-size: 22px;
  padding: 15px 0px;
  text-align: center;
  color: #0d6895;
  font-weight: bold;
}
.detail_source {
  color: #666;
  font: 14px "Microsoft Yahei", sans-serif;
  width: 100%;
  margin: 0px auto;
  text-align: center;
  padding-bottom: 20px;
  border-bottom: 1px solid #ededed;
}
</style>
