import React from "react";
import { Product } from "./pages/Products";
import { Store } from "./pages/Stores";

type setter =
  | React.Dispatch<React.SetStateAction<Product[]>>
  | React.Dispatch<React.SetStateAction<Store[]>>;
export const request = (path: string, setter: setter) => {
  fetch(`http://localhost:8000/${path}`)
    .then(data => data.json())
    .then(res => {
      setter(res);
      console.log(res);
    });
};
