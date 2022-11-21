import React, { useState, useEffect } from "react";
import Cookies from "js-cookie";

const makeRequest = async (endpoint: string) => {
  return fetch(`http://localhost:8000/${endpoint}`, {
    credentials: "include",
    // headers: { "Content-Type": "application/json", Accept: "application/json" },
  })
    .then(res => res.json())
    .catch(error => console.log(error));
};

function App() {
  const [username, setUsername] = useState(Cookies.get("username"));
  const [theme, setTheme] = useState(Cookies.get("lightThemeOn"));
  const [language, setLanguage] = useState(Cookies.get("language"));
  const [message, setMessage] = useState({ message: " ", lightThemeOn: theme });
  const [crucial, setCrucial] = useState("");

  const [images, setImages] = useState({});
  console.log("Hello world");
  useEffect(() => {
    console.log(username, theme, language);
    let data = makeRequest("cookie");
    data.then(res => setMessage(res));
    let imageData = makeRequest("fake-data");
    imageData.then(res => setImages(res));
  }, []);

  const reverseTheme = () => {
    setTheme(!theme);
    Cookies.set("lightThemeOn", !theme);
  };

  const handleUsername = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
    Cookies.set("username", e.target.value);
  };

  const handleLanguage = (e: React.ChangeEvent<HTMLInputElement>) => {
    setLanguage(e.target.value);
    Cookies.set("language", e.target.value);
  };

  const getMessage = () => {
    let data = makeRequest("cookie");
    data.then(res => {
      console.log(res);
      setMessage(res);
    });
  };

  const getCrucialData = () => {
    let data = makeRequest("crucial-data");
    data.then(res => {
      console.log(res);
      setCrucial(res);
    });
  };

  return (
    <div className="App">
      <div>
        <input
          type="text"
          name="username"
          value={username}
          onChange={handleUsername}
        />
        <label htmlFor="username">Your username</label>
      </div>
      <div>
        <input
          type="checkbox"
          name="light-theme"
          checked={theme}
          onClick={reverseTheme}
        />
        <label htmlFor="light-theme">Use light theme?</label>
      </div>
      <div>
        <input
          type="text"
          name="language"
          value={language}
          onChange={handleLanguage}
        />
        <label htmlFor="language">Language</label>
      </div>
      <button onClick={getMessage}>Get Server Message</button>
      <button onClick={getCrucialData}>Get Crucial Data</button>

      <div>Message: {JSON.stringify(message)}</div>
      <div>Crucial data: {JSON.stringify(crucial)}</div>
      {/* <div>{message.message}</div> */}
      {/* <div>Light theme is {message.lightThemeOn == "true" ? "on" : "off"}</div> */}
      <img
        src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUA
    AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO
        9TXL0Y4OHwAAAABJRU5ErkJggg=="
        alt="Red dot"
      />
    </div>
  );
}

export default App;
