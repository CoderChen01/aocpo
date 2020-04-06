module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        'components': '@/components',
        'assets': '@/assets',
        'network': '@/network',
        'views': '@/views',
        'store': '@/store',
        'common': '@/common'
      }
    }
  },
  assetsDir: 'static'
}
