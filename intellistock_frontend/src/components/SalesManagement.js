import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Table } from 'react-bootstrap';

const SalesManagement = () => {
  const [dailySales, setDailySales] = useState([]);
  const [monthlySales, setMonthlySales] = useState([]);

  // Fetch Daily Sales data from API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/daily-sales/') // Replace with your actual API endpoint
      .then(response => {
        setDailySales(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the daily sales data!", error);
      });
  }, []);

  // Fetch Monthly Sales data from API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/monthly-sales/') // Replace with your actual API endpoint
      .then(response => {
        setMonthlySales(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the monthly sales data!", error);
      });
  }, []);

  return (
    <Container>
      <Row id="tableRow">
        {/* Daily Sales Section */}
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header>
              <h4>Daily Sales</h4>
            </Card.Header>
            <Card.Body>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Total Sales</th>
                    <th>Number of Transactions</th>
                    <th>Inventory Usage</th>
                    <th>Waste Amount</th>
                  </tr>
                </thead>
                <tbody>
                  {dailySales.map((sale) => (
                    <tr key={sale.id}>
                      <td>{sale.sales_date}</td>
                      <td>${sale.total_sales}</td>
                      <td>{sale.number_of_transactions}</td>
                      <td>{sale.inventory_usage}</td>
                      <td>${sale.waste_amount}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>

        {/* Monthly Sales Section */}
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header>
              <h4>Monthly Sales</h4>
            </Card.Header>
            <Card.Body>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Quarter</th>
                    <th>Total Sales</th>
                    <th>Average Sales</th>
                    <th>Profit Percentage</th>
                    <th>Number of Transactions</th>
                    <th>Inventory Usage</th>
                  </tr>
                </thead>
                <tbody>
                  {monthlySales.map((sale) => (
                    <tr key={sale.id}>
                      <td>{sale.date}</td>
                      <td>{sale.quarter}</td>
                      <td>${sale.total_sales}</td>
                      <td>${sale.average_sales}</td>
                      <td>{sale.profit_percentage}%</td>
                      <td>{sale.number_of_transactions}</td>
                      <td>{sale.inventory_usage}</td>
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

export default SalesManagement;
