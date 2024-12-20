import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import loginPage from "@/views/loginPage.vue";
import registerPage from "@/views/registerPage.vue";
import HomePage from "@/views/homePage.vue";
import post_postPage from "@/views/post_postPage.vue";
import documentCenterPage from "@/views/docunmentCenterPage.vue";
import posts from "@/views/posts.vue";
import mapService from "@/views/mapService.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/user/documentCenter",
    name: "documentCenter",
    component: documentCenterPage,
  },
  {
    path: "/user/post_post",
    name: "post_post",
    component: post_postPage,
  },
  {
    path: "/user/login",
    name: "login",
    component: loginPage,
  },
  {
    path: "/user/register",
    name: "register",
    component: registerPage,
  },
  {
    path: "/_posts/posts",
    name: "posts",
    component: posts,
  },
  {
    path: "/map_service",
    name: "mapService",
    component: mapService,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
