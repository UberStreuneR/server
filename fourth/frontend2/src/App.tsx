import { useState, useEffect } from "react";

const makeRequest = async (endpoint: string) => {
  return fetch(`http://localhost:8000/${endpoint}`, {
    credentials: "include",
    // headers: { "Content-Type": "application/json", Accept: "application/json" },
  })
    .then(res => res.json())
    .catch(error => console.log(error));
};

function App() {
  const [images, setImages] = useState({ first: "", second: "", third: "" });

  useEffect(() => {
    let data = makeRequest("fake-data");
    data.then(res => {
      setImages(res);
      console.log(res);
    });
  }, []);

  return (
    <div className="App">
      <img src={"data:image/png;base64," + images["first"]} alt="data" />
      <img src={"data:image/png;base64," + images["second"]} alt="data" />
      <img src={"data:image/png;base64," + images["third"]} alt="data" />
    </div>
  );
}

export default App;
