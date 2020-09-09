const { createProxyMiddleware } = require('http-proxy-middleware');
module.exports = function(app) {
  app.use(
    '/django',
    createProxyMiddleware({
      target: 'http://localhost:8000',
      secure: false
      changeOrigin: true,

    })
  );
};
