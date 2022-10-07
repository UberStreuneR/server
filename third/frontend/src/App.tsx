import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Products, ProductsProps } from "./pages/Products";
import { Stores, StoresProps } from "./pages/Stores";
import { Contacts } from "./pages/Contacts";
import Home from "./pages/Home";
import { request } from "./utils";
function App() {
  const [products, setProducts] = useState<ProductsProps["products"]>([]);
  const [stores, setStores] = useState<StoresProps["stores"]>([]);
  useEffect(() => {
    request("products", setProducts);
    request("stores", setStores);
  }, []);
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Products products={products} />} />
          <Route path="/stores" element={<Stores stores={stores} />} />
          <Route path="/contacts" element={<Contacts />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
