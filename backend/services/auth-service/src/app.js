const express = require('express');
const dotenv = require('dotenv');
const mongoose = require('mongoose');
const authRoutes = require('./routes/authRoutes');

dotenv.config();
const app = express();

app.use(express.json());
app.use('/api/auth', authRoutes);

mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => console.log('Auth Service connected to MongoDB'));

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`Auth Service running on port ${PORT}`));
