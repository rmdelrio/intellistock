// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// import React from 'react';
// import ItemList from './components/ItemList';
// import FoodInventory from './components/FoodInventory';

// function App() {
//     return (
//         <div className="App">
//             <ItemList />
//             <FoodInventory />
//         </div>
        
//     );
// }

// export default App;



// ======================================

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavigationBar from "./components/NavigationBar";
import SalesManagement from "./components/SalesManagement";
import Deliveries from "./components/Deliveries";
import InventoryList from "./components/Inventory/InventoryList";
import OrderList from "./components/Orders/OrderList";

const App = () => (
  <Router>
    <NavigationBar />
    <Routes>
      <Route path="/inventory" element={<InventoryList />} />
      <Route path="/orders" element={<OrderList />} />
      <Route path="/sales-management" element={<SalesManagement/>} />
      <Route path="/deliveries" element={<Deliveries/>} />
    </Routes>
  </Router>
);

export default App;



