import * as methods from './MethodsManager'
const mutations = {
    //保存用户信息
    [methods.GET_USER_INFO](state, payload){
        state.UserInfo = payload
    },
    //切换登录状态
    [methods.LOGIN](state){
        state.IsLogin = true
    },
    //切换退出状态
    [methods.LOGOUT](state){
        state.IsLogin = false
    },
    //获得真任务列表
    [methods.GETTASKSLIST](state, payload) {
        state.TasksList = payload
    },
    //获得假任务列表
    [methods.GETTASKSFALSELIST](state, payload){
        state.FalseTasksList = payload
    },
    //恢复任务
    [methods.RECOVERTASK](state, index){
        const _recover = state.FalseTasksList.splice(index, 1)[0]
        if (_recover.hasOwnProperty('deleted_state')) {
            let _res = {
                running: _recover.running,
                state: _recover.deleted_state,
                school: _recover.school,
                created_date: _recover.created_date,
                updated_date: _recover.updated_date
            }
            state.TasksList.push(_res)
        } else {
            state.TasksList.push(_recover)
        }
    },
    //我的任务里删除
    [methods.MYTASKDEL](state, index){
        const _DelTask = state.TasksList.splice(index, 1)[0]
        state.FalseTasksList.push(_DelTask)
    },
    //任务垃圾箱里的删除
    [methods.FALSETASKDEL](state, index){
        state.FalseTasksList.splice(index, 1)
    },
    //创建任务是及时更新列表
    [methods.CREATETASK](state, payload){
        state.TasksList.push(payload)
    },
    //更新任务
    [methods.UPDATETASK](state, index){
        state.TasksList[index].running = 1
    },
    //递交操作
    [methods.HANDLEOPT](state, payload) {
        state.Opt = payload
    }
}

export default mutations