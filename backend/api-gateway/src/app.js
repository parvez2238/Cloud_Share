const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Proxy rules
app.use('/api/auth', createProxyMiddleware({ target: 'http://auth-service:5001', changeOrigin: true }));
app.use('/api/files', createProxyMiddleware({ target: 'http://file-management-service:5002', changeOrigin: true }));
// Add other services here...

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`API Gateway running on port ${PORT}`));
