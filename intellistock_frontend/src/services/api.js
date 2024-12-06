import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const getItems = () => axios.get(`${API_BASE_URL}/items/`);
export const getItemById = (id) => axios.get(`${API_BASE_URL}/items/${id}/`);
export const createItem = (data) => axios.post(`${API_BASE_URL}/items/`, data);
export const updateItem = (id, data) => axios.put(`${API_BASE_URL}/items/${id}/`, data);
export const deleteItem = (id) => axios.delete(`${API_BASE_URL}/items/${id}/`);

export const getOrders = () => axios.get(`${API_BASE_URL}/orders/`);
export const createOrder = (data) => axios.post(`${API_BASE_URL}/orders/`, data);
