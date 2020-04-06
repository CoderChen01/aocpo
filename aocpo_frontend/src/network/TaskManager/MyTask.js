import requests from '../requests'

export const GetTasks = _data => {
    return requests.get('task_manager/tasks', {params: {username: _data}})
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}

export const FalseDelTask = _data => {
    return requests.delete('task_manager/removing/', {params: _data})
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}

export const UpdateTask = _data => {
    return requests.put('task_manager/upgrade/', _data)
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}