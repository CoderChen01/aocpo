import requests from '../requests'

export const UsersAnalysisData = (opt) => {
    return requests.get('analysis_page/users_analysis_data', {params: opt})
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}

export const PostsAnalysisData = (opt) => {
    return requests.get('analysis_page/posts_analysis_data', {params: opt})
        .then(res => res.data)
        .catch(err => Promise.reject(err))
}