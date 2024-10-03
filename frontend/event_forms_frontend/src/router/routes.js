export default [
    {
        path: "/",
        name: "HomeView",
        component: () => import("@/views/HomeView.vue"),
        children: []
    },
    {
        path: "/list",
        name: "FormListView",
        component: () => import("@/views/FormListView.vue"),
        children: []
    },
    {
        path: "/create",
        name: "FormCreateView",
        component: () => import("@/views/FormCreateView.vue"),
        children: []
    },
    {
        path: "/update/:id",
        name: "FormUpdateView",
        component: () => import("@/views/FormUpdateView.vue"),
        children: []
    },
]