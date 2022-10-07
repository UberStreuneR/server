import React from "react";
import { Link } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";

export type Store = {
  name: string;
  city: string;
  country: string;
  currency: string;
  domain: string;
  storeId: typeof uuidv4;
};
export type StoresProps = {
  stores: Array<Store>;
};
export const Stores: React.FC<StoresProps> = (props: StoresProps) => {
  return (
    <>
      <h1>Stores</h1>
      <Link to="/">
        <button>Home</button>
      </Link>
      {props.stores.map(store => (
        <div key={props.stores.indexOf(store)}>
          <h3>{store.name}</h3>
          <p>
            {store.city}, {store.country}
          </p>
          <h4>Currency: {store.currency}</h4>
          <hr />
        </div>
      ))}
    </>
  );
};
