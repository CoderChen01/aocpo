import requests from '../requests'

export const TrueDelTask = opt => {
    return requests.delete('task_manager/removing/', {params: opt})
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}

export const RecoverTask = opt => {
    return requests.put('task_manager/recovering/', opt)
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}