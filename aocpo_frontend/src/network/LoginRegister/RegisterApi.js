import requests from '../requests'

//注册请求
export const RegisterApi = (data) => {
    return requests.post('register/', data)
        .then(response => response.data)
        .catch(error => Promise.reject(error))
}

//检查手机号是否注册请求
export const CheckRegisteredApi = (data) => {
    return requests.get('register/check_username', {params: {username: data}})
        .then(response => response.data)
        .catch(error => Promise.reject(error))
}