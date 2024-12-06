import React, { useEffect, useState } from "react";
import { Table, Button } from "react-bootstrap";
import { getItems, deleteItem } from "../../services/api";
import './../../App.css';

const InventoryList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    const response = await getItems();
    setItems(response.data);
  };

  const handleDelete = async (id) => {
    await deleteItem(id);
    fetchItems();
  };

  return (
    <div className="container mt-4">
      <h2>Inventory Control</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Item ID</th>
            <th>Item Description</th>
            <th>Vendor ID</th>
            {/* <th>Vendor Description</th> */}
            <th>Category ID</th>
            <th>Unit Cost</th>
            <th>Quantity On Hand</th>
            <th>Total Value</th>
            <th>Suggested Qty to Order</th>
            <th>Actual to Order</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={item.item_id}>
              <td>{index + 1}</td>
              <td>{item.item_id}</td>
              <td>{item.item_description}</td>
              <td>{item.vendor}</td>
              <td>{item.category}</td>
              <td>{item.unit_cost}</td>
              <td>{item.quantity_on_hand}</td>
              <td>{(item.unit_cost * item.quantity_on_hand).toFixed(2)}</td>
              <td>{item.suggested_quantity_to_order}</td>
              <td>{item.actual_quantity_to_order}</td>
              <td>
                <Button variant="warning" size="sm">Edit</Button>{" "}
                <Button variant="danger" size="sm" onClick={() => handleDelete(item.id)}>Delete</Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default InventoryList;
