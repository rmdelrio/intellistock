import React, { useEffect, useState } from "react";
import { Table, Button } from "react-bootstrap";
import { getOrders } from "../../services/api";

const OrderList = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    const response = await getOrders();
    setOrders(response.data);
  };

  return (
    <div className="container mt-4">
      <h2>Orders</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Order ID</th>
            <th>Order Date</th>
            <th>Expected Delivery Date</th>
            <th>Total Quantity Ordered</th>
            {/* <th>Total Amount</th> */}
            <th>Status</th>
            <th>Projected Sales</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order, index) => (
            <tr key={order.id}>
              <td>{index + 1}</td>
              <td>{order.order_id}</td>
              <td>{order.order_date}</td>
              <td>{order.expected_delivery_date}</td>
              <td>{order.total_quantity_ordered}</td>              
              <td>{order.status}</td>
              <td>{order.horizon_projected_sales}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default OrderList;
