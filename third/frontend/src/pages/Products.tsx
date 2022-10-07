import React from "react";
import { Link } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";

export type Product = {
  name: string;
  description: string;
  storeId: typeof uuidv4;
  price: number;
  productId: typeof uuidv4;
};
export type ProductsProps = {
  products: Array<Product>;
};
export const Products: React.FC<ProductsProps> = (props: ProductsProps) => {
  return (
    <>
      <h1>Products</h1>
      <Link to="/">
        <button>Home</button>
      </Link>
      {props.products.map(product => (
        <div key={props.products.indexOf(product)}>
          <h3>{product.name}</h3>
          <p>{product.description}</p>
          <h4>${product.price}</h4>
          <hr />
        </div>
      ))}
    </>
  );
};
