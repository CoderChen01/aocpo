import requests from '../requests'

export const SearchSchool = (_word) => {
    return requests.get('task_manager/schools', {params: {word: _word}})
        .then((res) => {
            return res.data
        })
        .catch((err) => {
            return Promise.reject(err)
        })
}

export const HandleTask = (data) => {
    return requests.post('task_manager/addition/', data)
        .then(res => res.data)
        .catch( err => Promise.reject(err))
}