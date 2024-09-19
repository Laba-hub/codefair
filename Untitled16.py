#!/usr/bin/env python
# coding: utf-8

# In[ ]:


const express = require('express');
const mysql = require('mysql');

const app = express();
app.use(express.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'inventory_system'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to database');
});

// Add new item
app.post('/add-item', (req, res) => {
    const { name, description, sku, quantity, price, supplier_id, category } = req.body;
    const sql = 'INSERT INTO Items (name, description, sku, quantity, price, supplier_id, category) VALUES (?, ?, ?, ?, ?, ?, ?)';
    db.query(sql, [name, description, sku, quantity, price, supplier_id, category], (err, result) => {
        if (err) throw err;
        res.send('Item added');
    });
});

// Update stock level
app.put('/update-stock/:id', (req, res) => {
    const { quantity_change } = req.body;
    const item_id = req.params.id;
    const sql = 'UPDATE Items SET quantity = quantity + ? WHERE item_id = ?';
    db.query(sql, [quantity_change, item_id], (err, result) => {
        if (err) throw err;
        res.send('Stock updated');
    });
});

// View all items
app.get('/items', (req, res) => {
    const sql = 'SELECT * FROM Items';
    db.query(sql, (err, results) => {
        if (err) throw err;
        res.json(results);
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

