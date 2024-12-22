<template>
  <div class="documentCenterPage">
    <a-table :columns="columns" :data-source="data">
      <template #headerCell="{ column }">
        <template v-if="column.key === 'name'">
          <span> 活动主题 </span>
        </template>
      </template>

      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'name'">
          <a @click="handleClickName(record.id)">
            {{ record.name }}
          </a>
        </template>
        <template v-else-if="column.key === 'tags'">
          <span>
            {{ record.tags }}
          </span>
        </template>
      </template>
    </a-table>
  </div>
</template>

<style scoped>
.documentCenterPage {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;
  margin-top: 10px;
}
</style>

<script lang="ts" setup>
import { message } from "ant-design-vue";
import { useRouter } from "vue-router";

const router = useRouter();
const handleClickName = (key: string) => {
  router.push({ path: "/_posts/postsLayout", query: { id: key } });
};

const columns = [
  {
    name: "活动主题",
    dataIndex: "name",
    key: "name",
  },
  {
    title: "活动时间",
    dataIndex: "time",
    key: "time",
  },
  {
    title: "活动地点",
    dataIndex: "address",
    key: "address",
  },
  {
    title: "调查人",
    key: "persons",
    dataIndex: "persons",
  },
  {
    title: "年龄",
    dataIndex: "age",
    key: "age",
  },
  {
    title: "活动概要",
    dataIndex: "tags",
    key: "tags",
  },
];

// const data = [
//   {
//     key: "1",
//     name: "敦煌研究",
//     persons: "刘一凡",
//     time: "2018-02-01",
//     age: 21,
//     address: "敦煌",
//     tags: "研究敦煌",
//   },
//   {
//     key: "2",
//     name: "Jim Green",
//     persons: "刘一凡",
//     age: 42,
//     address: "London No. 1 Lake Park",
//     tags: ["loser"],
//   },
//   {
//     key: "3",
//     name: "Joe Black",
//     age: 32,
//     address: "Sidney No. 1 Lake Park",
//     tags: ["cool", "teacher"],
//   },
// ];
import { ref } from "vue";
import { getBasicInformation } from "@/api/basicInfomation";
import { useRouter } from "vue-router";

// get data
const data = ref([]);
const fetchData = async () => {
  const res = await getBasicInformation();
  if (res.data.data) {
    data.value = res.data.data;
  } else {
    message.error("获取数据失败");
  }
};
fetchData();
</script>
