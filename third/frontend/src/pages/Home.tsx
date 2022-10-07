import React from "react";
import { Link } from "react-router-dom";
import { STATIC_HOST } from "../data/constants";
export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <nav>
        <Link to="products" style={{ marginRight: 3 }}>
          <button>Products</button>
        </Link>
        <Link to="stores">
          <button>Stores</button>
        </Link>
        <Link to="contacts">
          <button>Contacts</button>
        </Link>
      </nav>
      <div>
        <h3>Homepage image: </h3>
        <img src={`${STATIC_HOST}/image.png`} alt="" />
      </div>
    </div>
  );
}
