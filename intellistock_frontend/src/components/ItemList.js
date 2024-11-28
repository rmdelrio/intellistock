import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ItemList() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/items/')
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Inventory Items</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>{item.name} - {item.quantity_in_stock}</li>
                ))}
            </ul>
        </div>
    );
}

export default ItemList;
