export default [
    {
        path: "/",
        name: "home",
        component: () => import("@/views/HomeView.vue"),
        children: []
    },
    {
        path: "/list",
        name: "list",
        component: () => import("@/views/FormList.vue"),
        children: []
    },
    {
        path: "/create",
        name: "create",
        component: () => import("@/views/FormCreate.vue"),
        children: []
    },
]