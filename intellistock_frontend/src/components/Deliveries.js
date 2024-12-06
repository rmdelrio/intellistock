import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Table } from 'react-bootstrap';

const Deliveries = () => {
  const [deliveries, setDeliveries] = useState([]);

  // Fetch Deliveries data from API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/deliveries/') // Replace with your actual API endpoint
      .then(response => {
        setDeliveries(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the deliveries data!", error);
      });
  }, []);

  return (
    <Container>
      <Row id="tableRow">
        <Col md={12}>
          <Card className="mb-4">
            <Card.Header>
              <h4>Deliveries</h4>
            </Card.Header>
            <Card.Body>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Order ID</th>
                    <th>Invoice Number</th>
                    <th>Quantity Ordered</th>
                    <th>Quantity Received</th>
                    <th>Expected Delivery Date</th>
                    <th>Delivery Status</th>
                    <th>Total</th>
                  </tr>
                </thead>
                <tbody>
                  {deliveries.map((delivery) => (
                    <tr key={delivery.id}>
                      <td>{delivery.delivery_date}</td>
                      <td>{delivery.order_id}</td>
                      <td>{delivery.invoice_number}</td>
                      <td>{delivery.quantity_ordered}</td>
                      <td>{delivery.quantity_received}</td>
                      <td>{delivery.expected_delivery_date}</td>
                      <td>{delivery.delivery_status}</td>
                      <td>${delivery.total_cost}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Deliveries;
