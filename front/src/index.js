import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Projects from './Pages/Projects';
import About from './Pages/About';
import Creditos from './Pages/Creditos';
import { createBrowserRouter, RouterProvider, Route } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />
  },
  {
    path: "/project",
    element: <Projects />
  },
  {
    path: "/about",
    element: <About />
  },
  {
    path: "/creditos",
    element: <Creditos />
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <RouterProvider router={router} />
);
