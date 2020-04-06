import requests from '../requests'

export const GetData = opt => {
    return requests.get('analysis_page/posts_data', {params: opt})
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}