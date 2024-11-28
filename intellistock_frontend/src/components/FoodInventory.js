import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Form, Button, Card, Table, Container, Row, Col } from 'react-bootstrap';

function FoodInventory() {
    const [items, setItems] = useState([]);
    const [newItem, setNewItem] = useState({
        name: '',
        description: '',
        quantity_in_stock: 0,
        reorder_level: 0,
        perishable: false,
        expiration_date: ''
    });

    // Fetch items from backend
    useEffect(() => {
        fetchItems();
    }, []);

    const fetchItems = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/items/');
            setItems(response.data);
        } catch (error) {
            console.error('Error fetching items:', error);
        }
    };

    // Handle input change for new item form
    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewItem((prev) => ({
            ...prev,
            [name]: value
        }));
    };

    // Add new item
    const handleAddItem = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:8000/api/items/', newItem);
            fetchItems();  // Refresh items list
            setNewItem({
                name: '',
                description: '',
                quantity_in_stock: 0,
                reorder_level: 0,
                perishable: false,
                expiration_date: ''
            });
        } catch (error) {
            console.error('Error adding item:', error);
        }
    };

    return (
        <Container className="mt-4">
            <Row>
                <Col md={4}>
                    <Card className="p-3">
                        <h4>Add New Food Item</h4>
                        <Form onSubmit={handleAddItem}>
                            <Form.Group className="mb-2">
                                <Form.Label>Item Name</Form.Label>
                                <Form.Control
                                    type="text"
                                    name="name"
                                    placeholder="Enter item name"
                                    value={newItem.name}
                                    onChange={handleChange}
                                    required
                                />
                            </Form.Group>
                            <Form.Group className="mb-2">
                                <Form.Label>Description</Form.Label>
                                <Form.Control
                                    as="textarea"
                                    name="description"
                                    placeholder="Enter description"
                                    value={newItem.description}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                            <Form.Group className="mb-2">
                                <Form.Label>Quantity in Stock</Form.Label>
                                <Form.Control
                                    type="number"
                                    name="quantity_in_stock"
                                    placeholder="Enter quantity in stock"
                                    value={newItem.quantity_in_stock}
                                    onChange={handleChange}
                                    required
                                />
                            </Form.Group>
                            <Form.Group className="mb-2">
                                <Form.Label>Reorder Level</Form.Label>
                                <Form.Control
                                    type="number"
                                    name="reorder_level"
                                    placeholder="Enter reorder level"
                                    value={newItem.reorder_level}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                            <Form.Group className="mb-2">
                                <Form.Check
                                    type="checkbox"
                                    label="Perishable"
                                    name="perishable"
                                    checked={newItem.perishable}
                                    onChange={() => setNewItem((prev) => ({
                                        ...prev,
                                        perishable: !prev.perishable
                                    }))}
                                />
                            </Form.Group>
                            <Form.Group className="mb-3">
                                <Form.Label>Expiration Date</Form.Label>
                                <Form.Control
                                    type="date"
                                    name="expiration_date"
                                    value={newItem.expiration_date}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                            <Button variant="primary" type="submit">
                                Add Item
                            </Button>
                        </Form>
                    </Card>
                </Col>
                <Col md={8}>
                    <h4>Inventory List</h4>
                    <Table striped bordered hover>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Description</th>
                                <th>Quantity</th>
                                <th>Reorder Level</th>
                                <th>Perishable</th>
                                <th>Expiration Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            {items.map((item) => (
                                <tr key={item.id}>
                                    <td>{item.name}</td>
                                    <td>{item.description}</td>
                                    <td>{item.quantity_in_stock}</td>
                                    <td>{item.reorder_level}</td>
                                    <td>{item.perishable ? 'Yes' : 'No'}</td>
                                    <td>{item.expiration_date || '-'}</td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>
                </Col>
            </Row>
        </Container>
    );
}

export default FoodInventory;
