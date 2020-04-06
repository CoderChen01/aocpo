import requests from '../requests'

const LoginRes = (data) => {
    return requests.post('login/', data)
        .then(response => response.data)
        .catch(function (error) {
            return Promise.reject(error)
        })
}

export default LoginRes