import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import mutations from './mutations'
import actions from './actions'
import getters from './getters'

//用户信息， 登录状态
const state = {
    UserInfo: {},
    IsLogin: false,
    Opt: {},
    TasksList: [],
    FalseTasksList: []
}

const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})

export default store