import Vue from 'vue'
import aocpoApp from './acopoApp.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import store from './store'
import {
  GET_USER_INFO,
  LOGIN,
} from 'store/MethodsManager'

import {
  Input,
  Button,
  Row,
  Col,
  Container,
  Header,
  Aside,
  Main,
  Footer,
  Icon,
  PageHeader,
  Tabs,
  TabPane,
  Autocomplete,
  Link,
  Loading,
  Message,
  MessageBox,
  Dialog,
  Table,
  TableColumn,
  Menu,
  MenuItem,
  Select,
  Option,
  RadioGroup,
  RadioButton,
  DatePicker,
  Radio,
  scrollbar,
  InfiniteScroll,
  Backtop,
  Card,
  DropdownMenu,
  DropdownItem,
  Dropdown,
  Tooltip
} from 'element-ui'
Vue.config.productionTip = true
//cookies
Vue.use(VueCookies)
Vue.$cookies.config('7d')
//element-ui
Vue.use(Input)
    .use(Button)
    .use(Button)
    .use(Row)
    .use(Col)
    .use(Container)
    .use(Header)
    .use(Aside)
    .use(Main)
    .use(Footer)
    .use(Icon)
    .use(PageHeader)
    .use(Tabs)
    .use(TabPane)
    .use(Autocomplete)
    .use(Link)
    .use(Dialog)
    .use(Table)
    .use(TableColumn)
    .use(Loading.directive)
    .use(Menu)
    .use(MenuItem)
    .use(Option)
    .use(Select)
    .use(RadioGroup)
    .use(RadioButton)
    .use(DatePicker)
    .use(Radio)
    .use(InfiniteScroll)
    .use(scrollbar)
    .use(Backtop)
    .use(Card)
    .use(DropdownMenu)
    .use(DropdownItem)
    .use(Dropdown)
    .use(Tooltip)
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$message = Message
Vue.prototype.$loading = Loading.service

//路由守卫
router.beforeEach((to, from, next) => {
  window.document.title = to.meta.title
  if(to.meta.requireAuth){
    if(!Vue.$cookies.isKey('aocpo_cookies')){
      next({name: 'login'})
    } else{
      const _UserInfo = Vue.$cookies.get('aocpo_cookies')
      store.commit(GET_USER_INFO, _UserInfo)
      store.commit(LOGIN)
      next()
    }
  } else{
    if(to.meta.title === 'aocpo-登录') {
      if(!Vue.$cookies.isKey('aocpo_cookies')) {
        next()
      } else{
        const _UserInfo = Vue.$cookies.get('aocpo_cookies')
        store.commit(GET_USER_INFO, _UserInfo)
        store.commit(LOGIN)
        next()
      }
    } else {
      next()
    }
  }
})

//Vue实例
new Vue({
  store,
  router,
  render: h => h(aocpoApp),
}).$mount('#app')
