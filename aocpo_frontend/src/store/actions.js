import * as  methods from './MethodsManager'
import {GetTasks} from "network/TaskManager/MyTask"

const actions = {
    //及时的更新任务
    [methods.CREATETASK](context){
        const username = context.state.UserInfo.username
        GetTasks(username)
            .then(res => {
                if(res.status == 1000) {
                    context.commit(methods.GETTASKSLIST, res.data.true_data)
                    context.commit(methods.GETTASKSFALSELIST, res.data.false_data)
                } else {
                    if (res.status != 2000) {
                        this.$message({
                            type: 'error',
                            message: '服务器异常， 请联系管理员！',
                            duration: 2000,
                            center: true
                        })
                    }
                }
            })
            .catch(err => {
                console.log(err)
            })
    }
}

export default actions