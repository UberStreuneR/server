import React from "react";
import { Link } from "react-router-dom";
import { STATIC_HOST } from "../data/constants";

export function Contacts() {
  return (
    <>
      <Link to="/">
        <button>Home</button>
      </Link>
      <div>Our employees:</div>
      <img src={`${STATIC_HOST}/npc.jpg`} alt="" />
      <div style={{ maxWidth: 500 }}>
        They cannot possibly have contacts. At least their image is served
        through Nginx, as evidenced by the image source referring to port 80 of
        localhost.
      </div>
    </>
  );
}
