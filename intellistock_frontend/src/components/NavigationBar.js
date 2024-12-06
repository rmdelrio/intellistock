import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import { Link } from "react-router-dom";
import './../App.css';

const NavigationBar = () => (
  <Navbar bg="dark" variant="dark" expand="lg">
    <Navbar.Brand as={Link} to="/">IntelliStock</Navbar.Brand>
    <Nav className="mr-auto">
      {/* <Nav.Link as={Link} to="/inventory">Inventory</Nav.Link>
      <Nav.Link as={Link} to="/orders">Orders</Nav.Link> */}
      <Nav.Link as={Link} to="/dashboard">Dashboard</Nav.Link>
      <Nav.Link as={Link} to="/sales-management">Sales Management</Nav.Link>
      <Nav.Link as={Link} to="/inventory">Inventory Control</Nav.Link>
      <Nav.Link as={Link} to="/orders">Order Dashboard</Nav.Link>
      <Nav.Link as={Link} to="/deliveries">Deliveries</Nav.Link>
    </Nav>
  </Navbar>
);

export default NavigationBar;
