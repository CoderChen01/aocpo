import Vue from 'vue'
import VueRouter from 'vue-router'
import Analysis from "../views/Analysis/AnalysisPage";

Vue.use(VueRouter)

const Login = () => import('views/Login/Login')
const Register = () => import('views/Register/Register')
const TaskManager = () => import('views/TaskManager/TaskManager')
const AnalysisPage = () => import('views/Analysis/AnalysisPage')
const PublicOpinion = () => import('views/Analysis/yuqing/PublicOpinionSurveys')
const InfomationGather = () => import('views/Analysis/info/InfomationGather')
const NotFound = () => import('views/NotFound')

const routes = [
    {
        path: '/',
        redirect: {name: 'task_manager'}
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        meta: {
            title: 'aocpo-登录'
        }
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
        meta: {
            title: 'aocpo-注册'
        }
    },
    {
        path: '/aocpo/TaskMananger',
        name: 'task_manager',
        component: TaskManager,
        beforeEnter(to, form, next){
            window.document.title = to.meta.title
            next()
        },
        meta: {
            title: 'aocpo-任务管理',
            requireAuth: true
        }
    },
    {
        path: '/aocpo/AnalysisPage',
        name: 'analysis',
        component: AnalysisPage,
        children: [
            {
                path: 'PublicOpinionSurveys',
                name: 'yuqing',
                component: PublicOpinion,
                meta: {
                    title: 'aocpo-分析页面-舆情总览',
                    requireAuth: true
                }
            },
            {
                path: 'InfomationGather',
                name: 'info',
                component: InfomationGather,
                meta: {
                    title: 'aocpo-分析页面-信息汇总',
                    requireAuth: true
                }
            }
        ],
        meta: {
            title: 'aocpo-分析页面',
            requireAuth: true
        }
    },
    {
        path: '*',
        component: NotFound,
        meta: {
            title: '页面走丢了...'
        }
    }
]

const router = new VueRouter({
    routes,
    mode: 'history',
    linkActiveClass: 'active'
})

export default router
